
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
server {
    listen 80;
    server_name localhost;  # Cambia localhost por tu dominio si aplica

    location / {
        proxy_pass http://127.0.0.1:8000;  # Redirige a Waitress
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /ruta/a/staticfiles/;  # Cambia con la ruta a tus archivos estáticos
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