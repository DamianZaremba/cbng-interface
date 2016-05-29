from cbng_report.models import Users
import logging

from django.contrib.auth.models import Group
from tastypie.models import ApiKey

logger = logging.getLogger(__name__)


def create_api_token(instance, **kwargs):
    '''
    Signal based token creation.

    Ensures new users get an ApiKey.
    '''
    if kwargs['created'] is True:
        try:
            ApiKey.objects.get(user=kwargs['user'])
        except ApiKey.DoesNotExist:
            ApiKey.objects.create(user=kwargs['user'])


def map_user_rights(instance, **kwargs):
    '''
    Signal based permission assignment.
    Adds users into groups based on the old Users table.
    '''
    if kwargs['created'] is not True:
        return

    user = kwargs['user']

    # This is a special user internally
    if user.username == 'System':
        return

    # Add existing privileged users to the reviewers group
    # and give them admin/superuser access if required
    try:
        u = Users.objects.get(username=user.username)
    except Users.DoesNotExist:
        pass
    else:
        if u.admin == 1:
            try:
                user.groups.add(Group.objects.get(name='reviewers'))
            except Group.DoesNotExist, e:
                logger.error('Could not get reviewers group', e)

        if u.superadmin == 1:
            try:
                user.groups.add(Group.objects.get(name='admins'))
            except Group.DoesNotExist, e:
                logger.error('Could not get admins group', e)

            user.is_admin = True
            user.is_superuser = True

        user.email = u.email

    # Add everyone to the reporters group
    try:
        user.groups.add(Group.objects.get(name='reporters'))
    except Group.DoesNotExist, e:
        logger.error('Could not get reporters group', e)

    user.save()
