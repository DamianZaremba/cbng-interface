'''
Function to return ng formatted variables ({{something}})
'''
from django import template

register = template.Library()


@register.simple_tag
def ngvar(var_name):
    return '{{%s}}' % var_name
