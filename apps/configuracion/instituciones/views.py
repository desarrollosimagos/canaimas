# encoding:utf-8
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Institucion
from django.http import HttpResponse, HttpResponseRedirect
from .forms import InstitucionForm
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from apps.topologia.parroquias.models import Parroquia
from apps.registro.solicitud.models import Registros
import json


class RegistrarInstitucion(CreateView):
    
    template_name = 'configuracion/institucion/institucion.html'
    model = Institucion
    success_url = reverse_lazy("listar_institucion")
    form_class = InstitucionForm

    def get_context_data(self, **kwargs):
        """ Vista basada en Clases con un metodo: (`Registrar`). """

        context = super(RegistrarInstitucion, self).get_context_data(**kwargs)
        listar_estado = Estado.objects.all()

        context['listar_estados'] = listar_estado

        return context

    def post(self, request, *args, **kwargs):
        bandera = request.POST.get('bandera')
        nom_institucion = request.POST.get('nom_institucion')
        existe = Institucion.objects.filter(nom_institucion=nom_institucion).exists()
        if existe and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/menu/configuraciones/instituciones/')


class ListarInstitucion(ListView):
    
    model = Institucion
    template_name = 'configuracion/institucion/listar.html'
    context_object_name = "listar_institucion"

    def post(self, request, *args, **kwargs):

        pk_inst = self.request.POST.get('pk')
        status = self.request.POST.get('institucion_activa')

        #  Validamos el status
        if status == 'false':
            status = False
        else:
            status = True

        #Buscamos el id(pk) del usuario en el modelo de Usuario
        institucion = Institucion.objects.filter(id=pk_inst)
        institucion.update(
            institucion_activa=status
        )
        return HttpResponse('exito')


class EditarInstitucion(UpdateView):
   
    model = Institucion
    template_name = 'configuracion/institucion/modificar.html'
    context_object_name = "editar_institucion"
    success_url = reverse_lazy("listar_institucion")

    def get_context_data(self, **kwargs):

        context = super(EditarInstitucion, self).get_context_data(**kwargs)
        pk_inst = self.kwargs['pk']
        institucion = Institucion.objects.all()
        cod_est = institucion.filter(pk=pk_inst).values('estado_id')
        cod_mun = institucion.filter(pk=pk_inst).values('municipio')
        # cod_parr = institucion.filter(pk=pk_inst).values('parroquia')

        list_estado = Estado.objects.all()
        list_mun = Municipio.objects.filter(estado_id=cod_est)
        list_par = Parroquia.objects.filter(estado_id=cod_est, municipio=cod_mun)

        context['list_estado'] = list_estado
        context['list_mun'] = list_mun
        context['list_par'] = list_par

        return context


class BorrarInstitucion(DeleteView):
    template_name = 'configuracion/institucion/borrar.html'
    model = Institucion
        
    def delete(self, request, *args, **kwargs):
        response_data = {}
        existe = Registros.objects.filter(institucion_id=self.kwargs['pk'])
        print existe
        if existe.exists():
            response_data['existe'] = 'si'
        else:
            existe = Institucion.objects.filter(id=self.kwargs['pk'])
            print existe
            if existe.exists():
                self.object = self.get_object()
                self.object.delete()
                response_data['eliminado'] = 'ok'
        return HttpResponse(json.dumps(response_data), status=200, content_type='application/json')
