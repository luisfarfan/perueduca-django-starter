from rest_framework import serializers

from mascotas.models import Mascotas, RazaMascota


class RazaMascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RazaMascota
        fields = ('__all__')


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascotas
        fields = '__all__'
