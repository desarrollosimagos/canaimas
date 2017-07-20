from django.db import models
from apps.topologia.estados.models import Estado


class Municipio(models.Model):
    """ Clase que define todo lo referente a los `Municipios`:
    Registrar, Modificar, Eliminar y Consultar

    :param ForeignKey estado: campo que llama al modelo Estado.
    :param IntegerField cod_municipio: campo donde se coloca el codigo del Municipio.
    :param CharField municipio: campo donde ingresas el nombre del Municipio
    """
    estado = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL,
                               related_name='estado_municipio', null=True)
    cod_municipio = models.IntegerField(null=True)
    municipio = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return self.municipio

    class Meta:
        """
        :param unique_together: atributo que valida que el nombre y el codigo de municipio sea unico por estado
        :param ordering: Ordena los registros en base a el campo estado y sus municicipios
        """
        unique_together = ("estado", "cod_municipio", "municipio")
        ordering = ('estado', 'cod_municipio', 'municipio')

    def get_absolute_url(self):
        return ('listar_municipio', [self.id, ])
