from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
 
class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICES = (
        (DIALOG, _('Dialog')),
        (CHAT, _('Chat'))
    )
 
    type = models.CharField(
        _('Тип'),
        max_length=1,
        choices=CHAT_TYPE_CHOICES,
        default=DIALOG
    )
    members = models.ManyToManyField(get_user_model(), verbose_name=_("Участник"))
 
    def get_absolute_url(self):
        return reverse('chat_app:messages', kwargs={'chat_id': self.pk})
 
 
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.PROTECT, verbose_name=_("Чат"))
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name=_("Пользователь"))
    message = models.TextField(_("Сообщение"))
    pub_date = models.DateTimeField(_('Дата сообщения'), default=timezone.now)
    is_readed = models.BooleanField(_('Прочитано'), default=False)
 
    class Meta:
        ordering=['pub_date']
 
    def __str__(self):
        return self.message