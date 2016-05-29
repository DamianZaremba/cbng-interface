import json
import logging

from cbng_review.forms import SignupForm
from cbng_review.models import Classification, UserAccessRequest, Edit
from cbng_review.utils import get_next_to_review
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

logger = logging.getLogger(__name__)


def stats(request):
    stats = {}
    for stat in Classification.objects.all().values('user') \
            .annotate(total=Count('user')).order_by('total'):
        stats[User.objects.get(id=stat['user']).username] = stat['total']

    data = {
        'stats': sorted(stats.items())
    }

    return render(request, 'cbng_review/stats.html', data)


@permission_required('perms.cbng_review.can_review')
def reviewer(request):
    return render(request, 'cbng_review/reviewer.html', {})


def about(request):
    form = SignupForm()
    if request.user.is_authenticated():
        form.username = request.user.username

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            UserAccessRequest.objects.create(user=request.user,
                                             comments=form.cleaned_data['comment'])
            messages.add_message(request, messages.SUCCESS,
                                 'Access request submitted')

    access_requests = 0
    if request.user.is_authenticated():
        access_requests = UserAccessRequest.objects.filter(user=request.user).count()

    return render(request, 'cbng_review/about.html', {
        'form': form,
        'access_requests': access_requests
    })


@permission_required('perms.cbng_review.can_review')
def japi_next(request):
    '''
    Return the next review to score for the current user

    :param request:
    :return:
    '''
    edit = get_next_to_review(request.user)
    return HttpResponse(json.dumps({
        'id': edit.id,
        'diff': edit.diff,
        'article': edit.article
    }))


@permission_required('perms.cbng_review.can_review')
def japi_score(request, edit_id, score_id):
    '''
    Score a review for the current user

    :param request:
    :return:
    '''
    edit = get_object_or_404(Edit, id=int(edit_id))

    # Sanity test
    if not request.GET.get('force', False):
        if edit.classification != Edit.CLASSIFICATION_UNKNOWN and edit.classification != score_id:
            return HttpResponse(json.dumps({'status': 'OK', 'confirm': True}))

    valid_statues = [x[0] for x in Classification.CLASSIFICATIONS]
    if int(score_id) not in valid_statues:
        logger.error('Invalid classification %s requested for %s by %s' % (score_id,
                                                                           edit_id,
                                                                           request.user.username))
        return HttpResponse(json.dumps({'status': 'ERROR'}))

    try:
        Classification.objects.create(user=request.user,
                                      comment=request.GET.get('comment', ''),
                                      classification=int(score_id),
                                      edit=edit)
    except Exception, e:
        print(e)
        logger.error('Failed to save classification', e)
        return HttpResponse(json.dumps({'status': 'ERROR'}))

    return HttpResponse(json.dumps({'status': 'OK'}))


@permission_required('perms.cbng_review.can_review_admin')
def admin(request):
    return render(request, 'cbng_review/admin/home.html', {})


@permission_required('perms.cbng_review.can_review_admin')
def admin_edits(request):
    return render(request, 'cbng_review/admin/edits.html', {})


@permission_required('perms.cbng_review.can_review_admin')
def admin_edit(request, edit_id):
    return render(request, 'cbng_review/admin/edit.html', {})
