from django.db import models


class Estado(models.Model):
    """ Clase que define todo lo referente a los `Estados`:
    Registrar, Modificar, Eliminar y Consultar

    :param IntegerField cod_estado: campo donde se coloca el codigo del Estado.
    :param CharField estado: campo donde ingresas el nombre del Estado.
    """

    cod_estado = models.IntegerField(unique=True, null=True)
    estado = models.CharField(max_length=50, unique=True)

    class Meta:
        """ Ordena los registros en base a el campo cod_estado."""
        ordering = ('cod_estado',)  # Ordenado por

    def __unicode__(self):
        return self.estado

    def get_absolute_url(self):
        return ('listar_estado', [self.id, ])
