from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.core.urlresolvers import reverse

# Create your models here.
class Cliente(models.Model):

    carnet = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('motos.crear')

class Moto(models.Model):

    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    cilindrada = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=20,decimal_places=2,default=Decimal('0.00'))
    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('motos.crear1')

class Alquiler(models.Model):

    descripcion = models.CharField(max_length=100)
    cajero = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente)
    tiempo = models.TimeField()
    alquileres = models.ManyToManyField(Moto)
    def __str__(self):
        return self.descripcion
    def get_string_motos(self):
        return ', '.join([Moto.nombre for Moto in self.alquileres.all()])
    def get_absolute_url(self):
        return reverse('motos.crear2')
