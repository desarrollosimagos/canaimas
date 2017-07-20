from django.conf.urls import patterns, include, url
from .views import Inicio
from django.contrib.auth.decorators import login_required


"""
    Urls a la plantilla base de la aplicacion
"""
urlpatterns = patterns('',
                       url(r'^$', login_required(Inicio.as_view(template_name="inicio.html"), login_url='/')),
                       url(r'^topologia/',  include('apps.topologia.urls')),
                       url(r'^configuraciones/',  include('apps.configuracion.urls')),
                       url(r'^reportes/', include('apps.reportes.urls')),
                       url(r'^registros/', include('apps.registro.urls')),
                       )
