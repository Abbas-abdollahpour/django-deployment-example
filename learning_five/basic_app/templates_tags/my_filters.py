from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This is our Filter
    """
    return value.replace(arg,"")
