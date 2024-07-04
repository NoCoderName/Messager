menu = [
    {'title': 'Новости', 'url_name': 'profile_user:home'},
    {'title': 'Друзья', 'url_name': 'profile_user:friends'},
    {'title': 'Сообщения', 'url_name': 'chat_app:dialogs'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context