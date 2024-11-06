
from django.http import HttpResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
#para enviar correos
from django.contrib import messages
import random #para generar numeros random
import string
import requests

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def contacto(request):
    return render(request, 'myapp/contacto.html')

def metricas(request):
    return render(request, 'myapp/metricas.html')

def campanas(request):
    return render(request, 'myapp/campanas.html')

def base(request):
    return render(request, 'myapp/base.html')

def recuperar(request):
    return render(request, 'myapp/recuperar.html')

def perfil(request):
    return render(request, 'myapp/perfil.html')

def modificar(request):
    return render(request, 'myapp/modificar.html')

def eliminar(request):
    return render(request, 'myapp/eliminar.html')

def baterias(request):
    return render(request, 'myapp/baterias.html')

def servicios(request):
    return render(request, 'myapp/servicios.html')

def servicios_vista(request):
    return render(request, 'myapp/servicios.html')

def login_vista(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')

        if not correo or not contrasena:
            messages.error(request, 'Por favor ingrese ambos campos.')
            return redirect('index')

        try:
            print("probando")
            response = requests.post('https://apismsemail-production.up.railway.app/login', json={
                'email': correo, 
                'password': contrasena
            })
    
            if response.status_code == 200:
                cliente_data = response.json()
                request.session['cliente_id'] = cliente_data['id']  # Almacena el ID en la sesión
                print(cliente_data['id'])
                return redirect('perfil')  # Redirige a la página de perfil
            else:
                print("hola")
                mensaje = response.json().get('error', 'Error desconocido')
                print("error")
                messages.error(request, mensaje)
                return redirect('index')
        except requests.exceptions.RequestException as e:
            messages.error(request, f'Error de conexión: {e}')
            print("error")
            return redirect('index')
    return render(request, 'perfil')

def logout_vista(request):
    try:
        del request.session['cliente_id']
    except KeyError:
        pass
    return redirect('index')









#funcion form contacto