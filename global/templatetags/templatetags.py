from django import template
from blog.models import NavLink

register = template.Library()


def header():
    navlinks = NavLink.objects.all()
    return {'navlinks':navlinks}

register.inclusion_tag('header.html')(header)
