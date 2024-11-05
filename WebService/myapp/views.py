
from django.http import HttpResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType
import requests
import json   #para leer json
from django.conf import settings #parte para finalizar la compra
#para enviar correos
from django.contrib import messages
import random #para generar numeros random
import string


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def contacto(request):
    return render(request, 'myapp/contacto.html')

def metricas(request):
    return render(request, 'myapp/metricas.html')

def campañas(request):
    return render(request, 'myapp/campañas.html')

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
        
        # Hacer una solicitud a la API para autenticar al usuario
        response = requests.post('http://localhost:5000/login', json={
            'correo': correo,
            'contrasena': contrasena
        })

        if response.status_code == 200:
            cliente_data = response.json()
            request.session['cliente_id'] = cliente_data['id']  # Almacena el ID en la sesión
            print(cliente_data['id'])
            return redirect('perfil')  # Redirige a la página de perfil
        else:
            mensaje = response.json().get('error', 'Error desconocido')
            return render(request, 'myapp/index.html', {'mensaje': mensaje})  # Muestra el mensaje de error

def logout_vista(request):
    try:
        del request.session['cliente_id']
    except KeyError:
        pass
    return redirect('index')









#funcion form contacto