from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'tipo_educacion/', include('apps.configuracion.tipo_educacion.urls')),
    url(r'grados/', include('apps.configuracion.grados.urls')),
    url(r'modelos/', include('apps.configuracion.modelos.urls')),
    url(r'^instituciones/', include('apps.configuracion.instituciones.urls')),
)