from django.shortcuts import render,redirect
from .models import Comida
from django import forms
from .forms import ComidaForm, RecetaForm, IngredienteRecetaFormSet


def comidas_semanales(request):
    return render(request, 'ComidasSemanales/index.html')

def crear_comida(request):
    if request.method == 'POST':
        comida_form = ComidaForm(request.POST)
        receta_form = RecetaForm(request.POST)
        formset = IngredienteRecetaFormSet(request.POST)

        if comida_form.is_valid() and receta_form.is_valid() and formset.is_valid():
            comida = comida_form.save()
            receta = receta_form.save(commit=False)
            receta.titulo = comida
            receta.save()

            ingredientes = formset.save(commit=False)
            for ingrediente in ingredientes:
                ingrediente.receta = receta
                ingrediente.save()
            return redirect('ComidasSemanales:index')
    else:
        comida_form = ComidaForm()
        receta_form = RecetaForm()
        formset = IngredienteRecetaFormSet()

    context = {
        'comida_form': comida_form,
        'receta_form': receta_form,
        'formset': formset,
    }
    return render(request, 'ComidasSemanales/crear_comida.html', context)

def editar_comida(request):
    return render(request, 'ComidasSemanales/editar_comida.html')

def eliminar_comida(request):
    return render(request, 'ComidasSemanales/eliminar_comida.html')

def ver_comida(request):
    return render(request, 'ComidasSemanales/ver_comida.html')

def ver_comida_dia(request, dia):
    return render(request, 'ComidasSemanales/ver_comida_dia.html', {'dia': dia})
