from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse("Главная страница сайта")

def country(request):
    return HttpResponse("Страница о конкретной стране")

def about(request):
    return HttpResponse("Страница о сайте")
