# custom_filters.py
from django import template

register = template.Library()


@register.filter
def get_count(counts, category):
    return counts.get(category, 0)
