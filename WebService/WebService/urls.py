"""
URL configuration for WebService project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Proyecto/urls.py (archivo principal del proyecto)
from django.urls import include, path  # Importa `include` y `path`

urlpatterns = [
    path('', include('web.urls')),  # Enlaza las rutas de `web/urls.py` en la raíz (`/`)
]