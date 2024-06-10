from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    message = forms.CharField(label='Введите текст', widget=forms.TextInput(attrs={'class': 'message-input'}))
    
    class Meta:
        model = Message
        fields = ['message']