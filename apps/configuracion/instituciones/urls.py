from django.conf.urls import patterns, include, url
from .views import ListarInstitucion, RegistrarInstitucion, EditarInstitucion, BorrarInstitucion
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion institucions, permitiendo visualizar los registros, crearlos, editarlos y borrarlos.
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(ListarInstitucion.as_view(),
                                                 login_url='/'), name='listar_institucion'),
                       url(r'^registrarinstitucion/$', login_required(RegistrarInstitucion.as_view(),
                                                 login_url='/'), name='registrar_institucion'),
                       url(r'^editarinstitucion/(?P<pk>\d+)/$', login_required(EditarInstitucion.as_view(),
                                                 login_url='/'), name='editar_institucion'),
                       url(r'^borrarinstitucion/(?P<pk>\d+)/$', login_required(BorrarInstitucion.as_view(),
                                                 login_url='/'), name='borrar_institucion'),
                       )
