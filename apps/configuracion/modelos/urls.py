from django.conf.urls import patterns, include, url
from .views import RegistrarModelos, ListarModelos, EditarModelos, EliminarModelos
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                        url(r'^registro/$', login_required(RegistrarModelos.as_view(),
                                            login_url='/'), name='registro_modelos'),
                        url(r'^listar/$', login_required(ListarModelos.as_view(),
                                            login_url='/'), name='listar_modelos'),
                        url(r'editar/(?P<pk>\d+)$', login_required(EditarModelos.as_view(),
                                                    login_url='/'), name='editar_modelos'),
                        url(r'eliminar/(?P<pk>\d+)$', login_required(EliminarModelos.as_view(),
                                                        login_url='/'), name='eliminar_modelos'),
                    )