#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Estado


class EstadoForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario `Estado`."""

    class Meta:
        """
        Llamado del modelo
        """
        model = Estado
