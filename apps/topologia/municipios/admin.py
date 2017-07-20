from django.contrib import admin
from .models import Municipio


class MunicipioAdmin(admin.ModelAdmin):
    """
    :param list_display: Muesta el str de los campos en la vista lista
    :param list_filter: Crea un campo para filtrar y le decimos en que campo
    :param search_fields: Crea un campo para busqueda directa especificando cuales campos
    """
    list_display = ('estado', 'municipio')
    list_filter = ['municipio']
    search_fields = ['estado', 'municipio']

admin.site.register(Municipio, MunicipioAdmin)
