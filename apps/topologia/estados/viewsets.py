from .models import Estado
from .serializers import EstadoSerializer
from rest_framework import serializers, viewsets


class EstadoViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los `serializers`
    """
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()
