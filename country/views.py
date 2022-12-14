from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from country import utils
from country.forms import *
# Create your views here.
from country.models import *
from country.utils import DataMixin


# def index(request):
#     context = {"title": "Страны всего мира",
#                "cont_id": 0,
#                }
#     return render(request, "country/index.html", context)

class SiteHomepage(DataMixin, ListView):
    model = Country
    template_name = 'country/index.html'
    context_object_name = 'cntries'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Страны всего мира")
        return context | c_def

    def get_queryset(self):
        return Country.objects.filter(is_published=True)


def about(request):
    context = {"title": "О сайте",
               'menu': utils.menu_list
               }
    return render(request, "country/about.html", context)


def contacts(request):
    context = {"title": "Наши контакты",
               'menu': utils.menu_list
               }
    return render(request, "country/contacts.html", context)


# def continent(request, continent_sluggy):
#     current_continent = get_object_or_404(Contitent, contitent_slug=continent_sluggy)
#     countries_list = Country.objects.filter(country_continent_id=current_continent.pk)
#     context = {
#                 "title": current_continent.contitent_name,
#                 "countries_list": countries_list,
#                 "continent_slug": current_continent.contitent_slug,
#                 "cont_id": current_continent.pk,
#                }
#     return render(request, "country/conti.html", context)
class Continent(DataMixin, ListView):
    model = Country
    template_name = 'country/conti.html'
    context_object_name = 'countries_list'

    def get_current_continent(self):
        current_continent = get_object_or_404(Contitent, contitent_slug=self.kwargs['continent_sluggy'])
        return current_continent

    def get_queryset(self):
        return Country.objects.filter(
            is_published=True, country_continent__contitent_slug=self.kwargs['continent_sluggy'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=self.get_current_continent().contitent_name,
            cont_id=self.get_current_continent().pk
            )
        return context | c_def


# def curr_country(request, cntry):
#     current_country = get_object_or_404(Country, country_slug=cntry)
#     context = {
#         "title": current_country.country_name,
#         "current_country": current_country,
#     }
#     return render(request, "country/current_country.html", context)
class ShowCountry(DataMixin, DetailView):
    model = Country
    template_name = 'country/current_country.html'
    slug_url_kwarg = 'cntry'
    slug_field = 'country_slug'
    context_object_name = 'current_country'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=context['current_country'],
            cont_id=Country.objects.get(country_slug=self.kwargs['cntry']).country_continent.pk
        )
        return context | c_def


# def new_article(request):  # Добавление статьи
#     if request.method == "POST":
#         form = AddCountry(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')
#     else:
#         form = AddCountry()
#     context = {"title": "Добавление статьи",
#                "form": form,
#                }
#     return render(request, "country/new_article.html", context)
class NewArticle(DataMixin, CreateView):
    form_class = AddCountry
    template_name = 'country/new_article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление статьи')
        return context | c_def


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'country/register.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return context | c_def

