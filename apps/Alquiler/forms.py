from django import forms
from .models import Cliente, Alquiler,User

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ('carnet', 'nombre', 'apellidos', 'telefono')
        #help_texts = {
        #    'placa': ('Some useful help text.'),
        #}
        widgets = {
            'carnet': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

TIEMPO = (
    ('15 MINUTOS','15 MINUTOS'),
    ('30 MINUTOS','30 MINUTOS'),
    ('1 HORA','1 HORAS'),
    ('2 HORAS','2 HORAS'),
)

class AlquilerForm(forms.ModelForm):

    tiempo = forms.CharField(widget=forms.Select(choices=TIEMPO, attrs={'class': 'form-control'}))

    class Meta:
        model = Alquiler
        fields = ('cajero', 'cliente','tiempo', 'hora_inicio', 'hora_fin','vehiculos')
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control','placeholder':'ingrese en formato 00:00'},format="00:00"),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control'},format="00:00:00"),
            'cajero': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'vehiculos': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }




