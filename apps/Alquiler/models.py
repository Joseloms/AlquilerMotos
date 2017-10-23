from django.db import models
from django.contrib.auth.models import User
from apps.Vehiculo.models import Vehiculo
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal
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
    tiempo = models.CharField(max_length=100)
    cajero = models.ForeignKey(User)
    cliente = models.ForeignKey(Cliente)
    vehiculo = models.ManyToManyField(Vehiculo)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    pagado = models.BooleanField(default=False)
    class Meta:
        permissions = (
            ("add_alquileres", "Puede crear Alquileres"),
        )
    def __int__(self):
        return self.cliente

    def motos(self):
        return ', '.join([Vehiculo.descripcion for Vehiculo in self.vehiculo.all()])

    def get_precio(self):
        suma = self.vehiculo.all().aggregate(Sum('tipo__precio'))
        if suma:
            return suma['tipo__precio__sum']
        return 0
