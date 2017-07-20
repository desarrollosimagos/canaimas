#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import Institucion


class InstitucionForm(forms.ModelForm):
    """ Clase de donde se define la estructura del formulario 'Institucion'."""

    class Meta:
        """
        Llamado del modelo
        """
        model = Institucion
