import logging

from cbng_interface.models import Preferences
from cbng_report.models import User
from django.contrib.auth.models import Group
from tastypie.models import ApiKey

logger = logging.getLogger(__name__)


def create_api_token(sender, user, request, **kwargs):
    '''
    Signal based token creation.

    Ensures new users get an ApiKey.
    '''
    try:
        ApiKey.objects.get(user=user)
    except ApiKey.DoesNotExist:
        ApiKey.objects.create(user=user)


def map_user_rights(sender, user, request, **kwargs):
    '''
    Signal based permission assignment.
    Adds users into groups based on the old Users table.
    '''

    # This is a special user internally
    if user.username == 'System':
        return

    # Add existing privileged users to the reviewers group
    # and give them admin/superuser access if required
    try:
        u = User.objects.get(username=user.username)
    except User.DoesNotExist:
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

        user.email = u.email

    # Super super admins
    if user.username in ['RichSmith', 'Cobi', 'Crispy1989', 'DamianZaremba']:
        user.is_admin = True
        user.is_superuser = True

    # Add everyone to the reporters group
    try:
        user.groups.add(Group.objects.get(name='reporters'))
    except Group.DoesNotExist, e:
        logger.error('Could not get reporters group', e)

    user.save()


def map_preferences(sender, user, request, **kwargs):
    '''
    Signal based permission assignment.
    Adds users into groups based on the old Users table.
    '''

    # This is a special user internally
    if user.username == 'System':
        return

    p, n = Preferences.objects.get_or_create(user=user)

    # Add existing privileged users to the reviewers group
    # and give them admin/superuser access if required
    try:
        u = User.objects.get(username=user.username)
    except User.DoesNotExist:
        pass
    else:
        # Save the user preferences
        if n:
            p.next_on_review = (u.next_on_review == 1)

    p.save()
