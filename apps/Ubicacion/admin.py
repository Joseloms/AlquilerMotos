from django.contrib import admin
from .models import GPS, Limite
# Register your models here.

class GpsAdmin(admin.ModelAdmin):
    list_display = ('descripcion','vehiculo','latitud','longitud')
    search_fields = ('descripcion',)

class LimiteAdmin(admin.ModelAdmin):
    list_display = ('descripcion','distancia_km')
    search_fields = ('descripcion',)

admin.site.register(GPS,GpsAdmin)
admin.site.register(Limite,LimiteAdmin)
