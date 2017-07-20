from django.contrib.auth.models import User
from django.db import models
from apps.configuracion.instituciones.models import Institucion


class UsuarioInstitucion(models.Model):

    grupo_usuario = models.IntegerField(null=True, blank=True)
    usuario = models.OneToOneField(User, null=True)
    institucion = models.ForeignKey(Institucion, null=True)
    def __unicode__(self):
        return self.usuario