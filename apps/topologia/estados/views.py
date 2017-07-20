#encoding:utf-8
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from .models import Estado
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .forms import EstadoForm
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.utils.decorators import method_decorator
from apps.topologia.municipios.models import Municipio



class RegistrarEstado(CreateView):
    """ Vista basada en clase: (`Registrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminado el registro
        satisfactoriamente
    :param form_class: nombre de la clase Formulario
    """
    template_name = 'topologia/estados/estados.html'
    model = Estado
    success_url = reverse_lazy("listar_estado")
    form_class = EstadoForm

    def post(self, request, *args, **kwargs):
        bandera = request.POST.get('bandera')
        cod_estado = request.POST.get('cod_estado')
        estado = request.POST.get('estado')
        existe = Estado.objects.filter(estado=estado).exists()
        existe_c = Estado.objects.filter(cod_estado=cod_estado).exists()
        if existe and bandera == 'true':
            return HttpResponse('existe')
        elif existe_c and bandera == 'true':
            return HttpResponse('existe_c')
        else:
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/menu/topologia/estados/')


class ListarEstado(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    
    """
    model = Estado
    template_name = 'topologia/estados/listar.html'
    context_object_name = "listar_estado"


class EditarEstado(UpdateView):
    """ Vista basada en clase: (`Editar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez culminada la edición del
        registro satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Estado
    template_name = 'topologia/estados/modificar.html'
    context_object_name = "editar_estado"
    success_url = reverse_lazy("listar_estado")


class BorrarEstado(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
        satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Estado
    template_name = 'topologia/estados/borrar.html'
    context_object_name = "borrar_estado"
    success_url = reverse_lazy("listar_estado")

    def get_context_data(self, **kwargs):
        context = super(BorrarEstado, self).get_context_data(**kwargs)
        pk_est = self.kwargs['pk']
        estado = Estado.objects.all()
        id_est = estado.filter(pk=pk_est).values('cod_estado')
    
        mun = Municipio.objects.all()
        existe = mun.filter(estado_id=id_est)
        cantidad = len(existe)
    
        context['cantidad'] = cantidad
        return context
