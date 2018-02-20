from rest_framework import viewsets

from mascotas.models import Mascotas, RazaMascota
from mascotas.serializer import MascotaSerializer, RazaMascotaSerializer

"""
con este viewset ya tengo todo el REST implementado,
desde el POST, PUT, GET, DELETE, PATCH, OPTIONS
"""
class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all()
    serializer_class = MascotaSerializer


class RazaMascotaViewSet(viewsets.ModelViewSet):
    queryset = RazaMascota.objects.all()
    serializer_class = RazaMascotaSerializer


