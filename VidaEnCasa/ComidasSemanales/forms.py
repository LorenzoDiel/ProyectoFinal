from django import forms
from django.forms import inlineformset_factory
from .models import Comida, Receta, Ingrediente, IngredienteReceta

class ComidaForm(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la comida'}),
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['instrucciones', 'tiempo_preparacion']
        widgets = {
            'instrucciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Instrucciones de la receta'}),
            'tiempo_preparacion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo en minutos'}),
        }

class IngredienteRecetaForm(forms.ModelForm):
    class Meta:
        model = IngredienteReceta
        fields = ['receta', 'ingrediente', 'cantidad']
        widgets = {
            'receta': forms.Select(attrs={'class': 'form-control'}),
            'ingrediente': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad'}),
        }

IngredienteRecetaFormSet = inlineformset_factory( 
    Receta,
    IngredienteReceta,
    form=IngredienteRecetaForm,
    extra=3,
    can_delete=False
)