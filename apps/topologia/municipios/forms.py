#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Municipio


class MunicipioForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Municipio`."""
    class Meta:
        """
        Llamado del modelo
        """
        model = Municipio
