from django import forms
from .models import GPS, Limite

class GpsForm(forms.ModelForm):

    class Meta:
        model = GPS
        fields = ('descripcion', 'vehiculo', 'latitud', 'longitud')
        #help_texts = {
        #    'placa': ('Some useful help text.'),
        #}
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'vehiculo': forms.Select(attrs={'class': 'form-control'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control'}),
        }

class LimiteForm(forms.ModelForm):

    class Meta:
        model = Limite
        fields = ('descripcion','distancia_km')
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'distancia_km': forms.TextInput(attrs={'class': 'form-control'}),
        }


