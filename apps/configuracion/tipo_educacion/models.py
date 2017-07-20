from django.db import models

class TipoEducacion(models.Model):
    tipo = models.CharField(max_length=60,)

