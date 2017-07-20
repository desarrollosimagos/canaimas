from django.conf.urls import patterns, include, url
from .views import ListarGrafica, PdfGeneral
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarGrafica.as_view(),login_url='/'), name='grafica'),
                       url(r'^soportesgeneral/$', login_required(PdfGeneral.as_view(),login_url='/')),
                       )
