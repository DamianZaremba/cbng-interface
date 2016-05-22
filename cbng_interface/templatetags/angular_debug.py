from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag()
def angular_debug():
    '''Return the debug status as a lowercase string'''
    if settings.DEBUG:
        return 'true'
    return 'false'
