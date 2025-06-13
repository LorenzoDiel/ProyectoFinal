from django.shortcuts import render,redirect
from .models import Comida
from django import forms


def comidas_semanales(request):
    return render(request, 'ComidasSemanales/index.html')

class ComidaForm(forms.ModelForm):
    class Meta:
        model = Comida
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nombre de la comida'}),
        }

def crear_comida(request):
    if request.method == 'POST':
        form = ComidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ComidasSemanales:index')  # Redirigir a la página de comidas semanales después de crear
    else:
        form = ComidaForm()

    return render(request, 'ComidasSemanales/crear_comida.html', {'form': form})

def editar_comida(request):
    return render(request, 'ComidasSemanales/editar_comida.html')

def eliminar_comida(request):
    return render(request, 'ComidasSemanales/eliminar_comida.html')

def ver_comida(request):
    return render(request, 'ComidasSemanales/ver_comida.html')

def ver_comida_dia(request, dia):
    return render(request, 'ComidasSemanales/ver_comida_dia.html', {'dia': dia})
