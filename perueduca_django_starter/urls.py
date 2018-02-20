"""perueduca_django_starter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from mascotas.views import MascotaViewSet, RazaMascotaViewSet
from personas.views import PersonaViewSet, PersonaMascotasViewSet

""" 
DjangoRestFramework, tiene una interfaz amigable
para mostrar sus API REST, con DefaultRouter
podemos acceder a esta interfaz,
entren a localhost:8000, y veran como pueden probar sus 
"POST, PUT, DELETE, GET, PATCH, OPTIONS"
"""
router = routers.DefaultRouter()
router.register(r'personas', PersonaViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'razamascotas', RazaMascotaViewSet)
router.register(r'personasmascotas', PersonaMascotasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
