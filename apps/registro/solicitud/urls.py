from django.conf.urls import patterns, include, url
from .views import RegistrarSolicitud, ListarSolicitud, ActualizarSolicitud, EliminarSolicitud, Remitida, Entregada
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                        url(r'^registro/$', login_required(RegistrarSolicitud.as_view(),
                                            login_url='/'), name='registrar'),
                        url(r'^listar/$', login_required(ListarSolicitud.as_view(),
                                            login_url='/'), name='lista'),
                        url(r'editar/(?P<pk>\d+)$', login_required(ActualizarSolicitud.as_view(),
                                                    login_url='/'), name='actualizar'),
                        url(r'elimina/(?P<pk>\d+)$', login_required(EliminarSolicitud.as_view(),
                                                        login_url='/'), name='eliminar'),
                        url(r'^remitida/$', login_required(Remitida.as_view(),
                                            login_url='/'), name='estatus_remitida'),
                        url(r'^entregada/$', login_required(Entregada.as_view(),
                                                login_url='/'), name='estatus_entregada'),
                    )