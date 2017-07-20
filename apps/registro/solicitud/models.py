from django.db import models
from django.contrib.auth.models import User
from apps.topologia.estados.models import Estado
from apps.configuracion.tipo_educacion.models import TipoEducacion
from apps.configuracion.grados.models import Grados
from apps.configuracion.modelos.models import Modelos
from apps.configuracion.instituciones.models import Institucion


SEXO = (
    ('0', "Seleccione"),
    ('1', "Femenino"),
    ('2', "Masculino"),
)

STATUS = (
    ('1', 'Atendiendo'),
    ('2', 'Remitida'),
    ('3', 'Reparada'),
    ('4', 'Entregada'),
    ('5', 'Devuelta'),
)


class Registros(models.Model):
    
    codigo       = models.CharField(max_length=50,)
    # usuario      = models.CharField(max_length=50,)
    fecha_s      = models.DateField(auto_now_add=False, auto_now=False)
    fecha_e      = models.DateField(auto_now_add=False, auto_now=False)
    modelo       = models.ForeignKey(Modelos, on_delete=models.CASCADE, related_name='computador_modelo', null=True)
    serial       = models.CharField(max_length=100,)
    status = models.CharField(max_length=1, null=True, blank=True, choices=STATUS,)
    # componente   = models.CharField(max_length=100, null=True, blank=True)
    descripcion  = models.TextField(null=True, blank=True)
    nombre    = models.CharField(max_length=50,)
    apellido  = models.CharField(max_length=50,)
    sexo      = models.CharField(choices=SEXO, default=0, max_length=1)
    edad      = models.IntegerField()
    tipo      = models.ForeignKey(TipoEducacion, on_delete=models.CASCADE, related_name='registro_tipo', null=True)
    grado     = models.ForeignKey(Grados, on_delete=models.CASCADE, related_name='registro_grado', null=True)
    escuela   = models.CharField(max_length=50,)
    estado    = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL, related_name='institucion_estado', null=True)
    parroquia = models.IntegerField()
    municipio = models.IntegerField()
    direcc_es = models.TextField(null=True, blank=True)
    cedula    = models.IntegerField()
    nombre2    = models.CharField(max_length=50,)
    apellido2  = models.CharField(max_length=50,)
    telefono1 = models.CharField(max_length=50,)
    telefono2 = models.CharField(max_length=50, null=True, blank=True)
    email     = models.CharField(max_length=100,)
    estado2    = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL, related_name='representante_estado', null=True)
    municipio2 = models.IntegerField()
    parroquia2 = models.IntegerField()
    direcc_re = models.TextField(null=True, blank=True)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='registro_institucion', null=True)
    portatil = models.BooleanField(default=False)
    contrato = models.BooleanField(default=False)
    bateria = models.BooleanField(default=False)
    caja = models.BooleanField(default=False)
    cargador = models.BooleanField(default=False)
    reparacion = models.TextField(null=True, blank=True)

    # Auditoria
    user_create = models.ForeignKey(User, null=True, blank=True, related_name='+')
    user_update = models.ForeignKey(User, null=True, blank=True, related_name='+')
    
    class Meta:
        """ Ordena los registros en base a el campo codigo."""
        ordering = ('codigo',)
