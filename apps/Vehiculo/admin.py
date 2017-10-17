from django.contrib import admin
from .models import Vehiculo,Tipo,Trabajo,Mantenimiento

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','marca', 'modelo', 'activo')
    search_fields = ('descripcion',)
    list_filter = ('tipo','activo',)

class MantenimientAdmin(admin.ModelAdmin):
    list_display = ('descripcion','vehiculo','trabajos', 'fecha')
    search_fields = ('descripcion',)
    list_filter = ('trabajo','fecha',)

admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(Tipo)
admin.site.register(Trabajo)
admin.site.register(Mantenimiento,MantenimientAdmin)
