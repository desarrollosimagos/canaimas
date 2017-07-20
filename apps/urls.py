from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'^', include('apps.login.urls')),
                       url(r'^menu/', include('apps.menu.urls')),
                       )
