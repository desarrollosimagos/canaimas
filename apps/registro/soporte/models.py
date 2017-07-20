from django.db import models
from django.contrib.auth.models import User
from apps.registro.solicitud.models import Registros
from apps.configuracion.modelos.models import Modelos
from apps.configuracion.instituciones.models import Institucion


ESTATUS = (
    ('0', "Seleccione"),
    ('2', 'Remitida'),
    ('3', 'Reparada'),
)


class Soporte(models.Model):
    """ Clase que define todo lo referente a los `Estados`:
    Registrar, Modificar, Eliminar y Consultar

    :param IntegerField cod_estado: campo donde se coloca el codigo del Estado.
    :param CharField estado: campo donde ingresas el nombre del Estado.
    """
    cod_solicitud = models.ForeignKey(Registros)
    serial = models.CharField(max_length=30)
    modelo = models.ForeignKey(Modelos)
    institucion = models.ForeignKey(Institucion, null=True, blank=True,)

    problema = models.TextField(max_length=300)
    descripcion = models.TextField(max_length=300)
    hardware = models.BooleanField(default=False)
    software = models.BooleanField(default=False)
    status = models.CharField(choices=ESTATUS, default=0, max_length=1)

    #  Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    fecha_create = models.DateTimeField(auto_now_add=True,)
    fecha_update = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    class Meta:
        """ Ordena los registros en base a el campo cod_estado."""
        ordering = ('cod_solicitud',)  # Ordenado por

    def __unicode__(self):
        return self.cod_solicitud

    def get_absolute_url(self):
        return ('listar_soportes', [self.id, ])
