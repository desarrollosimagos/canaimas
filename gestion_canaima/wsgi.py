"""
WSGI config for gestion_canaima project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/administrador/django/canaimas/gestion_canaima')
os.environ['DJANGO_SETTINGS_MODULE'] = 'gestion_canaima.settings'
#os.environ['DJANGO_SETTINGS_MODULE'] = 'actividades.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

