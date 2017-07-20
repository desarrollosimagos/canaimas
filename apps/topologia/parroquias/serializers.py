from rest_framework import serializers
from .models import Parroquia


class ParroquiaSerializer(serializers.ModelSerializer):
    """
        Clase donde llamamos al modelo `Parroquia` y serializamos los campos
    """
    class Meta:
        model = Parroquia
        fields = ('id', 'estado', 'municipio', 'parroquia',)
