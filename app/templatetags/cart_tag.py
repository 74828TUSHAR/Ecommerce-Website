# your_app/templatetags/cart_tag.py

from django import template

register = template.Library()

@register.simple_tag
def example_tag():
    return "This is an example tag"
