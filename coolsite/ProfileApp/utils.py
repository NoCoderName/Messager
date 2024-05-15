menu = [
    {'title': 'Типо главная страница', 'url_name': 'profile_user:home'},
    {'title': 'Друзья', 'url_name': 'profile_user:friends'},
    # {'title': 'Друзья', 'url_name': '#'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu

        if 'cat_selected' not in context:
            context['cat_selected'] = 0

        return context