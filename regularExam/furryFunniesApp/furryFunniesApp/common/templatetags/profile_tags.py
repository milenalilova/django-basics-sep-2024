from django import template

from furryFunniesApp.urils import get_profile

register = template.Library()


@register.simple_tag()
def find_profile():
    return get_profile()
