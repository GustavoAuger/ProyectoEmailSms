#!/usr/bin/env python
import os
import sys
from django.core.wsgi import get_wsgi_application

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebService.settings')
    try:
        from django.core.management import execute_from_command_line
        # Ejecutar migraciones automáticamente en Vercel
        if os.getenv('ENV') == 'PRODUCTION':
            execute_from_command_line(['manage.py', 'migrate'])
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

# Exponer la aplicación WSGI para Vercel
application = get_wsgi_application()