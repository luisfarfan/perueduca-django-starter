from django.db import models

# Create your models here.

class Mascotas(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    raza = models.ForeignKey('RazaMascota', on_delete=True)


class RazaMascota(models.Model):
    descripcion = models.CharField(max_length=255)