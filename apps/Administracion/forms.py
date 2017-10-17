from django.contrib.auth.models import User, Group
from django import forms


class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'permissions': forms.SelectMultiple(attrs={'class': 'form-control'})
        }
        labels = {
            'name': 'Nombre del Grupo',
            'permissions': 'Permisos'
        }

class UserForm(forms.ModelForm):
    class Meta:
          model = User
          fields = [
              'first_name',
              'last_name',
              'username',
              'password',
              'email',
          ]
          widgets = {
              'username': forms.TextInput(attrs={'class': 'form-control'}),
              'first_name': forms.TextInput(attrs={'class': 'form-control'}),
              'last_name': forms.TextInput(attrs={'class': 'form-control'}),
              'email': forms.EmailInput(attrs={'class': 'form-control'}),
              'password': forms.PasswordInput(attrs={'class': 'form-control'}),
          }


