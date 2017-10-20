from django import forms
from .models import Vehiculo, Tipo, Trabajo, Mantenimiento

class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = ('placa', 'descripcion', 'marca', 'modelo', 'cilindrada', 'tipo')
        #help_texts = {
        #   'tipo': ('debe seleccionar un tipo.'),
        #}
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'cilindrada': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }

class TipoForm(forms.ModelForm):

    class Meta:
        model = Tipo
        fields = ('descripcion','precio','km_mantenimiento')
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'km_mantenimiento': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TrabajoForm(forms.ModelForm):

    class Meta:
        model = Trabajo
        fields = ('descripcion','activo')
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MantenimientoForm(forms.ModelForm):

    class Meta:
        model = Mantenimiento
        fields = ('descripcion','vehiculo','trabajo')
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'trabajo': forms.SelectMultiple(attrs={'class': 'form-control'})
        }