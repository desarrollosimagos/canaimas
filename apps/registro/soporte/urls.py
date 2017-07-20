from django.conf.urls import patterns, include, url
from .views import ListarSoporte, RegistrarSoporte, EditarSoporte, BorrarSoporte, BuscarSolicitud
from django.contrib.auth.decorators import login_required


"""
    Urls para ingresar a la aplicacion soportes, permitiendo visualizar los registros, crearlos, editarlos y borrarlos.
"""
urlpatterns = patterns('',
                        url(r'^$', login_required(ListarSoporte.as_view(),
                                    login_url='/'), name='listar_soporte'),
                        url(r'^registrarsoporte/$', login_required(RegistrarSoporte.as_view(),
                                                    login_url='/'), name='registrar_soporte'),
                        url(r'^editarsoporte/(?P<pk>\d+)/$', login_required(EditarSoporte.as_view(),
                                                                login_url='/'), name='editar_soporte'),
                        url(r'^borrarsoporte/(?P<pk>\d+)/$', login_required(BorrarSoporte.as_view(),
                                                                login_url='/'), name='borrar_soporte'),
                        url(r'^busqueda_solicitud/$', 'apps.registro.soporte.views.BuscarSolicitud',
                            name='busqueda_solicitud'),
                    )
