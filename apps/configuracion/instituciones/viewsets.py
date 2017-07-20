from .models import Institucion
from .serializers import InstitucionSerializer
from rest_framework import serializers, viewsets


class InstitucionViewSet(viewsets.ModelViewSet):
    """
        Clase que construye la vista de los `serializers`
    """
    serializer_class = InstitucionSerializer
    queryset = Institucion.objects.all()
