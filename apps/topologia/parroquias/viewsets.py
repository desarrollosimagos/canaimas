from .models import Parroquia
from .serializers import ParroquiaSerializer
from rest_framework import serializers, viewsets


class ParroquiaViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los `serializers`
    """
    serializer_class = ParroquiaSerializer
    queryset = Parroquia.objects.all()
