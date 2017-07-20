from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.configuracion.grados.models import Grados
from apps.configuracion.tipo_educacion.models import TipoEducacion
from apps.configuracion.modelos.models import Modelos
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.configuracion.instituciones.models import Institucion
from .models import Registros
from apps.registro.soporte.models import Soporte
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import time
import json
import re

class RegistrarSolicitud(CreateView):
    template_name = 'registro/solicitud/registro.html'
    model = Registros
    success_url = reverse_lazy("lista") 
    
    def get_context_data(self, **kwargs):
        context = super(RegistrarSolicitud, self).get_context_data(**kwargs)
        
        usuario = self.request.user
        id_institucion = usuario.usuarioinstitucion.institucion_id
        
        institucion = Institucion.objects.all()
        institucion_f = institucion.filter(id=id_institucion)
        institucion_v =  institucion_f.values('id', 'nom_institucion')
        
        modelo    = Modelos.objects.all()
        tipo  = TipoEducacion.objects.all()
        grados = Grados.objects.all()
        estado    = Estado.objects.all()
        estado2   = Estado.objects.all()
        
        codigo = Registros.objects.order_by('-id').values('codigo')[:1] # ordenar de forma descendente y traer solo 1
        
        if codigo.count() > 0:
            
            codigo = re.findall(r'\d+', codigo[0]['codigo']) # extraer solo numeros 
            codigo =  int(codigo[0]) # convertir a entero (eliminar los 0 a la izquierda)
            codigo = "GC"+str(codigo+1).zfill(4) # sumo 1 y se rellena con 4 "0" a la izquierda
        else:
            codigo = 'GC0001'
        
        fecha_s = time.strftime("%d/%m/%Y")
        usuario_id = self.request.user.id
        usuario = User.objects.get(id=usuario_id).username
        
        context['lista_modelo'] = modelo
        context['lista_institucion'] = institucion_v
        context['listado_tipo'] = tipo
        context['listado_grado'] = grados
        context['listado_estado']= estado
        context['lista_estado'] = estado2
        context['codigo'] = codigo
        context['fecha_s'] = fecha_s
        context['usuario'] = usuario
        return context

    def post(self, request, *args, **kwargs):
       
        bandera = request.POST.get('bandera')
        codigo = request.POST.get('codigo')

        existe_cod = Registros.objects.filter(codigo=codigo).exists()
        print existe_cod
        if existe_cod and bandera == 'true':
            return HttpResponse('existe_cod')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
                return HttpResponse('/menu/registros/solicitud/listar/')
    
class ListarSolicitud(ListView):
    template_name = 'registro/solicitud/listado.html'
    model = Registros
    
    def get_context_data(self, **kwargs):
        context = {}
        es_administrador = self.request.user.groups.all().filter(name='Administrador').exists()
        
        data = {}
        datos = []
            
        if es_administrador:
            solicitudes = Registros.objects.all()
            solicitudes_v = solicitudes.values('id', 'institucion_id__siglas', 'institucion_id__nom_institucion', 'codigo', 'cedula', 'serial', 'nombre2', 'apellido2', 'fecha_s', 'fecha_e', 'status')
            for n in solicitudes_v:
                data = n
                datos.append(data)
        else:
            
            usuario = self.request.user.usuarioinstitucion
            institucion_id = usuario.institucion_id
            
            solicitudes = Registros.objects.all()
            solicitudes_f = solicitudes.filter(institucion_id=institucion_id)
            solicitudes_v = solicitudes_f.values('id', 'institucion_id__siglas', 'institucion_id__nom_institucion', 'codigo', 'cedula', 'serial', 'nombre2', 'apellido2', 'fecha_s', 'fecha_e', 'status')
            
            for n in solicitudes_v:
                data = n
                datos.append(data)
           
        context['listado'] = datos
        return context
    

class Remitida(UpdateView):
    
    def post(self, request, *args, **kwargs):
        response_data = {}
        id_reg = self.request.POST.get('id')
        print "aqui",id_reg
        Registros.objects.filter(id=id_reg).update(status='5')
                
        return HttpResponse('exito')

class Entregada(UpdateView):
    
    def post(self, request, *args, **kwargs):
        response_data = {}
        id_reg = self.request.POST.get('id')
        print "aadas",id_reg
        Registros.objects.filter(id=id_reg).update(status='4')
                
        return HttpResponse('exito')

    
class ActualizarSolicitud(UpdateView):
    template_name = 'registro/solicitud/actualizar.html'
    model = Registros
    success_url = reverse_lazy("lista")
    context_object_name = "registro_act" 
    
    def get_context_data(self, **kwargs):
        context = super(ActualizarSolicitud, self).get_context_data(**kwargs)
        
        modelo    = Modelos.objects.all()
        institucion = Institucion.objects.all()
        tipo  = TipoEducacion.objects.all()
        grados = Grados.objects.all()
        estado    = Estado.objects.all()
        estado2   = Estado.objects.all()
        list_mun = Municipio.objects.all()
        list_mun2 = Municipio.objects.all()
        list_par = Parroquia.objects.all()
        list_par2 = Parroquia.objects.all()
        
        context['lista_modelo'] = modelo
        context['lista_institucion'] = institucion
        context['listado_tipo'] = tipo
        context['listado_grado'] = grados
        context['listado_estado']= estado
        context['lista_estado'] = estado2
        context['list_mun'] = list_mun
        context['list_mun2'] = list_mun2
        context['list_par'] = list_par
        context['list_par2'] = list_par2
        return context
    
class EliminarSolicitud(DeleteView):
    template_name = 'registro/solicitud/eliminar.html'
    model = Registros
    
    def delete(self, request, *args, **kwargs):
        response_data = {}
        existe = Soporte.objects.filter(cod_solicitud_id=self.kwargs['pk'])
        if existe.exists():
            response_data['existe'] = 'si'
        else:
            existe = Registros.objects.filter(id=self.kwargs['pk'])
            print existe
            if existe.exists():
                self.object = self.get_object()
                self.object.delete()
                response_data['eliminado'] = 'ok'
        
        return HttpResponse(json.dumps(response_data), status=200, content_type='application/json')
    
def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]