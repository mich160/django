from django import template
from mainapp import utils

register = template.Library()

@register.filter
def isTeacher(request):
    return utils.isTeacher(request)