#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Modelo Parroquia del país'''
from django.db import models
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio


class Parroquia(models.Model):
    """ Clase que define todo lo referente a las `Parroquias`:
    Registrar, Modificar, Eliminar y Consultar

    :param ForeignKey estado: campo que llama al modelo Estado.
    :param IntegerField municipio: campo que a traves de ajax carga los municipios asociados al estado.
    :param IntegerField cod_parroquia: campo donde se coloca el codigo de la Parroquia.
    :param CharField parroquia: campo donde ingresas el nombre de la Parroquia
    """
    parroquia = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, to_field='cod_estado', on_delete=models.SET_NULL, related_name='estado_parroquia', null=True)
    cod_parroquia = models.IntegerField(null=True)
    municipio = models.IntegerField(null=True)

    def __unicode__(self):
        """ Representacion en cadena de la clase Parroquia. """
        return self.parroquia

    class Meta:
        """
        :param unique_together: atributo que valida que la parroquia sea unica por municipio y a su ves al estado
        :param ordering: Ordena los registros en base a el campo estado, municicipios y parroquia
        """
        unique_together = ("estado", "municipio", "parroquia")  # Municipio unico por Estado seleccionado
        ordering = ('estado', 'municipio', 'cod_parroquia', 'parroquia')  # Ordenado por

    def get_absolute_url(self):
        """ La Url de vista principal de administracion de Parroquia. """
        return ('listar_parroquia', [self.id, ])
