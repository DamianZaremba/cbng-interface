import json
import logging
from datetime import datetime

from cbng_report.forms import ReportForm, CommentForm
from cbng_report.models import Vandalism, Report, Comment
from cbng_report.utils import get_next_report
from cbng_backend.utils import send_msg_to_relay
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

logger = logging.getLogger(__name__)


def home(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            comment = form.cleaned_data['comment']
            try:
                v = Vandalism.objects.get(id=id)
            except Vandalism.DoesNotExist:
                messages.add_message(request, messages.ERROR,
                                     'Could not find revert ID %d' % id)
            else:
                if not v.reverted:
                    messages.add_message(request, messages.ERROR,
                                         'Edit with revert ID %d was NOT reverted!' % id)
                else:
                    try:
                        r = Report.objects.get(vandalism=v)
                    except Report.DoesNotExist:
                        r = Report(vandalism=v,
                                   timestamp=datetime.now,
                                   status=0)

                        if request.user.is_authenticated():
                            r.reporterid = request.user.id
                            r.reporter = request.user.username
                        else:
                            r.reporterid = -1
                            r.reporter = 'Anonymous'

                        r.save()

                    if comment:
                        c = Comment()
                        c.vandalism = v
                        c.timestamp = datetime.now
                        if request.user.is_authenticated():
                            c.userid = request.user.id
                        else:
                            c.userid = -1
                        c.comment = comment
                        c.save()

                    send_msg_to_relay(('[[report:%(id)d]] comment ',
                                       'http://tools.wmflabs.org/cluebotng/report/%(id)d',
                                       '* %(user)s * New Report' % {
                                           'id': r.id,
                                           'user': request.user.username,
                                       }))

                    return redirect('/report/%d' % r.revertid.id)

    return render(request, 'cbng_report/home.html', {'form': ReportForm()})


def list(request):
    reports_list = Report.objects.order_by('-timestamp').all()
    paginator = Paginator(reports_list, 50)

    page = request.GET.get('page')
    try:
        reports = paginator.page(page)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)

    return render(request, 'cbng_report/list.html', {'reports': reports})


def report(request, id):
    vandalism = get_object_or_404(Vandalism, id=id)
    try:
        report = Report.objects.get(vandalism=vandalism)
    except Report.DoesNotExist:
        report = None

    if request.method == 'POST' and request.user.has_perm('cbng_report.can_comment'):
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(vandalism=vandalism,
                                   user=request.user,
                                   timestamp=datetime.utcnow(),
                                   comment=form.cleaned_data['comment'].encode('utf-8'))
            messages.add_message(request, messages.SUCCESS, 'Added comment')

    return render(request, 'cbng_report/report.html', {
        'vandalism': vandalism,
        'report': report,
        'comments': Comment.objects.filter(vandalism=vandalism).order_by('-timestamp'),
        'form': CommentForm()
    })


@permission_required('perms.cbng_report.can_review')
def report_status_change(request, revert_id, status_id):
    '''
    Crappy json 'API' for scoring a report.

    TODO - add 'redirect on score' functionality
    :param request:
    :param revert_id:
    :param status_id:
    :return:
    '''
    valid_statues = [x[0] for x in Report.STATUSES]
    if int(status_id) not in valid_statues:
        logger.error('Invalid status %s requested for %s by %s' % (status_id,
                                                                   revert_id,
                                                                   request.user.username))
        return HttpResponse(json.dumps({'status': 'ERROR'}))

    try:
        v = Vandalism.objects.get(id=revert_id)
        r = Report.objects.get(vandalism=v)
        r.status = int(status_id)
        r.save()
    except Exception as e:
        logger.error('Failed to save status %d on %d' %
                     (status_id, revert_id), e)
    else:

        try:
            comment = '%s has marked this report as "%s".' % (request.user.username,
                                                              r.get_status_display())
            Comment.objects.create(vandalism=v,
                                   timestamp=datetime.now(),
                                   user=request.user,
                                   comment=comment)

            send_msg_to_relay(('[[report:%(id)d]] comment ',
                               'http://tools.wmflabs.org/cluebotng/report/%(id)d',
                               '* %(user)s * %(comment)s' % {
                                   'id': r.id,
                                   'user': request.user.username,
                                   'comment': comment
                               }))
        except Exception as e:
            logger.error(
                'Failed to save comment for change on %s' % revert_id, e)

        return HttpResponse(json.dumps({
            'status': 'OK',
            'report_status': r.get_status_display(),
            'next': get_next_report(request.user)
        }))

    return HttpResponse(json.dumps({'status': 'ERROR'}))
