from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .forms import *

from ProfileApp.utils import DataMixin


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'LoginApp/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_name_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')

        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'LoginApp/login.html'

    def get_context_data(self, *, object_name_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')

        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('profile_user:profile', kwargs={'prof_slug': self.request.user.slug})
    

def logout_user(request):
    logout(request)

    return redirect('login')
