from django import template

register = template.Library()

@register.filter(name='custom_tags')
def custom_tags(value):
        return value.split()
