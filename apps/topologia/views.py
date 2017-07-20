from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import connection, transaction


class Topologia(TemplateView):
    """ Vista basada en clase: (`Plantilla`)
    :param template_name: ruta al archivo que contiene la plantilla principal de la aplicacion
    """
    template_name = 'topologia/topologia.html'
