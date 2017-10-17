
from django.db import models
from decimal import Decimal
from django.utils import timezone

# Create your models here.

class Tipo(models.Model):

    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))
    km_mantenimiento = models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))
    def __str__(self):
        return self.descripcion


class Vehiculo(models.Model):

    placa = models.CharField(primary_key=True,max_length=100)
    descripcion = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cilindrada = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo)
    km_recorrido = models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.descripcion


class Trabajo(models.Model):

    descripcion = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.descripcion


class Mantenimiento(models.Model):

    descripcion = models.CharField(max_length=100)
    trabajo = models.ManyToManyField(Trabajo)
    vehiculo = models.ForeignKey(Vehiculo)
    fecha = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.descripcion

    def trabajos(self):
        return ', '.join([Trabajo.descripcion for Trabajo in self.trabajo.all()])

