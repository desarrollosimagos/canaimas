from django.conf.urls import patterns, include, url
from .views import RegistrarEstado, ListarEstado, EditarEstado, BorrarEstado
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion estados, permitiendo visualizar los registros, crearlos, editarlos y borrarlos.
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarEstado.as_view(template_name="topologia/estados/listar.html"),
                                                 login_url='/'), name='listar_estado'),
                       url(r'^registrarestado/$', login_required(RegistrarEstado.as_view(template_name="topologia/estados/estados.html"),
                                                 login_url='/'), name='registrar_estado'),
                       url(r'^editarestado/(?P<pk>\d+)/$', login_required(EditarEstado.as_view(template_name="topologia/estados/modificar.html"),
                                                 login_url='/'), name='editar_estado'),
                       url(r'^borrarestado/(?P<pk>\d+)/$', login_required(BorrarEstado.as_view(template_name="topologia/estados/borrar.html"),
                                                 login_url='/'), name='borrar_estado'),
                       )
