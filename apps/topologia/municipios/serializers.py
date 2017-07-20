from rest_framework import serializers
from .models import Municipio


class MunicipioSerializer(serializers.ModelSerializer):
    """
        Clase donde llamamos al modelo `Municipio` y serializamos los campos
    """
    class Meta:
        model = Municipio
        fields = ('id', 'estado', 'municipio')
