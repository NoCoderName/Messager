from django import template
from django.contrib.auth import get_user_model


register = template.Library()

@register.simple_tag(name='exclude_signed')
def exclude_signed(log_username, subscribe_user):
    log_user = get_user_model().objects.get(username=log_username)
    
    if log_user.friends.filter(username=subscribe_user).exists():
        return False
    else:
        return True