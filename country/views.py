from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from country.models import *
menu = [
    {'name': "Главная страница", 'link': "homepage"},
    {'name': "О сайте", 'link': "about"},
    {'name': "Контакты", 'link': "contacts"},
]


def index(request):
    continents = Contitent.objects.all()
    context = {"title": "Страны всего мира",
               'menu': menu,
               "continents": continents,
               }
    return render(request, "country/index.html", context)


def about(request):
    context = {"title": "О сайте",
               'menu': menu}
    return render(request, "country/about.html", context)


def contacts(request):
    context = {"title": "Наши контакты",
               'menu': menu}
    return render(request, "country/contacts.html", context)


def continent(request, continent_sluggy):
    continents = Contitent.objects.all()
    current_continent = Contitent.objects.get(contitent_slug=continent_sluggy)
    countries_list = Country.objects.filter(country_continent_id=current_continent.pk)
    context = {
                "title": current_continent.contitent_name,
                'menu': menu,
                "continents": continents,
                "countries_list": countries_list,
               }
    return render(request, "country/conti.html", context)