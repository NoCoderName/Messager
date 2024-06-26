from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, View, ListView

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
    

class Friends(DataMixin, ListView):
    model = get_user_model()
    template_name = 'ProfileApp/friends.html'
    context_object_name = 'friends'             # нужно будет поменять на "подписки"

    def get_queryset(self):
        username = self.request.GET.get('username')

        if username:
            return get_user_model().objects.filter(username__iregex=username)
        else:  
            return get_user_model().objects.get(username=self.request.user.username).friends.all() #

    def get_context_data(self,  *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Подписки')
        
        return dict(list(context.items()) + list(c_def.items()))


# Прототип. Нужно будет по другому реализовать
class AddFriends(View):
    slug_url_kwarg = 'slug'

    def get(self, request, *args, **kwargs):
        friend = get_user_model().objects.get(slug=kwargs.get('slug'))
        request.user.friends.add(friend)

        return redirect(reverse('profile_user:profile', kwargs={'prof_slug': kwargs.get('slug')}))
