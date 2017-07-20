from django.contrib import admin
from .models import Institucion


class InstitucionAdmin(admin.ModelAdmin):
    """
    :param list_display: Muesta el str de los campos en la vista lista
    :param search_fields: Crea un campo para busqueda directa
    """
    # list_display = ('estado',)
    # search_fields = ['estado']

admin.site.register(Institucion, InstitucionAdmin)
