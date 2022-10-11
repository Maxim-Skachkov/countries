from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Contitent(models.Model):
    contitent_name = models.CharField(max_length=50)
    contitent_slug = models.CharField(max_length=50)

    def __str__(self):
        return self.contitent_name

    def get_absolute_url(self):
        return reverse('continent', kwargs={'continent_sluggy': self.contitent_slug})

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_population = models.PositiveIntegerField()
    country_description = models.TextField()
    country_capital = models.CharField(max_length=100)
    country_continent = models.ForeignKey(Contitent, default='-', on_delete=models.SET_DEFAULT)
    country_flag = models.ImageField(upload_to="photos/flags/%Y/%m/%d/")
    country_photo = models.ImageField(upload_to="photos/borders/%Y/%m/%d/")
    country_slug = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.country_name

    def get_absolute_url(self):
        return reverse('country', kwargs={'cntry': self.country_slug})


class Comment(models.Model):
    comment_text = models.TextField()
    user = models.ForeignKey(User, default='Anon', on_delete=models.SET_DEFAULT)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
