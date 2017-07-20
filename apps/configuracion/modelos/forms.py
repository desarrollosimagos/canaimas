#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Modelos


class ModelosForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Modelos`."""

    class Meta:
        """
        Llamado del modelo
        """
        model = Modelos
