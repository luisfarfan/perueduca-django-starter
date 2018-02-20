from rest_framework import viewsets

from personas.models import Persona, PersonaMascotas
from personas.serializer import PersonaSerializer, PersonaMascotasSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


"""
La diferencia de este viewset, con el PersonaViewSet,
es que este traera el json anidado detallado de las mascotas, 
en cambio el otro solo traera sus primary keys.
"""
class PersonaMascotasViewSet(viewsets.ModelViewSet):
    queryset = PersonaMascotas.objects.all()
    serializer_class = PersonaMascotasSerializer
