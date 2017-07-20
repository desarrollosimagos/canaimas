from django.db import models
from ..tipo_educacion.models import TipoEducacion

class Grados(models.Model):
    tipo  = models.ForeignKey(TipoEducacion, on_delete=models.CASCADE, related_name='tipo_grado', null=True) ##*** campo relacion con otro modelo
    grado = models.CharField(max_length=60,)
