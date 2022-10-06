from django.contrib import admin

# Register your models here.
from country.models import Country, Comment, Contitent

admin.site.register(Country)
admin.site.register(Contitent)
admin.site.register(Comment)
