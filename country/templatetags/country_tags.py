from django import template
from country.models import *

register = template.Library()

@register.simple_tag()
def get_menu():
    menu_list = [
    {'name': "Главная страница", 'link': 'homepage'},
    {'name': "Добавить статью", 'link': 'new_article'},
    {'name': "О сайте", 'link': "about"},
    {'name': "Контакты", 'link': "contacts"},
]
    return menu_list


@register.simple_tag()
def get_continents():
    continents = Contitent.objects.all().order_by('-contitent_name')
    return continents


@register.simple_tag()
def get_countries():
    cntries = Country.objects.all().order_by('country_name')
    return cntries


@register.inclusion_tag("country/inclusion_tags/left_menu.html")
def show_continents(cont_id=0):
    conts = Contitent.objects.all().order_by('-contitent_slug')
    return {"conties": conts, "cont_id": cont_id}

