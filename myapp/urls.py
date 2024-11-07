# urls.py
from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('myapp/', include('myapp.urls')),
    # ...
]

urlpatterns = [
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('contacto', views.contacto, name='contacto'),
    path('metricas', views.metricas, name='metricas'),
    path('login_vista',views.login_vista,name='login_vista'),
    path('logout_vista',views.logout_vista,name='logout_vista'),
    path('perfil',views.perfil,name='perfil'),
    path('servicios', views.servicios_vista, name='servicios'), #renderizar los items de servicios en ciclo tomando la funcion
    path('procesar-seleccion-campana', views.procesar_seleccion_campana, name='procesar_seleccion_campana'),
    path('crear_campana', views.crear_campana, name='crear_campana'),
    path('mostrar_campana', views.mostrar_campana, name='mostrar_campana')

] 
