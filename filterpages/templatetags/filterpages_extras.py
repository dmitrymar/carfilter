from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def carpic(value, arg):
    return 'http://media.ed.edmunds-media.com/' + value + str(arg) + ".jpg"
