from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.configuracion.tipo_educacion.models import TipoEducacion
from .models import Grados
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
import json


class RegistrarGrados(CreateView):
    template_name = 'configuracion/grados/registro.html'
    model = Grados
    success_url = reverse_lazy("listar_grados")

    def get_context_data(self, **kwargs):
        context = super(RegistrarGrados, self).get_context_data(**kwargs)
        queryset = TipoEducacion.objects.all()

        context['listado_tipo'] = queryset
        return context

    def post(self, request, *args, **kwargs):
        bandera = request.POST.get('bandera')
        grado = request.POST.get('grado')
        existe_grado = Grados.objects.filter(grado=grado).exists()

        if existe_grado and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/menu/configuraciones/grados/listar/')


class ListarGrados(ListView):
    template_name = 'configuracion/grados/listar.html'
    model = Grados
    context_object_name = "listar_grados" ### esta variable es la del for


class EditarGrados(UpdateView):
    template_name = 'configuracion/grados/editar.html'
    model = Grados
    success_url = reverse_lazy("listar_grados")
    context_object_name = "editar_grados"  # value de la caja de texto

    # funcion para llenar el combo de un campo
    def get_context_data(self, **kwargs):
        context = super(EditarGrados, self).get_context_data(**kwargs)
        queryset = TipoEducacion.objects.all()

        context['listado_tipo'] = queryset 
        return context

    def post(self, request, *args, **kwargs):
        id_r = request.POST.get('id')
        bandera = request.POST.get('bandera')
        grado = request.POST.get('grado')
        tipo = request.POST.get('tipo')
        existe_grado = Grados.objects.filter(grado=grado).exclude(id=id_r).exists()

        if existe_grado and bandera == 'true':
            return HttpResponse('existe')
        else:
            Grados.objects.filter(id=id_r).update(grado=grado, tipo=tipo)
            return HttpResponseRedirect('/menu/configuraciones/grados/listar/')


class EliminarGrados(DeleteView):
    model = Grados
   
    def delete(self, request, *args, **kwargs):
        response_data = {}
        
        id_grado = Grados.objects.all().values('tipo_id')
        
        id_tipo = TipoEducacion.objects.all().values('id')
        
        existe = Grados.objects.filter(tipo_id=id_tipo)
        
        if existe.exists():
            response_data['existe'] = 'si'
        else:
            existe = TipoEducacion.objects.filter(id=id_grado)
            if existe.exists():
                self.object = self.get_object()
                self.object.delete()
                response_data['eliminado'] = 'ok'
        
        return HttpResponse(json.dumps(response_data), status=200, content_type='application/json')
    
def BuscarAjaxGrados(request):
    
    id_tip = request.GET['id']
    grados = Grados.objects.filter(tipo_id=id_tip)
    data = serializers.serialize('json',grados,
                                       fields=('id','grado'))
    
    return HttpResponse(data, content_type='application/json')