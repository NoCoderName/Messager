from django import template


register = template.Library()

@register.simple_tag
def get_companion(user, chat):
    for u in chat.members.all():
        if u != user:
            return u
    return None