from django import forms
from .models import Cliente, Alquiler

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
        fields = ('cliente','cajero','tiempo','vehiculos')
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'cajero': forms.Select(attrs={'class': 'form-control'}),
            'vehiculos': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }




