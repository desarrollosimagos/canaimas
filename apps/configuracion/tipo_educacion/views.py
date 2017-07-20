from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import TipoEducacion
from apps.configuracion.grados.models import Grados
from django.http import HttpResponse, HttpResponseRedirect
import json


class RegistrarTipoEducacion(CreateView):
    template_name = 'configuracion/tipo_educacion/registro.html'
    model = TipoEducacion
    success_url = reverse_lazy("listar_tipo_educacion")

    def post(self, request, *args, **kwargs):
        bandera = request.POST.get('bandera')
        tipo = request.POST.get('tipo')
        existe_tipo = TipoEducacion.objects.filter(tipo=tipo).exists()

        if existe_tipo and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/menu/configuraciones/tipo_educacion/listar/')


class ListarTipoEducacion(ListView):
    template_name = 'configuracion/tipo_educacion/listar.html'
    model = TipoEducacion
    context_object_name = "listar_tipo"


class EditarTipoEducacion(UpdateView):
    template_name = 'configuracion/tipo_educacion/editar.html'
    model = TipoEducacion
    success_url = reverse_lazy("listar_tipo_educacion")
    context_object_name = "editar_tipo"

    def post(self, request, *args, **kwargs):
        id_r = request.POST.get('id')
        bandera = request.POST.get('bandera')
        tipo = request.POST.get('tipo')
        existe_tipo = TipoEducacion.objects.filter(tipo=tipo).exclude(id=id_r).exists()

        if existe_tipo and bandera == 'true':
            return HttpResponse('existe')
        else:
            TipoEducacion.objects.filter(id=id_r).update(tipo=tipo)

            return HttpResponseRedirect('/menu/configuraciones/tipo_educacion/listar/')


class EliminarTipoEducacion(DeleteView):
    #template_name = 'configuracion/tipo_educacion/eliminar.html'
    model = TipoEducacion
    
    def delete(self, request, *args, **kwargs):
        response_data = {}
        existe = Grados.objects.filter(tipo_id=self.kwargs['pk'])
        if existe.exists():
            response_data['existe'] = 'si'
        else:
            existe = TipoEducacion.objects.filter(id=self.kwargs['pk'])
            if existe.exists():
                self.object = self.get_object()
                self.object.delete()
                response_data['eliminado'] = 'ok'
        
        return HttpResponse(json.dumps(response_data), status=200, content_type='application/json')