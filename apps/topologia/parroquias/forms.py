#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Parroquia


class ParroquiaForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Parroquia`."""
    class Meta:
        model = Parroquia
