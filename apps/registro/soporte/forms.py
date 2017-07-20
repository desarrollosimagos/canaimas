#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Soporte


class SoporteForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario 'Soporte'."""

    class Meta:
        """
        Llamado del modelo
        """
        model = Soporte
