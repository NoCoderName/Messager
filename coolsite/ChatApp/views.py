import django.core.asgi
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.db.models import Count

from .models import Chat
from .forms import MessageForm
from ProfileApp.utils import DataMixin


class DialogsView(DataMixin, View):
    template_name = 'ChatApp/dialog.html'
    
    def get(self, request):
        context = self.get_user_context(title='Профиль')
        context['user_profile'] = request.user
        context['chats'] = Chat.objects.filter(members__in=[self.request.user.id])

        return render(request, self.template_name, context)
    

class MessagesView(DataMixin, View):
    template_name = 'ChatApp/messages.html'

    def get(self, request, chat_id):
        try:
            chat = Chat.objects.get(id=chat_id)
            if request.user in chat.members.all():
                chat.message_set.filter(is_readed=False).exclude(author=request.user).update(is_readed=True)
            else:
                chat = None
        except Chat.DoesNotExist:
            chat = None

        context = self.get_user_context(title=request.user)
        context['chat'] = chat
        context['form'] = MessageForm()

        return render(request, self.template_name, context)
 
    def post(self, request, chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id = chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('chat_app:messages', kwargs={'chat_id': chat_id}))
    

class CreateDialogView(View):
    def get(self, request, user_id):
        chats = Chat.objects.filter(members__in=[request.user.id, user_id], type=Chat.DIALOG).annotate(c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        return redirect(reverse('chat_app:messages', kwargs={'chat_id': chat.id}))