from django.urls import path

from .views import *

app_name = 'profile_user'

urlpatterns = [
    path('', Plug.as_view(), name='home'),
    path('profile/<slug:prof_slug>/', ProfileView.as_view(), name='profile'),
]