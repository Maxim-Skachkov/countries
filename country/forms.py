from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddCountry(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country_continent'].empty_label = 'Укажите континент'

    class Meta:
        model = Country
        fields = '__all__'
        widgets = {
            'country_description': forms.Textarea(attrs={'cols': 80, 'rows': 8})
        }

    def clean_country_name(self):
        country_name = self.cleaned_data['country_name']
        if len(country_name) > 20:
            raise ValidationError('слишком длинное название')
        return country_name


class AddContinent(forms.Form):
    contitent_name = forms.CharField(max_length=50, label='Континент')
    contitent_slug = forms.CharField(max_length=50, label='slug')