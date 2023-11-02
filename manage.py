#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import logging


# DjangoInstrumentor().instrument()
# configure_azure_monitor()

def main():
    """Run administrative tasks."""

    print("JEREVOSS: manage.py main")
    from opentelemetry.instrumentation.django import DjangoInstrumentor
    from azure.monitor.opentelemetry import configure_azure_monitor
    logging.warning("main")
    # When running in Azure, the WEBSITE_HOSTNAME environment variable is automatically set to
    # the URL of the app (e.g. msdocs-python-webapp-quickstart-123.azurewebsites.net)
    settings_module = 'quickstartproject.production' if 'WEBSITE_HOSTNAME' in os.environ else 'quickstartproject.settings'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
