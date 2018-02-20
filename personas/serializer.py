from rest_framework import serializers

from mascotas.serializer import MascotaSerializer
from personas.models import Persona, PersonaMascotas


class PersonaSerializer(serializers.ModelSerializer):
    """
        le pongo "many=True" por que son varias mascotas, entonces
        cuando me muestra la información, me lo dara en un json anidado.
    """
    mascotas = MascotaSerializer(many=True, read_only=True)

    class Meta:
        model = Persona
        fields = ('__all__')


class PersonaMascotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaMascotas
        fields = '__all__'
