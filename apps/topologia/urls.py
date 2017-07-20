from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import Topologia

urlpatterns = patterns('',
                       url(r'^$', login_required(Topologia.as_view(), login_url='/')),
                       url(r'^estados/', include('apps.topologia.estados.urls')),
                       url(r'^municipios/', include('apps.topologia.municipios.urls')),
                       url(r'^parroquias/', include('apps.topologia.parroquias.urls')),
                       )
