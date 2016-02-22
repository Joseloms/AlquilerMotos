from django.contrib import admin
from .models import Alquiler,Moto,Cliente

class AlquilerAdmin(admin.ModelAdmin):

    list_display = ('descripcion', 'cajero', 'cliente', 'tiempo','get_string_motos')
    filter_horizontal = ('alquileres',)

admin.site.register(Alquiler,AlquilerAdmin)
admin.site.register(Moto)
admin.site.register(Cliente)