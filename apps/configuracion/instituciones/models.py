from django.db import models
from apps.topologia.estados.models import Estado
from django.contrib.auth.models import User


class Institucion(models.Model):
    """ Clase que define todo lo referente a los `Estados`:
    Registrar, Modificar, Eliminar y Consultar

    :param IntegerField cod_estado: campo donde se coloca el codigo del Estado.
    :param CharField estado: campo donde ingresas el nombre del Estado.
    """
    nom_institucion = models.CharField(max_length=100, unique=True)
    siglas = models.CharField(max_length=15)
    telefono = models.CharField(max_length=11)
    correo = models.CharField(max_length=100, null=True,)
    estado = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL, related_name='estado_institucion', null=True, blank=True)
    municipio = models.IntegerField(null=True, blank=True)
    parroquia = models.IntegerField(null=True, blank=True)
    direccion = models.CharField(max_length=200)
    institucion_activa = models.BooleanField(default=False)

    #  Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True,)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """ Ordena los registros en base a el campo cod_estado."""
        ordering = ('nom_institucion',)  # Ordenado por

    def __unicode__(self):
        return self.nom_institucion

    def get_absolute_url(self):
        return ('listar_institucion', [self.id, ])
