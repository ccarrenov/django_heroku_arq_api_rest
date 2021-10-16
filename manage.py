#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    PROD_SETTINGS = os.environ.get('PROD_SETTINGS')
    print('PROD_SETTINGS: {0}'.format(PROD_SETTINGS))

    if PROD_SETTINGS and PROD_SETTINGS == 'True':
        print('CARGANDO MODO PRODUCTIVO')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_heroku_arq_api_rest.settings-prod')
    else:
        print('CARGANDO MODO DESARROLLO')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_heroku_arq_api_rest.settings')

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
