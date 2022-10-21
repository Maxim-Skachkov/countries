"""countries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from country.views import *

urlpatterns = [
    path('', SiteHomepage.as_view(), name='homepage'),
    path('continent/<slug:continent_sluggy>/', Continent.as_view(), name='continent'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('country/<slug:cntry>', ShowCountry.as_view(), name='country'),
    path('new_article', NewArticle.as_view(), name='new_article')
]


