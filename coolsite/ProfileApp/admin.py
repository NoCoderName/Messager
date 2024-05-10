from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(ProfileUser)
class ProfileAdmin(UserAdmin):
    model = ProfileUser
    
    readonly_fields = ["slug"]
    list_display = ('id', 'get_html_image', 'username', 'slug', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined')
    list_display_links = ('id', 'username', 'slug')
    
    #то что отражается в админ панели при редактирования модели 
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': ('photo', 'slug', 'status', 'birthday', 'friends')
            }
        )
    )

    def get_html_image(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_image.short_description = 'Фото пользователя'