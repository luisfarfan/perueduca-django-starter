from django.db import models

from mascotas.models import Mascotas

"""
Modelo "Persona"
"""


class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=255)
    edad = models.IntegerField()
    mascotas = models.ManyToManyField(Mascotas, through='PersonaMascotas')


"""
Creo este modelo para relacionar Persona con mascotas,
asi se hace la relación de muchos a muchos, 
Una persona puede tener varias mascotas (solo como ejemplo).
"""


class PersonaMascotas(models.Model):
    persona = models.ForeignKey('Persona', on_delete=True)
    mascota = models.ForeignKey(Mascotas, on_delete=True)
    tiempo_crianza = models.IntegerField()
