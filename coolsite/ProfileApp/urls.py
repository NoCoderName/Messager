from django.urls import path

from .views import *

app_name = 'profile_user'

urlpatterns = [
    path('', Plug.as_view(), name='home'),
    path('profile/<slug:prof_slug>/', ProfileView.as_view(), name='profile'),
    path('friends/', Friends.as_view(), name='friends'),
    path('add_friends/<slug:slug>/', AddFriends.as_view(), name='add_friends'),
]