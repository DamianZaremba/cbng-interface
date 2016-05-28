from cbng_report.models import Users
import logging

from django.contrib.auth.models import Group
from tastypie.models import ApiKey

logger = logging.getLogger(__name__)

def create_api_token(sender, user, request, **kwargs):
    try:
        ApiKey.objects.get(user=user)
    except ApiKey.DoesNotExist:
        ApiKey.objects.create(user=user)


def map_user_rights(sender, user, request, **kwargs):
    try:
        u = Users.objects.get(username=user.username)
    except Users.DoesNotExist:
        pass
    else:
        if u.admin == 1:
            try:
                user.groups.add(Group.objects.get(name='reviewers'))
            except Group.DoesNotExist, e:
                logger.error('Could not get reviwers group', e)

        if u.superadmin == 1:
            user.admin = True
            user.staff = True

        user.email = u.email
        user.save()
