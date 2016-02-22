from django import forms
from .models import Cliente, Moto, Alquiler

class ClienteCreateForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('carnet', 'nombre')
        widgets = {
            'carnet': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'})
        }

class MotoCreateForm(forms.ModelForm):

    class Meta:
        model = Moto	
        fields = ('nombre', 'marca', 'cilindrada', 'precio')

class AlquilerCreateForm(forms.ModelForm):

    class Meta:
        model = Alquiler
        fields = ('descripcion', 'cajero', 'cliente', 'tiempo', 'alquileres')