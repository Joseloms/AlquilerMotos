from django import forms
from .models import Cliente, Alquiler
from ..Vehiculo.models import Vehiculo

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
    ('15','15 MINUTOS'),
    ('30','30 MINUTOS'),
    ('60','1 HORAS'),
    ('120','2 HORAS'),
)

class AlquilerForm(forms.ModelForm):
    tiempo = forms.CharField(widget=forms.Select(choices=TIEMPO, attrs={'class': 'form-control'}))
    vehiculo = forms.ModelMultipleChoiceField(queryset=Vehiculo.objects.filter(activo = True))
    class Meta:
        model = Alquiler
        fields = ( 'cliente','tiempo','vehiculo')
        widgets = {

            # 'hora_fin': forms.TimeInput(attrs={'class': 'form-control'},format="00:00:00"),
            # 'cajero': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'vehiculo': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class AlquilerCreateForm(forms.ModelForm):
    tiempo = forms.CharField(widget=forms.Select(choices=TIEMPO, attrs={'class': 'form-control'}))
    class Meta:
        model = Alquiler
        fields = ( 'cajero', 'cliente', 'hora_inicio', 'hora_fin','tiempo','vehiculo','pagado')
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'class': 'form-control'}),
            'hora_fin': forms.TimeInput(attrs={'class': 'form-control'}),
            'cajero': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'vehiculos': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

