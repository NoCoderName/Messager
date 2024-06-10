from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'chat_app'

urlpatterns = [
    path('dialogs/', DialogsView.as_view(), name='dialogs'),
    path('dialogs/create/<int:user_id>/', CreateDialogView.as_view(), name='create_dialog'),
    path('dialogs/<int:chat_id>/', MessagesView.as_view(), name='messages'),
]