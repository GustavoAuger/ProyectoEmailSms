#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.wsgi import get_wsgi_application
import django
from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tu_proyecto.settings')
    django.setup()
    try:
        # Ejecuta las migraciones automáticamente
        execute_from_command_line(['manage.py', 'migrate'])
    except Exception as exc:
        print(f"Error al ejecutar migraciones: {exc}")
    # Ejecuta el servidor
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

app = get_wsgi_application()