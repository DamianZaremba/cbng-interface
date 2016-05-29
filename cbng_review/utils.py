from random import randint

from cbng_review.models import Edit, Classification
from django.db.models import Q


def send_signup_email(email, username, comments):
    data = ('Hello,\r\n',
            'New user:\r\n',
            'Email: %(email)s\r\n',
            'Wikipedia: %(username)s\r\n',
            'Comments: %(comments)s\r\n\r\n',
            '<http://enwp.org/Special:Contributions/%(username)s>\r\n',
            'Thanks,\r\n',
            'ClueBot NG Review Interface.') % {
        'email': email,
        'username': username,
        'comments': comments
    }

    print(data)


def get_next_to_review(user):
    '''
    Generate the next review ID for a user
    :param user: User to generate a report ID for
    :return: (Integer) id or None
    '''
    edits = Edit.objects \
                .exclude(id__in=Classification.objects.filter(user=user)
                         .values_list('edit__id', flat=True)
                         .distinct())\
                .filter(~Q(status=2)) \
                .order_by('group__weight')[0:100]

    if len(edits) > 0:
        return edits[randint(0, len(edits) - 1)]

    return None
