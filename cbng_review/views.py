import json

from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render


def stats(request):
    return render(request, 'cbng_review/stats.html', {})


@permission_required('perms.cbng_review.can_review')
def reviewer(request):
    return render(request, 'cbng_review/reviewer.html', {})


def about(request):
    return render(request, 'cbng_review/about.html', {})


@permission_required('perms.cbng_review.can_review')
def japi_next(request):
    '''
    Return the next review to score for the current user

    :param request:
    :return:
    '''
    return HttpResponse(json.dumps({}))


@permission_required('perms.cbng_review.can_review')
def japi_score(request):
    '''
    Score a review for the current user

    :param request:
    :return:
    '''
    return HttpResponse(json.dumps({}))
