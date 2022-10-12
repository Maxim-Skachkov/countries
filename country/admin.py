from django.contrib import admin

# Register your models here.
from .models import *


class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', 'country_continent', 'country_slug', 'time_updated', 'is_published')
    list_display_links = ('country_name',)
    search_fields = ('country_name',)
    list_editable = ('is_published',)


class ContinentAdmin(admin.ModelAdmin):
    list_display = ('contitent_name', 'contitent_slug')


admin.site.register(Country, CountryAdmin)
admin.site.register(Contitent, ContinentAdmin)
admin.site.register(Comment)
