from django.conf.urls import patterns, include, url
from .views import RegistrarMunicipio, ListarMunicipio, BorrarMunicipio, ActualizarMunicipio
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion municipios, permitiendo visualizar los registros, crearlos, editarlos, eliminarlos
    y ruta a metodos con ajax.
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarMunicipio.as_view(template_name="topologia/municipios/listar.html"),
                                                 login_url='/'), name='listar_municipio'),
                       url(r'^registrarmunicipio/$', 'apps.topologia.municipios.views.RegistrarMunicipio',
                           name='registrar_municipio',),
                       url(r'^editarmunicipio/(?P<pk>\d+)/$', 'apps.topologia.municipios.views.ActualizarMunicipio',
                           name='editar_municipio',),
                       url(r'^borrarmunicipio/(?P<pk>\d+)/$', login_required(BorrarMunicipio.as_view(template_name="topologia/municipios/borrar.html"),
                                                                             login_url='/'), name='borrar_municipio'),
                       )
