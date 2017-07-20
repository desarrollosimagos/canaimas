from django.views.generic import CreateView, ListView, UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Parroquia
from apps.topologia.estados.models import Estado
from apps.topologia.municipios.models import Municipio
from .forms import ParroquiaForm
from django.core import serializers
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def RegistrarParroquia(request):
    """ Vista basada en Metodos o funciones: (`Registrar`)."""
    list_e = Estado.objects.all()
    list_m = Municipio.objects.all()
    if request.method == 'POST':
        bandera = request.POST.get('bandera')
        cod_parroquia = request.POST.get('cod_parroquia')
        estado = request.POST.get('estado')
        municipio = request.POST.get('municipio')
        parroquia = request.POST.get('parroquia')
        existe_t = Parroquia.objects.filter(cod_parroquia=cod_parroquia, estado=estado, municipio=municipio, parroquia=parroquia).exists()
        existe_cm = Parroquia.objects.filter(cod_parroquia=cod_parroquia, estado=estado, municipio=municipio).exists()
        existe_n = Parroquia.objects.filter(estado=estado, municipio=municipio, parroquia=parroquia).exists()
        existe_c = Parroquia.objects.filter(cod_parroquia=cod_parroquia, estado=estado).exists()
        if existe_t and bandera == 'true':
            return HttpResponse('existe_t')
        elif existe_cm and bandera == 'true':
            return HttpResponse('existe_cm')
        elif existe_n and bandera == 'true':
            return HttpResponse('existe_n')
        elif existe_c and bandera == 'true':
            return HttpResponse('existe_c')
        else:
            form_reg_par = ParroquiaForm(request.POST, request.FILES)
            if form_reg_par.is_valid():
                new_reg_par = form_reg_par.save(commit=False)
                new_reg_par.user = request.user.username
                new_reg_par.save()
            return HttpResponseRedirect('/menu/topologia/parroquias/')
    else:
        form_reg_par = ParroquiaForm()
    ctx = {'form_reg_par': form_reg_par, 'list_e': list_e, 'list_m': list_m}  # ctx = Contexto
    return render_to_response('topologia/parroquias/parroquias.html',
                              ctx, context_instance=RequestContext(request))


class ListarParroquia(ListView):
    """ Vista basada en clase: (`Listar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Parroquia
    template_name = 'topologia/parroquias/listar.html'
    context_object_name = "listar_parroquia"


    def get_context_data(self, **kwargs):
        # Llamamos ala implementacion para traer un primer context
        context = super(ListarParroquia, self).get_context_data(**kwargs)
        # Agregamos un QuerySet
        context['list_m'] = Municipio.objects.all()
        return context


@login_required(login_url='/')
def ActualizarParroquia(request, pk):
    """ Vista basada en Metodos o funciones: (`Modificar`)."""
    list_e = Estado.objects.all()
    list_m = Municipio.objects.all()
    obj_reg_parr = Parroquia.objects.get(id=pk)
    if request.method == 'POST':
        form_reg_parr = ParroquiaForm(request.POST, request.FILES, instance=obj_reg_parr)
        if form_reg_parr.is_valid():
            edit_reg_parr = form_reg_parr.save(commit=False)
            edit_reg_parr.save()
            return HttpResponseRedirect('/menu/topologia/parroquias/')
    else:
        form_reg_parr = ParroquiaForm(instance=obj_reg_parr)
    ctx = {'form_reg_parr': form_reg_parr, 'obj_reg_parr': obj_reg_parr, 'list_e': list_e, 'list_m': list_m}
    return render_to_response('topologia/parroquias/modificar.html',
                              ctx, context_instance=RequestContext(request))


class BorrarParroquia(DeleteView):
    """ Vista basada en clase: (`Borrar`)

    :param template_name: ruta de la plantilla
    :param model: Modelo al cual se hace referencia
    :param success_url: nombre de la ruta a la cual se redireccionara la aplicacion una vez eliminado el registro
                            satisfactoriamente
    :param context_object_name: nombre del objeto que contiene esta vista
    """
    model = Parroquia
    template_name = 'topologia/parroquias/borrar.html'
    context_object_name = "borrar_parroquia"
    success_url = reverse_lazy("listar_parroquia")

    # def get_context_data(self, **kwargs):
    #     context = super(BorrarParroquia, self).get_context_data(**kwargs)
    #     pk_par = self.kwargs['pk']
    #     parroquia = Parroquia.objects.all()
    #     id_par = parroquia.filter(pk=pk_par).values('cod_parroquia')
    #     id_mun = parroquia.filter(pk=pk_par).values('municipio')
    #     id_est = parroquia.filter(pk=pk_par).values('estado_id')
    #     
    #     sec = Sector.objects.all()
    #     # cen = Centros.objects.all()
    #     existe_s = sec.filter(parroquia=id_par, municipio=id_mun, estado_id=id_est)
    #     # existe_c = cen.filter(parroquia=id_par, municipio=id_mun, estado_id=id_est)
    #     cantidad_s = len(existe_s)
    #     # cantidad_c = len(existe_c)
    #     
    #     context['cantidad_s'] = cantidad_s
    #     # context['cantidad_c'] = cantidad_c
    #     return context

#=====================================================================================
                            # Metodo BuscarAjaxParr json
#=====================================================================================


def BuscarAjaxMun(request):
    """ Metodo que en base al estado seleccionado se filtran los municipios pertenecientes a el y los datos
    serializados son validados en el metodo ajax para el ubicado en /static/js/validaciones.js
    """
    id_est = request.GET['id']
    municipios = Municipio.objects.filter(estado_id=id_est)
    data = serializers.serialize('json', municipios, fields=('id', 'municipio'))

    return HttpResponse(data, content_type='application/json')


def BuscarAjaxPar(request):
    """ Metodo que en base al estado seleccionado y a su correspondiente municipio filtra las parroquias, los datos son
    serializados y validados en el metodo ajax para el ubicado en /static/js/validaciones.js
    """
    id_est = request.GET['id_est']
    id_mun = request.GET['id_mun']
    parroquias = Parroquia.objects.filter(estado_id=id_est, municipio=id_mun)
    data = serializers.serialize('json', parroquias, fields=('pk', 'parroquia'))

    return HttpResponse(data, content_type='application/json')

#=====================================================================================
                            # Metodo BuscarAjaxParr json para representante
#=====================================================================================
def BuscarAjaxMun2(request):
    
    id_est = request.GET['id']
    municipios = Municipio.objects.filter(estado_id=id_est)
    data = serializers.serialize('json',municipios,
                                       fields=('cod_municipio','municipio'))
    #print "LISTA DE MUNICIPIOS: ",data
    
    return HttpResponse(data, content_type='application/json')


#@login_required(login_url='/iniciar/login/')
def BuscarAjaxPar2(request):
   
    id_est = request.GET['id_est']
    id_mun = request.GET['id_mun']
    parroquias = Parroquia.objects.filter(estado_id=id_est,municipio=id_mun)
    data = serializers.serialize('json',parroquias,
                                       fields=('cod_parroquia','parroquia'))
    return HttpResponse(data, content_type='application/json') 