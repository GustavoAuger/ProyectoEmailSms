
# Proyecto Email SMS - Frontend con Django, Waitress y Nginx

Este proyecto contiene el frontend de la plataforma de envíos de email y SMS, desarrollada con Django. Se implementa con el servidor WSGI **Waitress** para manejar el tráfico en el servidor web y **Nginx** como balanceador de carga y servidor de archivos estáticos.

**Repositorio en GitHub:** [ProyectoEmailSms en la rama webserver2.0](https://github.com/GustavoAuger/ProyectoEmailSms)

## Tabla de Contenidos
1. [Requisitos previos](#requisitos-previos)
2. [Instrucciones de configuración](#instrucciones-de-configuración)
3. [Ejecución de la aplicación](#ejecución-de-la-aplicación)
4. [Configuración de Nginx](#configuración-de-nginx)
5. [Solución de problemas](#solución-de-problemas)

## Requisitos previos
Asegúrate de tener instalados los siguientes programas:
- **Python 3.x**: para ejecutar Django.
- **Pip**: para instalar las dependencias del proyecto.
- **Virtualenv**: para crear un entorno virtual aislado.
- **Nginx**: como balanceador de carga y servidor de archivos estáticos.
- **Waitress**: servidor WSGI para servir la aplicación de Django.

## Instrucciones de configuración

1. **Clona el repositorio**

   git clone https://github.com/GustavoAuger/ProyectoEmailSms.git
   git checkout webserver2.0

2. **Crea un entorno virtual usando virtualenv:**

    python -m venv myvenv
    Activa el entorno virtual:

- Windows:

myvenv\Scripts\activate

- Mac/Linux:

source myvenv/bin/activate

3. **Instala las dependencias con el entorno virtual activo, instala las dependencias:**

pip install -r requirements.txt
Ejecución de la aplicación
Ejecuta Django con Waitress

4. **Desde la raíz del proyecto, inicia Waitress:**
waitress-serve --port=8000 myapp.wsgi:application

Este comando iniciará el servidor Waitress en el puerto 8000. Asegúrate de que la ruta myapp.wsgi:application coincida con la configuración WSGI_APPLICATION en settings.py.

5. **Verifica el servidor**

Abre un navegador y dirígete a http://localhost:8000 para verificar que la aplicación esté en funcionamiento.

## Configuración de Nginx

Nginx actuará como un proxy inverso que distribuye las solicitudes hacia Waitress.

1. **Crea un nuevo archivo de configuración en Nginx**

- Linux:
sudo nano /etc/nginx/sites-available/proyectoemailsms

- Windows: 
Localiza nginx.conf en el directorio de instalación o crea un archivo .conf en la carpeta conf.

Añade la configuración nginx

2. **Copiar y pega código:**

-Definir el grupo de servidores Waitress para balanceo de carga:

upstream django_servers {
    # Método de balanceo de carga (least_conn: menos conexiones activas)
    least_conn;
    server 127.0.0.1:8000;  # Primera instancia de Waitress
    server 127.0.0.1:8001;  # Segunda instancia de Waitress
    # Añade más servidores si es necesario
}

-PREVIAMENTE se debe ejecutar las instnacias de Wairtress en la terminal:

start waitress-serve --listen=127.0.0.1:8001 myapp:app
start waitress-serve --listen=127.0.0.1:8002 myapp:app
... # Añade más servidores si es necesario

## Configuración del servidor Nginx

server {
    listen 80;  # Puerto de escucha en HTTP
    server_name midominio.com;  # Cambia a tu dominio o IP

    # Configuración de caché
    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=cache_django:10m max_size=1g inactive=60m use_temp_path=off;

    # Configuración de proxy inverso y caché
    location / {
        # Balanceo de carga a través del grupo django_servers
        proxy_pass http://django_servers;

        # Configuración de caché
        proxy_cache cache_django;           # Zona de caché
        proxy_cache_valid 200 1h;           # Cacheo de 1 hora para respuestas 200 (éxito)
        proxy_cache_use_stale error timeout updating;
        proxy_cache_bypass $http_cache_control;

        # Headers para el proxy inverso
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Configuración para archivos estáticos de Django
    location /static/ {
        alias /ruta/a/static/files;  # Cambia por la ruta real a los archivos estáticos
    }
}


3. **Cambia /ruta/a/staticfiles/ por la ruta real de tus archivos estáticos en Django. Recolecta previamente estos archivos con python manage.py collectstatic.**

4. **Habilita la configuración:**

- Linux:
sudo ln -s /etc/nginx/sites-available/proyectoemailsms /etc/nginx/sites-enabled
sudo systemctl restart nginx

- Windows: Reinicia Nginx desde la línea de comandos o el administrador de servicios.

## Solución de problemas

Errores en Nginx: Si Nginx no se inicia, revisa las rutas en la configuración y los registros de errores.
Archivos estáticos no se cargan: Asegúrate de haber ejecutado collectstatic y de que la ruta en Nginx sea la correcta.
Problemas con el entorno virtual: Si falla la activación, verifica la ruta y asegúrate de que virtualenv esté instalado.