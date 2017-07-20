from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Modelos
from .forms import ModelosForm
from apps.registro.solicitud.models import Registros
from django.http import HttpResponse, HttpResponseRedirect
import json

class RegistrarModelos(CreateView):
    template_name = 'configuracion/modelos/registro.html'
    model = Modelos
    success_url = reverse_lazy("listar_modelos")
    form_class = ModelosForm

    def post(self, request, *args, **kwargs):
        bandera = request.POST.get('bandera')
        nombre = request.POST.get('nombre')
        existe_modelo = Modelos.objects.filter(nombre=nombre).exists()
        
        if existe_modelo and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
                return HttpResponse('/menu/configuraciones/modelos/listar/')


class ListarModelos(ListView):
    template_name = 'configuracion/modelos/listar.html'
    model = Modelos
    context_object_name = "listar_modelo"


class EditarModelos(UpdateView):
    template_name = 'configuracion/modelos/editar.html'
    model = Modelos
    success_url = reverse_lazy("listar_modelos")
    context_object_name = "editar_modelo"

    def post(self, request, *args, **kwargs):
        id_r = request.POST.get('id')
        bandera = request.POST.get('bandera')
        nombre = request.POST.get('nombre')
        existe_modelo = Modelos.objects.filter(nombre=nombre).exclude(id=id_r).exists()

        if existe_modelo and bandera == 'true':
            return HttpResponse('existe')
        else:
            Modelos.objects.filter(id=id_r).update(nombre=nombre)

            return HttpResponse('/menu/configuraciones/modelos/listar/')


class EliminarModelos(DeleteView):
    template_name = 'configuracion/modelos/eliminar.html'
    model = Modelos
    
    def delete(self, request, *args, **kwargs):
        response_data = {}
        existe = Registros.objects.filter(modelo_id=self.kwargs['pk'])
        if existe.exists():
            response_data['existe'] = 'si'
        else:
            existe = Modelos.objects.filter(id=self.kwargs['pk'])
            if existe.exists():
                self.object = self.get_object()
                self.object.delete()
                response_data['eliminado'] = 'ok'
        
        return HttpResponse(json.dumps(response_data), status=200, content_type='application/json')