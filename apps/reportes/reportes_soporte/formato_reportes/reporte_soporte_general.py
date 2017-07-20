#encoding:utf-8
import class_pdf
import sys
from django.db import connection, transaction
from django.conf import settings
from apps.script import delete_Files


def reporte_soporte_general(id_inst,tipo,status,desde,hasta):

        reload(sys)
        sys.setdefaultencoding("utf-8")

        pdf = class_pdf.ReporteCandidato(orientation='P', unit='mm', format='letter')  # HORIENTACION DE LA PAGINA

        pdf.set_author('Marcel Arcuri')
        pdf.alias_nb_pages()  # LLAMADA DE PAGINACION
        pdf.add_page()  # ANADE UNA NUEVA PAGINACION
        pdf.set_margins(15,10,10)  # MARGENE DEL DOCUMENTO

        pdf.ln(5)
        pdf.set_fill_color(255, 255, 255)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(180,5,"Listado de Soporte Técnico".decode("UTF-8"),'',1,'C',1)
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(180,5,"Desde el "+str(desde)+" hasta el "+str(hasta).decode("UTF-8"),'',1,'C',1)
        pdf.set_font('Arial', 'B', 10)
        pdf.ln(5)
        
        # Fila de la cabezara de la tabla
        pdf.set_fill_color(255,29,47)
        pdf.set_text_color(255,255,255)
        pdf.set_font('Arial','B',10)
        pdf.cell(10,5,"N°".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,5,"Solicitudes".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,5,"Serial".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,5,"Modelo".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,5,"Fecha".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,5,"Estatus".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,5,"Hardware".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(20,5,"Software".decode("UTF-8"),'LTBR',0,'C',1)
        pdf.cell(35,5,"Técnico".decode("UTF-8"),'LTBR',1,'C',1)
        pdf.set_fill_color(255,255,255)
        pdf.set_font('Arial','',10)

        
        cursor = connection.cursor()
        sql_sop = "SELECT r.codigo, s.serial, m.nombre, to_char(s.fecha_create, 'dd/mm/YYYY') as fecha_create, s.status, s.hardware, s.software, a.username"
        sql_sop += " FROM soporte_soporte s"
        sql_sop += " INNER JOIN modelos_modelos m ON s.modelo_id = m.id"
        sql_sop += " INNER JOIN solicitud_registros r ON s.cod_solicitud_id = r.id"
        sql_sop += " INNER JOIN auth_user a ON s.user_create_id = a.id"

        if tipo == '1':
                sql_sop += " WHERE s.institucion_id=%s and s.fecha_create::date between %s and %s"
                sql_sop += " ORDER BY r.codigo"
                cursor.execute(sql_sop,[id_inst,desde,hasta])
        else:
                sql_sop += " WHERE s.institucion_id=%s and s.status=%s and s.fecha_create::date between %s and %s"
                sql_sop += " ORDER BY r.codigo"
                cursor.execute(sql_sop,[id_inst,status,desde,hasta])
        
        row = dictfetchall(cursor)
        
        i = 1
        j = 0
        item = 0
        for t in row:
                # id_c = t['id_c']
                pdf.set_fill_color(255,255,255)
                if j == 20:
                        pdf.add_page()
                        pdf.set_fill_color(255,255,255)
                        pdf.ln(5)
                        pdf.set_fill_color(255, 255, 255)
                        pdf.set_font('Arial', 'B', 12)
                        pdf.cell(180,5,"Listado de Soporte Técnico".decode("UTF-8"),'',1,'C',1)
                        pdf.set_font('Arial', 'B', 10)
                        pdf.cell(180,5,"Desde el "+str(desde)+" hasta el "+str(hasta).decode("UTF-8"),'',1,'C',1)
                        pdf.set_font('Arial', 'B', 10)
                        pdf.ln(5)
                        
                        # Fila de la cabezara de la tabla
                        pdf.set_fill_color(255,29,47)
                        pdf.set_text_color(255,255,255)
                        pdf.set_font('Arial','B',10)
                        pdf.cell(10,5,"N°".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(20,5,"Solicitudes".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(20,5,"Serial".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(20,5,"Modelo".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(20,5,"Fecha".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(20,5,"Estatus".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(20,5,"Hardware".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(20,5,"Software".decode("UTF-8"),'LTBR',0,'C',1)
                        pdf.cell(35,5,"Técnico".decode("UTF-8"),'LTBR',1,'C',1)
                        pdf.set_fill_color(255,255,255)
                        pdf.set_font('Arial','',10)
                        # Fin Cabezera
                        j=0
                item = int(item) + 1
                # Filas que vienen de la BD
                print t['status']
                if t['status'] == '2':
                        est = 'REMITIDA'
                else:
                        est = 'REPARADA'

                if t['hardware'] == True:
                        har = 'X'
                else:
                        har = ''

                if t['software'] == True:
                        sof = 'X'
                else:
                        sof = ''

                pdf.set_font('Arial','',8)
                pdf.set_fill_color(255,255,255)
                pdf.set_text_color(24,29,31)
                pdf.cell(10,5,str(item).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(20,5,str(t['codigo']).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(20,5,str(t['serial']),'LTBR',0,'C',1)
                pdf.cell(20,5,str(t['nombre']),'LTBR',0,'C',1)
                pdf.cell(20,5,str(t['fecha_create']).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(20,5,str(est),'LTBR',0,'C',1)
                pdf.cell(20,5,str(har),'LTBR',0,'C',1)
                pdf.cell(20,5,str(sof).decode("UTF-8"),'LTBR',0,'C',1)
                pdf.cell(35,5,str(t['username']).upper(),'LTBR',1,'C',1)
                j = j + 1
        ruta_reporte = settings.MEDIA_PDF
        nombre = ' Detallado.pdf'
        pdf.output(ruta_reporte+'/'+nombre, 'F')
        archivo = open(ruta_reporte+'/'+nombre, "r")

        ruta = ruta_reporte+'/'
        delete_Files(ruta)
        
        return nombre, archivo


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
