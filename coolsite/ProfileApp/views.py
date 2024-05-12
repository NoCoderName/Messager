from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import DetailView, View

from .utils import DataMixin


class ProfileView(DataMixin, DetailView):
    model = get_user_model()
    template_name = 'ProfileApp/profile.html'
    context_object_name = 'prof'
    slug_url_kwarg = 'prof_slug'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Профиль')
        return dict(list(context.items()) + list(c_def.items()))
    

# Заглушка
class Plug(DataMixin, View):
    template_name = 'ProfileApp/home.html'
    context_object_name = 'prof'
    
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
    
    def get_context_data(self, *, object_list=None, **kwargs):
        c_def = self.get_user_context(title='Стена')
        return c_def
    
