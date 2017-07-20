from django.conf.urls import patterns, include, url
from .views import RegistrarTipoEducacion, ListarTipoEducacion, EditarTipoEducacion, EliminarTipoEducacion
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
                        url(r'^registro/$', login_required(RegistrarTipoEducacion.as_view(),
                                            login_url='/'), name='registro_tipo_educacion'),
                        url(r'^listar/$', login_required(ListarTipoEducacion.as_view(),
                                            login_url='/'), name='listar_tipo_educacion'),
                        url(r'editar/(?P<pk>\d+)$', login_required(EditarTipoEducacion.as_view(),
                                                    login_url='/'), name='editar_tipo_educacion'),
                        url(r'eliminar/(?P<pk>\d+)$', login_required(EliminarTipoEducacion.as_view(),
                                                        login_url='/'), name='eliminar_tipo_educacion'),
                    )