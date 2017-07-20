from django.conf.urls import patterns, include, url
from .views import RegistrarGrados, ListarGrados, EditarGrados, EliminarGrados, BuscarAjaxGrados
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                        url(r'^registro/$', login_required(RegistrarGrados.as_view(),
                                            login_url='/'), name='registro_grados'),
                        url(r'^listar/$', login_required(ListarGrados.as_view(),
                                            login_url='/'), name='listar_grados'),
                        url(r'editar/(?P<pk>\d+)$', login_required(EditarGrados.as_view(),
                                                    login_url='/'), name='editar_grados'),
                        url(r'eliminar/(?P<pk>\d+)$', login_required(EliminarGrados.as_view(),
                                                    login_url='/'), name='eliminar_grados'),
                        url(r'grados_ajax/$', 'apps.configuracion.grados.views.BuscarAjaxGrados',
                            name='grados_ajax'),
                    )