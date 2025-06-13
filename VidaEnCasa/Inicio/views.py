from django.shortcuts import render, redirect
from .forms import RegistroForm

def inicio(request):
    """
    Render the home page of the application.
    """
    return render(request, 'Inicio/inicio.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio:inicio') # Redirigir a la página de inicio después del registro exitoso
    else:
        form = RegistroForm()
        
    return render(request, 'Inicio/registro.html', {'form': form})

def index(request):
    """
    Render the index page of the application.
    This is typically the landing page after login or registration.
    """
    return render(request, 'Inicio/index.html')