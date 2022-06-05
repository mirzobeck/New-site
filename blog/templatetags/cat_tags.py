from django import template
from blog.models import category
from datetime import datetime

register = template.Library()

@register.simple_tag
def get_cat():
    return category.objects.all()



