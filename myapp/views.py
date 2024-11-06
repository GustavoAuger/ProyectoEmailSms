
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
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def contacto(request):
    return render(request, 'myapp/contacto.html')

def metricas(request):
    return render(request, 'myapp/metricas.html')

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
#LLAMA A LA API PARA ENVIAR CAMPAÑA 
def procesar_seleccion_campana(request):
    if request.method == "POST":
        campana_id = request.POST.get("campana_id")
        if campana_id:
            # Datos que se envían a la API externa
            data = {"campana_id": campana_id}
            
            try:
                # Realizar la solicitud POST a la API externa
                response = requests.post("http://localhost:5000/add_campaigns", json=data)
                
                # Verificar si la solicitud fue exitosa
                if response.status_code == 200:
                    return JsonResponse({"mensaje": f"Campaña seleccionada: {campana_id}"})
                else:
                    return JsonResponse({"error": "Error al enviar los datos a la API externa"}, status=500)
            except requests.exceptions.RequestException as e:
                # Capturar errores en caso de que la API no responda o no esté disponible
                return JsonResponse({"error": f"Error de conexión: {str(e)}"}, status=500)
    
    return JsonResponse({"error": "No se seleccionó ninguna campaña"}, status=400)

#MOSTRAR CAMPANA

def mostrar_campana(request):
    # Llama a la API para obtener las campañas
    user_id = 1
    canal = "email"
    url = f'https://apismsemail-production.up.railway.app/list_campaigns_by_id?id={user_id}&canal={canal}'
    
    # Realizar la solicitud GET a la API con los parámetros
    response = requests.get(url)
    if response.status_code == 200:
        campanas = response.json()  # Aquí obtienes las campañas desde la API
    else:
        campanas = []  # En caso de error, mostrar una lista vacía
    
    # Renderiza la plantilla 'campana.html' con las campañas
    return render(request, 'campana.html', {'campanas': campanas})

#CREAR CAMPANA

def crear_campana(request):
    if request.method == "POST":
        tipo_campana = request.POST.get("tipo_campana")
        descripcion = request.POST.get("descripcion")
        
        if tipo_campana and descripcion:
            # Datos que se enviarán a la API
            data = {
                "tipo_campana": tipo_campana,
                "descripcion": descripcion
            }
            
            try:
                # Realizar la solicitud POST a la API externa
                response = requests.post("http://localhost:5000/add_campaigns", json=data)
                
                # Verificar si la solicitud fue exitosa
                if response.status_code == 200:
                    return JsonResponse({"mensaje": "Campaña creada exitosamente"})
                else:
                    return JsonResponse({"error": "Error al enviar los datos a la API externa"}, status=500)
            except requests.exceptions.RequestException as e:
                # Capturar errores en caso de que la API no responda o no esté disponible
                return JsonResponse({"error": f"Error de conexión: {str(e)}"}, status=500)
    
    return JsonResponse({"error": "Datos incompletos para crear campaña"}, status=400)
