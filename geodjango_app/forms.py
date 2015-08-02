

__author__ = 'Matt'


from django import forms
from django.forms import ModelForm
from linki.models import Advert


class AdvertForm(ModelForm):
    class Meta:
        model = Advert