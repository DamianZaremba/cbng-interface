import logging
from random import randint

from cbng_interface.models import Preferences
from cbng_report.models import Report

logger = logging.getLogger(__name__)


def get_next_report(user):
    '''
    Generate the next report ID for a user
    :param user: User to generate a report ID for
    :return: (Integer) id or None
    '''
    try:
        p = Preferences.objects.get(user=user)
    except Preferences.DoesNotExist, e:
        logger.exception(
            'Failed to get the preferences for user %s' % user.id, e)
        p = None

    if p is None or p.next_on_review:
        try:
            reports = Report.objects.filter(
                status=0).order_by('-timestamp')[0:100]
            if len(reports) > 0:
                return reports[randint(0, len(reports) - 1)].vandalism__id
        except Exception, e:
            logger.exception(
                'Failed to get the next report for user %s' % user.id, e)
    return None
