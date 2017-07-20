from .models import Municipio
from .serializers import MunicipioSerializer
from rest_framework import serializers, viewsets


class MunicipioViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los `serializers`
    """
    serializer_class = MunicipioSerializer
    queryset = Municipio.objects.all()
