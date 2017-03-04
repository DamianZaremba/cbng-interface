import logging

from django.db import connections

from cbng_interface.models import Preferences
from django.contrib.auth.models import Group
from tastypie.models import ApiKey
from django.conf import settings

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
    admin, superadmin = 0, 0
    email = None
    with connections['legacy'].cursor() as c:
        if user.username in settings.WIKIPEDIA_REPORT_USER_MAPPINGS.keys():
            legacy_username = settings.WIKIPEDIA_REPORT_USER_MAPPINGS[
                user.username]
        else:
            legacy_username = user.username

        c.execute(
            'select admin, superadmin, email from users where username = %s', (legacy_username,))
        r = c.fetchone()
        if r:
            (admin, superadmin, email) = r

    if admin == 1:
        try:
            user.groups.add(Group.objects.get(name='reviewers'))
        except Group.DoesNotExist, e:
            logger.error('Could not get reviewers group', e)

    if superadmin == 1:
        try:
            user.groups.add(Group.objects.get(name='admins'))
        except Group.DoesNotExist, e:
            logger.error('Could not get admins group', e)

    if email:
        user.email = email

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
    next_on_review = False
    with connections['legacy'].cursor() as c:
        if user.username in settings.WIKIPEDIA_REPORT_USER_MAPPINGS.keys():
            legacy_username = settings.WIKIPEDIA_REPORT_USER_MAPPINGS[
                user.username]
        else:
            legacy_username = user.username

        c.execute(
            'select next_on_review from users where username = %s', (legacy_username,))
        r = c.fetchone()
        if r:
            next_on_review = (r[0] == 1)

    # Save the user preferences
    if n:
        p.next_on_review = next_on_review

    p.save()


def map_reports(sender, user, request, **kwargs):
    '''
    Signal based report/comment assignment.
    Re-assigns userids based on the old users table.
    This makes sure we display the correct username in the frontend ;)
    '''

    # This is a special user internally
    if user.username == 'System':
        return

    # Update all reports
    with connections['legacy'].cursor() as c:
        if user.username in settings.WIKIPEDIA_REPORT_USER_MAPPINGS.keys():
            legacy_username = settings.WIKIPEDIA_REPORT_USER_MAPPINGS[
                user.username]
        else:
            legacy_username = user.username

        c.execute(
            'select id from users where username = %s', (legacy_username,))
        r = c.fetchone()
        if r:
            legacy_id = r[0]
            c.execute(
                'update `reports` set `userid` = %d, `user` = NULL where `userid` = %d', (user.id, legacy_id))
            c.execute(
                'update `comments` set `userid` = %d, `user` = NULL where `userid` = %d', (user.id, legacy_id))
