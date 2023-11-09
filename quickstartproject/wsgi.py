"""
WSGI config for quickstartproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from importlib_metadata import entry_points
for entry_point in entry_points(group="opentelemetry_traces_exporter"):
    print("JEREVOSS entry_point.name: %s" % entry_point.name)
for entry_point in entry_points(group="opentelemetry_logs_exporter"):
    print("JEREVOSS entry_point.name: %s" % entry_point.name)

# settings_module = 'quickstartproject.production' if 'WEBSITE_HOSTNAME' in os.environ else 'quickstartproject.settings'
settings_module = 'quickstartproject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)


from os import environ
import logging

logger = logging.getLogger(__name__)

logger.warning("JEREVOSS: PYTHONPATH: %s" % environ["PYTHONPATH"])
from quickstartproject import settings
logger.warning("JEREVOSS: settings: %s" % settings)
from quickstartproject.settings import ALLOWED_HOSTS
logger.warning("JEREVOSS: ALLOWED_HOSTS: %s" % ALLOWED_HOSTS)

application = get_wsgi_application()


from django.conf import settings
logger.warning("JEREVOSS: settings.DEBUG: %s" % settings.DEBUG)
logger.warning("JEREVOSS: settings.ALLOWED_HOSTS: %s" % settings.ALLOWED_HOSTS)
settings_middleware = getattr(settings, "MIDDLEWARE", [])
logger.warning("JEREVOSS: wsgi settings.MIDDLEWARE: %s" % settings_middleware)
