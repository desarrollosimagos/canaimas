from django.conf.urls import patterns, include, url
from .views import RegistrarParroquia, ListarParroquia, BorrarParroquia, BuscarAjaxMun, BuscarAjaxPar, BuscarAjaxMun2, BuscarAjaxPar2
from django.contrib.auth.decorators import login_required

"""
    Urls para ingresar a la aplicacion parroquias, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
    y ruta a metodos con ajax.
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarParroquia.as_view(template_name="topologia/parroquias/listar.html"),
                                                 login_url='/'), name='listar_parroquia'),
                       url(r'^registrarparroquia/$', 'apps.topologia.parroquias.views.RegistrarParroquia'),
                       url(r'^editarparroquia/(?P<pk>\d+)/$', 'apps.topologia.parroquias.views.ActualizarParroquia',
                           name='editar_parroquia',),
                       url(r'^borrarparroquia/(?P<pk>\d+)/$', login_required(BorrarParroquia.as_view(template_name="topologia/parroquias/borrar.html"),
                                                                             login_url='/'), name='borrar_parroquia'),
                       url(r'^busqueda_ajax/$', 'apps.topologia.parroquias.views.BuscarAjaxMun', name='busqueda_ajax'),
                       url(r'^busqueda_ajax2/$', 'apps.topologia.parroquias.views.BuscarAjaxPar', name='busqueda_ajax2'),
                       url(r'^busqueda_ajaxRe/$','apps.topologia.parroquias.views.BuscarAjaxMun2', name='listar_parroquiaRe',),
                       url(r'^busqueda_ajaxRe2/$','apps.topologia.parroquias.views.BuscarAjaxPar2', name='listar_municipiosRe',),
                       )
