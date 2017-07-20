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
from apps.reportes.reportes_solicitudes.class_pdf import ReporteConstruct
from django.db import connection, transaction
import time
from django.db import connection, transaction
from apps.reportes.reportes_solicitudes import procesos
from apps.configuracion.instituciones.models import Institucion
from django.conf import settings  # Ruta de settings
import class_pdf
import unicodedata


class ReporteSolicitudes(TemplateView):

    template_name = 'reportes/reporte_solicitudes.html'

    def get_context_data(self, **kwargs):
        context = super(ReporteSolicitudes, self).get_context_data(**kwargs)
        es_administrador = self.request.user.groups.all().filter(name='Administrador').exists()
        list_estados = Estado.objects.all()

        if es_administrador:
            institucion = Institucion.objects.all()

        else:

            usuario = self.request.user
            id_institucion = usuario.usuarioinstitucion.institucion_id


            institucion = Institucion.objects.filter(id=id_institucion)

        context['list_estados'] = list_estados
        context['institucion'] = institucion
        return context

class Reporte(View):

    def get_context_data(self, **kwargs):
        context = {}
        return context

    def get(self, request, *args, **kwargs):

        tipo = self.request.GET.get('tipo')
        institucion = self.request.GET.get('institucion')
        estado = self.request.GET.get('estado')
        municipio = self.request.GET.get('municipio')
        parroquia = self.request.GET.get('parroquia')
        status = self.request.GET.get('status')
        desde = self.request.GET.get('desde')
        hasta = self.request.GET.get('hasta')
        bandera = self.request.GET.get('bandera')

        if bandera == 'pdf':

            pdf = ReporteConstruct(orientation='L',unit='mm', format='letter')
            # pdf = class_pdf.ReporteConstruct

            pdf.alias_nb_pages()  # LLAMADA DE PAGINACION
            pdf.add_page()  # AÑADE UNA NUEVA PAGINACION
            # pdf.set_fill_color(157, 188, 201)  # COLOR DE BORDE DE LA CELDA
            # pdf.set_text_color(24, 29, 31)  # COLOR DEL TEXTO
            pdf.set_margins(15, 10, 10)

            pdf.set_font('Arial', 'B', 10)
            pdf.cell(140, 5, "".decode("UTF-8"), '', 0, 'L', 0)
            pdf.cell(50, 4, "".decode("UTF-8"), '', 0, 'L', 0)
            pdf.ln(10)
            ########################################################################

            pdf.set_fill_color(255, 255, 255)
            pdf.set_text_color(0, 0, 0)
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(250, 5, "LISTA DE SOLICITUDES".decode("UTF-8"), '', 1, 'C', 1)
            pdf.set_font('Arial', 'B', 10)
            pdf.cell(250,5,"Desde el "+str(desde)+" hasta el "+str(hasta).decode("UTF-8"),'',1,'C',1)
            pdf.set_font('Arial', 'B', 10)
            pdf.ln(5)

            pdf.set_fill_color(255, 255, 255)
            pdf.set_text_color(0, 0, 0)

            ##### CICLO FOR
            ROW = ''


            if tipo == '1':

                cursor = connection.cursor()
                QUERY = "select to_char(fecha_s, 'dd/mm/YYYY') as fecha_s, codigo, cedula, nombre2, apellido2, status from solicitud_registros WHERE institucion_id='"+str(institucion)+"' AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"' ORDER BY codigo asc"
                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)

            if tipo == '2' and estado != 0:

                cursor = connection.cursor()
                QUERY = "SELECT to_char(fecha_s, 'dd/mm/YYYY') AS fecha_s, codigo, cedula, nombre2, apellido2, status FROM solicitud_registros AS sr INNER JOIN estados_estado AS ee ON sr.estado_id=ee.id WHERE institucion_id='"+str(institucion)+"' AND sr.estado_id="+str(estado)+" AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"' ORDER BY codigo ASC"
                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)

            if tipo == '3' and estado != 0 and municipio !=0:

                cursor = connection.cursor()
                QUERY = "SELECT to_char(fecha_s, 'dd/mm/YYYY') AS fecha_s, codigo, cedula, nombre2, apellido2, status FROM solicitud_registros AS sr INNER JOIN estados_estado AS ee ON sr.estado_id=ee.id INNER JOIN municipios_municipio AS mm ON sr.municipio=mm.id WHERE institucion_id='"+str(institucion)+"' AND sr.estado_id="+str(estado)+" AND sr.municipio="+str(municipio)+" AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"' ORDER BY codigo ASC"
                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)

            if tipo == '4' and estado != 0 and municipio !=0 and parroquia !=0:

                cursor = connection.cursor()
                QUERY = "SELECT to_char(fecha_s, 'dd/mm/YYYY') AS fecha_s, codigo, cedula, nombre2, apellido2, status FROM solicitud_registros AS sr INNER JOIN estados_estado AS ee ON sr.estado_id=ee.id INNER JOIN municipios_municipio AS mm ON sr.municipio=mm.id INNER JOIN parroquias_parroquia AS pp ON sr.parroquia=pp.id WHERE institucion_id='"+str(institucion)+"' AND sr.estado_id="+str(estado)+" AND sr.municipio="+str(municipio)+" AND sr.parroquia="+str(parroquia)+" AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"' ORDER BY codigo ASC"
                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)

            if tipo == '5' and status != 0:

                cursor = connection.cursor()
                QUERY = "SELECT to_char(fecha_s, 'dd/mm/YYYY') AS fecha_s, codigo, cedula, nombre2, apellido2, status FROM solicitud_registros AS sr WHERE institucion_id='"+str(institucion)+"' AND sr.status='"+str(status)+"' AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"' ORDER BY codigo ASC"

                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)

            ##### ENCABEZADO DATOS PERSONALES

            pdf.set_fill_color(255, 29, 47)
            pdf.set_text_color(255, 255, 255)

            pdf.cell(10, 5, "N°".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(30, 5, "FECHA".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(30, 5, "CÓDIGO".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(30, 5, "CÉDULA".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(50, 5, "NOMBRE".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(50, 5, "APELLIDO".decode("UTF-8"), 'LTBR', 0, 'C', 1)
            pdf.cell(50, 5, "ESTATUS".decode("UTF-8"), 'LTBR', 0, 'C', 1)

            pdf.set_fill_color(255, 255, 255)
            pdf.set_text_color(0, 0, 0)

            item = 1
            for lr2 in ROW:
                if lr2['status'] == '1':
                    status = 'ATENDIENDO'
                elif lr2['status'] == '2':
                    status = 'REMITIDA'
                elif lr2['status'] == '3':
                    status = 'REPARADA'
                elif lr2['status'] == '4':
                    status = 'ENTREGADA'
                elif lr2['status'] == '5':
                    status = 'DEVUELTA'

                ##### CICLO FOR
                pdf.ln(5)
                pdf.cell(10, 5, str(item), 'LTBR', 0, 'C', 1)
                pdf.cell(30, 5, str(lr2['fecha_s']), 'LTBR', 0, 'C', 1)
                pdf.cell(30, 5, str(lr2['codigo']), 'LTBR', 0, 'C', 1)
                pdf.cell(30, 5, str(lr2['cedula']), 'LTBR', 0, 'C', 1)
                pdf.cell(50, 5, unicode(lr2['nombre2']), 'LTBR', 0, 'C', 1)
                pdf.cell(50, 5, unicode(lr2['apellido2']), 'LTBR', 0, 'C', 1)
                pdf.cell(50, 5, str(status), 'LTBR', 0, 'C', 1)
                item = item + 1

            if len(ROW) == 0:
                response = "<body>"
                response += "<link rel='stylesheet' type='text/css' href='/static/css/bootstrap.css'>"
                response += "<script src='/static/js/bootstrap.min.js'></script>"
                response += "<img src='/static/img/no_disponible.png' style='width:80%;margin-left:10%'/>"
                response += "<button title='Cerrar ventana' class='btn btn-danger' style='font-size:24px; width:20%; height: 10%; font-weight: bold; text-align: center;margin-left:40%' onclick=window.close()>Cerrar</button>"
                response += "<body>"
                return HttpResponse(response)
            else:

                self.get_context_data()
                arch = 'Solicitudes_registradas'
                ruta_reporte = settings.MEDIA_PDF
                archivo = ruta_reporte+'/'+str(arch)+'.pdf'
                pdf.output(archivo, 'F')
                archivo = open(archivo, "r")
                response = HttpResponse(archivo.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename="'+str(arch)+'.pdf"'

                return response

        else:
            response_data ={}
            ROW = ''


            if tipo == '1':

                cursor = connection.cursor()
                QUERY = "SELECT CASE"
                QUERY +=" WHEN status='1' THEN 'Atendiendo'"
                QUERY +=" WHEN status='2' THEN 'Remitida'"
                QUERY +=" WHEN status='3' THEN 'Reparada'"
                QUERY +=" WHEN status='4' THEN 'Entregada'"
                QUERY +=" ELSE 'Devuelta'"
                QUERY +=" END AS name, count(status) as y from solicitud_registros where institucion_id='"+str(institucion)+"' AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"' group by status"
                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)
                #print ROW

            if tipo == '2' and estado != 0:

                cursor = connection.cursor()
                QUERY = "SELECT CASE"
                QUERY +=" WHEN status='1' THEN 'Atendiendo'"
                QUERY +=" WHEN status='2' THEN 'Remitida'"
                QUERY +=" WHEN status='3' THEN 'Reparada'"
                QUERY +=" WHEN status='4' THEN 'Entregada'"
                QUERY +=" ELSE 'Devuelta' END AS name, count(status) as y"
                QUERY +=" FROM solicitud_registros As sr"
                QUERY +=" INNER JOIN estados_estado AS ee ON sr.estado_id=ee.id"
                QUERY +=" WHERE institucion_id='"+str(institucion)+"' AND sr.estado_id="+str(estado)+" AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"'"
                QUERY +=" GROUP BY status"
                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)
                #print ROW

            if tipo == '3' and estado != 0 and municipio !=0:

                cursor = connection.cursor()
                QUERY = "SELECT CASE"
                QUERY +=" WHEN status='1' THEN 'Atendiendo'"
                QUERY +=" WHEN status='2' THEN 'Remitida'"
                QUERY +=" WHEN status='3' THEN 'Reparada'"
                QUERY +=" WHEN status='4' THEN 'Entregada'"
                QUERY +=" ELSE 'Devuelta' END AS name, count(status) as y"
                QUERY +=" FROM solicitud_registros As sr"
                QUERY +=" INNER JOIN estados_estado AS ee ON sr.estado_id=ee.id"
                QUERY +=" INNER JOIN municipios_municipio AS mm ON sr.municipio=mm.id"
                QUERY +=" WHERE institucion_id='"+str(institucion)+"' AND sr.estado_id="+str(estado)+" AND sr.municipio="+str(municipio)+" AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"'"
                QUERY +=" GROUP BY status"
                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)

            if tipo == '4' and estado != 0 and municipio !=0 and parroquia !=0:

                cursor = connection.cursor()
                QUERY = "SELECT CASE"
                QUERY +=" WHEN status='1' THEN 'Atendiendo'"
                QUERY +=" WHEN status='2' THEN 'Remitida'"
                QUERY +=" WHEN status='3' THEN 'Reparada'"
                QUERY +=" WHEN status='4' THEN 'Entregada'"
                QUERY +=" ELSE 'Devuelta' END AS name, count(status) as y"
                QUERY +=" FROM solicitud_registros As sr"
                QUERY +=" INNER JOIN estados_estado AS ee ON sr.estado_id=ee.id"
                QUERY +=" INNER JOIN municipios_municipio AS mm ON sr.municipio=mm.id"
                QUERY +=" INNER JOIN parroquias_parroquia AS pp ON sr.parroquia=pp.id"
                QUERY +=" WHERE institucion_id='"+str(institucion)+"' AND sr.estado_id="+str(estado)+" AND sr.municipio="+str(municipio)+" AND sr.parroquia="+str(parroquia)+" AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"'"
                QUERY +=" GROUP BY status"
                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)

            if tipo == '5' and status != 0:

                cursor = connection.cursor()
                QUERY = "SELECT CASE"
                QUERY +=" WHEN status='1' THEN 'Atendiendo'"
                QUERY +=" WHEN status='2' THEN 'Remitida'"
                QUERY +=" WHEN status='3' THEN 'Reparada'"
                QUERY +=" WHEN status='4' THEN 'Entregada'"
                QUERY +=" ELSE 'Devuelta' END AS name, count(status) as y"
                QUERY +=" FROM solicitud_registros As sr"
                QUERY +=" WHERE institucion_id='"+str(institucion)+"' AND sr.status='"+str(status)+"' AND fecha_s BETWEEN '"+str(desde)+"' AND '"+str(hasta)+"'"
                QUERY +=" GROUP BY status"
                cursor.execute(QUERY)
                ROW = procesos.dictfetchall(cursor)

            return HttpResponse(json.dumps(ROW), content_type='application/json')

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


