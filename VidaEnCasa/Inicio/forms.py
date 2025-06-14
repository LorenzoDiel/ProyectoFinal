from django import forms
from django.forms import ModelForm
from Inicio.models import Registro

class RegistroForm(ModelForm):
    class Meta:
        model = Registro
        fields = ['nombre', 'apellido', 'usuario', 'contrasena']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'usuario': forms.TextInput(attrs={'placeholder': 'Nombre de Usuario'}),
            'contrasena': forms.PasswordInput(attrs={'placeholder': '•••••••••••••'}),
        }