from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import logging
from tastypie.models import ApiKey

logger = logging.getLogger(__name__)


def bad_request(request):
    return render(request, 'cbng_interface/errors/400.html')


def permission_denied(request):
    return render(request, 'cbng_interface/errors/403.html')


def four_oh_four(request):
    return render(request, 'cbng_interface/errors/404.html')


def five_hundred(request):
    return render(request, 'cbng_interface/errors/500.html')


def signup(request):
    return render(request, 'cbng_interface/auth/signup.html')


@login_required
def profile(request):
    data = {}

    try:
        data['api_key'] = ApiKey.objects.get(user=request.user).key
    except ApiKey.DoesNotExist:
        logger.warn('User %s does not have an API key', request.user)
        pass

    return render(request, 'cbng_interface/auth/profile.html', data)
