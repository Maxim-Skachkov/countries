from django.db.models import Count

from .models import *
menu_list = [
    {'name': "Главная страница", 'link': 'homepage'},
    {'name': "Добавить статью", 'link': 'new_article'},
    {'name': "О сайте", 'link': "about"},
    {'name': "Контакты", 'link': "contacts"},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        conties = Contitent.objects.all().annotate(Count('country'))
        context = kwargs
        context['conties'] = conties
        menu = menu_list.copy()
        if not self.request.user.is_authenticated:
            menu.pop(1)
        context['menu'] = menu
        if 'cont_id' not in context:
            context['cont_id'] = 0
        return context
