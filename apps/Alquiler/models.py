from django.db import models
from django.contrib.auth.models import User
from apps.Vehiculo.models import Vehiculo
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Cliente(models.Model):
    carnet = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Alquiler(models.Model):

    fecha = models.DateTimeField(auto_now_add = timezone.now())
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cajero = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente)
    vehiculos = models.ManyToManyField(Vehiculo)
    class Meta:
        permissions = (
            ("add_alquileres", "Puede crear Alquileres"),
        )

    def __int__(self):
        return self.cliente
    def motos(self):
        return ', '.join([Vehiculo.descripcion for Vehiculo in self.vehiculos.all()])