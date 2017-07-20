# encoding:utf-8
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Soporte
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.configuracion.modelos.models import Modelos
from .forms import SoporteForm
from apps.registro.solicitud.models import Registros
from django.core import serializers
from django.contrib.auth.models import User


class RegistrarSoporte(CreateView):
    """ Vista basada en clase: (`Registrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminado el registro
        satisfactoriamente
    :param form_class: nombre de la clase Formulario
    """
    template_name = 'registro/soporte/soporte.html'
    model = Soporte
    success_url = reverse_lazy("listar_soporte")
    form_class = SoporteForm

    def get_context_data(self, **kwargs):
        """ Vista basada en Clases con un metodo: (`Registrar`). """

        context = super(RegistrarSoporte, self).get_context_data(**kwargs)
        
        usuario = self.request.user
        id_institucion = usuario.usuarioinstitucion.institucion_id
        
        listar_registros = Registros.objects.filter(institucion_id=id_institucion, status=1)
        listar_modelo = Modelos.objects.all()
        usuario_id = self.request.user.id
        usuario = User.objects.get(id=usuario_id).username
        
        context['listar_registros'] = listar_registros
        context['listar_modelo'] = listar_modelo
        context['usuario'] = usuario

        return context

    def post(self, request, *args, **kwargs):

        # bandera = request.POST.get('bandera')
        id_sol = request.POST.get('cod_solicitud')
        descripcion = request.POST.get('descripcion')
        status = request.POST.get('status')

        Registros.objects.filter(id=id_sol).update(reparacion=descripcion, status=status)
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.save()
            return HttpResponse('procesado')


class ListarSoporte(ListView):
    """ Vista basada en clase: (`Listar`)
    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Soporte
    template_name = 'registro/soporte/listar.html'
    #context_object_name = "listar_soporte"
    
    def get_context_data(self, **kwargs):
        context = {}
        es_administrador = self.request.user.groups.all().filter(name='Administrador').exists()
        
        data = {}
        datos = []
            
        if es_administrador:
            solicitudes = Soporte.objects.all()
            solicitudes_v = solicitudes.values('id', 'cod_solicitud_id__codigo', 'status')
            for n in solicitudes_v:
                data = n
                datos.append(data)
        else:
            
            usuario = self.request.user.usuarioinstitucion
            institucion_id = usuario.institucion_id
            
            solicitudes = Soporte.objects.all()
            solicitudes_f = solicitudes.filter(institucion_id=institucion_id)
            solicitudes_v = solicitudes_f.values('id', 'cod_solicitud_id__codigo', 'status')
            
            for n in solicitudes_v:
                data = n
                datos.append(data)
           
        context['listar_soporte'] = datos
        return context


class EditarSoporte(UpdateView):
    """ Vista basada en clase: (`Editar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminada la edición del
        registro satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Soporte
    template_name = 'registro/soporte/modificar.html'
    context_object_name = "editar_soporte"
    success_url = reverse_lazy("listar_soporte")

    def get_context_data(self, **kwargs):
        """ Vista basada en Clases con un metodo: (`Registrar`). """

        context = super(EditarSoporte, self).get_context_data(**kwargs)
        listar_registros = Registros.objects.all()
        listar_modelo = Modelos.objects.all()

        context['listar_registros'] = listar_registros
        context['listar_modelo'] = listar_modelo

        return context


class BorrarSoporte(DeleteView):
    """ Vista basada en clase: ('Borrar')

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
        satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Soporte
    template_name = 'registro/soporte/borrar.html'
    context_object_name = "borrar_soporte"
    success_url = reverse_lazy("listar_soporte")

    # def get_context_data(self, **kwargs):
    #     context = super(BorrarSoporte, self).get_context_data(**kwargs)
    #     pk_ins = self.kwargs['pk']
    #     soporte = Soporte.objects.all()
    #     id_sol = soporte.filter(pk=pk_ins).values('id')
    # 
    #     dep = Dependencia.objects.all()
    #     existe = dep.filter(soporte_id=id_sol)
    # 
    #     cantidad = len(existe)
    # 
    #     context['cantidad'] = cantidad
    #     return context


def BuscarSolicitud(request):

    id_sol = request.GET['id']
    solicitudes = Registros.objects.filter(id=id_sol)
    
    data = serializers.serialize('json', solicitudes,
                                 fields=('serial', 'modelo', 'descripcion', 'institucion'))
    return HttpResponse(data, content_type='application/json')
