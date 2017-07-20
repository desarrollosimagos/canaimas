from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from .views import login_view, logout_view, RegistrarseUsuario, EliminarUsuarios
from django.contrib.auth.decorators import login_required


"""
    Urls a la plantilla de inicio de sesion
"""
urlpatterns = patterns('',
                        url(r'^$', login_view, name='vista_login'),
                        url(r'^logout/$', logout_view, name='logout_view'),
                        url(r'^nuevo_usuario/$', login_required(RegistrarseUsuario.as_view(),
                                                    login_url='/'), name='nuevo_usuario'),
                        url(r'^eliminar_user/(?P<pk>\d+)$', login_required(EliminarUsuarios.as_view(),
                                                            login_url='/'), name='eliminar_user'),
                        url(r'^buscar_grupos/$', 'apps.login.views.buscar_grupos', name="buscar_grupos",),
                        url(r'^buscar_institucion/$', 'apps.login.views.buscar_institucion', name="buscar_institucion",),
                    )
