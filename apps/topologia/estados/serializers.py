from rest_framework import serializers
from .models import Estado


class EstadoSerializer(serializers.ModelSerializer):
    """
        Clase donde llamamos al modelo `Estado` y serializamos los campos
    """
    class Meta:
        model = Estado
        fields = ('id', 'cod_estado', 'estado',)
