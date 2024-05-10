from django.db import models
from django.contrib.auth.models import AbstractUser 
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from django.contrib.auth import get_user_model


class ProfileUser(AbstractUser):
    photo = models.ImageField(upload_to='photo_user/%Y/%m/%d/', blank=True, null=True, verbose_name='Фото пользователя')
    slug = AutoSlugField(max_length=100, unique=True, populate_from=('username',), verbose_name="URL")
    status = models.BooleanField(default=True, verbose_name='Статус') # Online/Ofline
    birthday = models.DateTimeField(blank=True, null=True, verbose_name='День рождения')
    friends = models.ManyToManyField(get_user_model(), blank=True, related_name='friends+', verbose_name='Друзья')

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='%(app_label)s_%(class)s_groups+',
        blank=True,
        verbose_name='Группы',
        help_text='Группы, к которым принадлежит этот пользователь.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='%(app_label)s_%(class)s_user_permissions+',
        blank=True,
        verbose_name='Права',
        help_text='Специальные права для данного пользователя.',
    )

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('profile', kwargs={'prof_slug': self.slug})
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
        ordering = ['id',]