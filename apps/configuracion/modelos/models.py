from django.db import models

class Modelos(models.Model):
    nombre = models.CharField(max_length=60,)
