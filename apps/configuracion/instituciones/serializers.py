from rest_framework import serializers
from .models import Institucion


class InstitucionSerializer(serializers.ModelSerializer):
    """
        Clase donde llamamos al modelo `Institucion` y serializamos los campos
    """
    class Meta:
        model = Institucion
        fields = ('id', 'nom_institucion', 'siglas', 'telefono', 'correo',
                  'estado', 'municipio', 'parroquia', 'direccion',
                  'user_create', 'user_update', 'fecha_create', 'fecha_update')