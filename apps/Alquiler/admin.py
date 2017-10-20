from django.contrib import admin
from .models import Cliente, Alquiler
# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('carnet','nombre','apellidos','telefono')
    search_fields = ('apellidos',)

class AlquilerAdmin(admin.ModelAdmin):
    list_display = ('cliente','cajero','fecha','motos','total','hora_inicio','hora_fin')
    search_fields = ('cliente',)

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Alquiler,AlquilerAdmin)
