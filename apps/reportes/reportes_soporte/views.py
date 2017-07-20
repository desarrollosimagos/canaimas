#encoding:utf-8
from django.views.generic import CreateView, TemplateView, DetailView, ListView, View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core import serializers
from apps.topologia.estados.models import Estado
from django.db.models import Count
import json
import sys
from django.http import HttpResponse
from django.template import RequestContext
import class_pdf
from django.db import connection, transaction
import time
from apps.configuracion.instituciones.models import Institucion
from apps.reportes.reportes_soporte.formato_reportes import reporte_soporte_general


class ListarGrafica(TemplateView):

    #model = Votacion
    template_name = 'reportes/reporte_soporte.html'

    def get_context_data(self, **kwargs):
        context = super(ListarGrafica, self).get_context_data(**kwargs)
        es_administrador = self.request.user.groups.all().filter(name='Administrador').exists()
        list_estados = Estado.objects.all()
        
        if es_administrador:
            institucion = Institucion.objects.all()
        
        else:
        
            usuario = self.request.user
            id_institucion = usuario.usuarioinstitucion.institucion_id

            institucion = Institucion.objects.filter(id=id_institucion)

        context['list_estados'] = list_estados
        context['listar_institucion'] = institucion
        return context

    def post(self, request, *args, **kwargs):
        id_ele = self.request.POST.get('id_eleccion')
        response_data = []
        context = super(ListarGrafica, self).get_context_data(**kwargs)
        bandera = request.POST.get('bandera')
        tipo = request.POST.get('tipo')
        status = request.POST.get('status')
        desde = request.POST.get('from_date')
        hasta = request.POST.get('to_date')
        id_inst = request.POST.get('id_inst')

        cursor = connection.cursor()
        sql_sop = " SELECT m.nombre, COUNT(modelo_id) total "
        sql_sop += " FROM soporte_soporte s "
        sql_sop += " INNER JOIN modelos_modelos m ON s.modelo_id = m.id"

        if tipo == '1':
            sql_sop += " WHERE s.institucion_id=%s and s.fecha_create::date between %s and %s GROUP BY m.nombre"
            cursor.execute(sql_sop,[id_inst,desde,hasta])
        else:
            sql_sop += " WHERE s.institucion_id=%s and s.status=%s and s.fecha_create::date between %s and %s GROUP BY m.nombre"
            cursor.execute(sql_sop,[id_inst,status,desde,hasta])
        
        queryset = dictfetchall(cursor)
        ##print "HOLAAA",queryset
        tam = len(queryset)
        response_dat = {}
        i = 0
        while i < tam:
            response_data.append(queryset[i])
            i += 1
        
        data = json.dumps(response_data)
        
        return HttpResponse(data, content_type='application/json')


class PdfGeneral(View):

    template_name = 'reportes/reporte_soporte.html'
    # model = Votacion

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):
        tipo = self.request.GET.get('tipo')
        id_inst = self.request.GET.get('id_inst')
        status = self.request.GET.get('status')
        desde = self.request.GET.get('desde')
        hasta = self.request.GET.get('hasta')
        reload(sys)
        sys.setdefaultencoding("utf-8")
 
        cursor = connection.cursor()
        sql_sop = "SELECT serial, hardware, software, fecha_create, cod_solicitud_id, m.nombre, status"
        sql_sop += " FROM soporte_soporte s"
        sql_sop += " INNER JOIN modelos_modelos m ON s.modelo_id = m.id"
        sql_sop += " WHERE fecha_create::date between %s and %s"
        print 'aquiii',sql_sop
        cursor.execute(sql_sop,[desde,hasta])
        row = dictfetchall(cursor)
        

        if len(row) == 0:
            response = "<body>"
            response += "<link rel='stylesheet' type='text/css' href='/static/css/bootstrap.css'>"
            response += "<script src='/static/js/bootstrap.min.js'></script>"
            response += "<img src='/static/img/no_disponible.png' style='width:80%;margin-left:10%'/>"
            response += "<button title='Cerrar ventana' class='btn btn-danger' style='font-size:24px; width:20%; height: 10%; font-weight: bold; text-align: center;margin-left:40%' onclick=window.close()>Cerrar</button>"
            response += "<body>"
            return HttpResponse(response)
        else:
            nombre, archivo = reporte_soporte_general.reporte_soporte_general(id_inst,tipo,status,desde,hasta)
            response = HttpResponse(archivo.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="'+str(nombre)

            return response



def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


