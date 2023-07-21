from django import template

from blog.models import Like

register = template.Library()


@register.filter
def check_like(obj, value):
    return Like.objects.filter(
        article=obj,
        user=value

    )
