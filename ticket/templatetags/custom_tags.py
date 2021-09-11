from django import template
import math

register = template.Library()

@register.simple_tag
def add(a, b):
    return math.ceil(a+b)

