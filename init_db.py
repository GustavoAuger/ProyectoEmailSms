# init_db.py
from django.core.management import call_command

def run_migrations():
    print("Ejecutando migraciones de base de datos...")
    call_command('migrate')

if __name__ == "__main__":
    run_migrations()