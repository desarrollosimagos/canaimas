from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # Paginacion
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from apps.topologia.estados.models import Estado
from .models import Municipio
from .forms import MunicipioForm
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group, Permission, User
from django.utils.decorators import method_decorator
from apps.topologia.parroquias.models import Parroquia

@login_required(login_url='/')

def RegistrarMunicipio(request):
    """
        Vista basada en Metodos o funciones: (`Registrar`)
    """
    lista_estado = Estado.objects.all()
    mun = Municipio.objects.all()
    count_m = len(mun) + 1
    if request.method == 'POST':
        bandera = request.POST.get('bandera')
        cod_municipio = request.POST.get('cod_municipio')
        estado = request.POST.get('estado')
        municipio = request.POST.get('municipio')
        existe_c = Municipio.objects.filter(estado=estado, cod_municipio=cod_municipio).exists()
        existe_n = Municipio.objects.filter(estado=estado, municipio=municipio).exists()
        existe_t = Municipio.objects.filter(estado=estado, cod_municipio=cod_municipio, municipio=municipio).exists()
        if existe_t and bandera == 'true':
            return HttpResponse('existe_t')
        elif existe_c and bandera == 'true':
            return HttpResponse('existe_c')
        elif existe_n and bandera == 'true':
            return HttpResponse('existe_n')
        else:
            form_reg_mun = MunicipioForm(request.POST, request.FILES)
            if form_reg_mun.is_valid():
                new_reg_mun = form_reg_mun.save(commit=False)
                new_reg_mun.save()
            return HttpResponseRedirect('/menu/topologia/municipios/')
    else:
        form_reg_mun = MunicipioForm()
    ctx = {'form_reg_mun': form_reg_mun, 'lista_estado': lista_estado, 'count_m': count_m}
    return render_to_response('topologia/municipios/municipios.html',
                              ctx, context_instance=RequestContext(request))


@login_required(login_url='/')
def ActualizarMunicipio(request, pk):
    """ Vista basada en Metodos o funciones: (`Modificar`). """
    obj_reg_mun = Municipio.objects.get(id=pk)
    lista_estado = Estado.objects.all()
    # lista_circuito = Circuito.objects.filter(estado_id=obj_reg_mun.estado_id)
    if request.method == 'POST':
        bandera = request.POST.get('bandera')
        cod_municipio = request.POST.get('cod_municipio')
        estado = request.POST.get('estado')
        existe = Municipio.objects.filter(cod_municipio=cod_municipio, estado=estado).exists()

        if existe and bandera == 'true':
            return HttpResponse('existe')
        else:
            form_reg_mun = MunicipioForm(request.POST, request.FILES, instance=obj_reg_mun)
            if form_reg_mun.is_valid():
                edit_reg_mun = form_reg_mun.save(commit=False)
                edit_reg_mun.save()
            return HttpResponseRedirect('/menu/topologia/municipios/')
    else:
        form_reg_mun = MunicipioForm(instance=obj_reg_mun)
    ctx = {'form_reg_mun': form_reg_mun, 'obj_reg_mun': obj_reg_mun, 'lista_estado': lista_estado,}  # ctx = Contexto
    return render_to_response('topologia/municipios/modificar.html',
                              ctx, context_instance=RequestContext(request))


class ListarMunicipio(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    :param paginate_by: Genera la paginacion de los registros en base a la cantidad definida.
    """
    model = Municipio
    template_name = 'topologia/municipios/listar.html'
    context_object_name = "listar_municipio"


class BorrarMunicipio(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
        satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Municipio
    template_name = 'topologia/municipios/borrar.html'
    context_object_name = "borrar_municipio"
    success_url = reverse_lazy("listar_municipio")

    def get_context_data(self, **kwargs):
        context = super(BorrarMunicipio, self).get_context_data(**kwargs)
        pk_mun = self.kwargs['pk']
        municipio = Municipio.objects.all()
        id_mun = municipio.filter(pk=pk_mun).values('cod_municipio')
        
        par = Parroquia.objects.all()
        existe = par.filter(municipio=id_mun)
        cantidad = len(existe)
    
        context['cantidad'] = cantidad
        return context
