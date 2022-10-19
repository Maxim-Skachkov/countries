from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from country.forms import *
# Create your views here.
from country.models import *


def index(request):
    context = {"title": "Страны всего мира",
               "cont_id": 0,
               }
    return render(request, "country/index.html", context)


def about(request):
    context = {"title": "О сайте",
               }
    return render(request, "country/about.html", context)


def contacts(request):
    context = {"title": "Наши контакты",
               }
    return render(request, "country/contacts.html", context)


def continent(request, continent_sluggy):
    current_continent = get_object_or_404(Contitent, contitent_slug=continent_sluggy)
    countries_list = Country.objects.filter(country_continent_id=current_continent.pk)
    context = {
                "title": current_continent.contitent_name,
                "countries_list": countries_list,
                "continent_slug": current_continent.contitent_slug,
                "cont_id": current_continent.pk,
               }
    return render(request, "country/conti.html", context)


def curr_country(request, cntry):
    current_country = get_object_or_404(Country, country_slug=cntry)
    context = {
        "title": current_country.country_name,
        "current_country": current_country,
    }
    return render(request, "country/current_country.html", context)


def new_article(request):
    if request.method == "POST":
        form = AddCountry(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AddCountry()
    context = {"title": "Добавление статьи",
               "form": form,
               }
    return render(request, "country/new_article.html", context)