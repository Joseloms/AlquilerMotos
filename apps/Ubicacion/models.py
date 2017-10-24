#encoding:utf-8
# Create your models here.

from django.db import models
from ..Vehiculo.models import Vehiculo
from decimal import Decimal

class GPS(models.Model):

    descripcion = models.CharField(max_length=100)
    vehiculo = models.OneToOneField(Vehiculo)
    latitud = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    longitud = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return self.descripcion

class Limite(models.Model):

    descripcion = models.CharField(max_length=100)
    distancia_km = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return self.descripcion

