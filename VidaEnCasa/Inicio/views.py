from django.shortcuts import render, redirect
from .forms import RegistroForm

def inicio(request):
    error = None
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')
        try:
            registro = RegistroForm.objects.get(usuario=usuario, contrasena=contrasena)
            # Si el usuario y la contraseña son correctos, redirige a la página de inicio
            if registro.contrasena  == contrasena:
                request.session['usuario'] = registro.usuario
                return redirect('Inicio:index')
            else:
                error = "Contraseña o usuario incorrectos."
        except RegistroForm.DoesNotExist:
            error = "Usuario no encontrado."
    return render(request, 'Inicio/inicio.html', {'error': error})

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
    return render(request, 'Inicio/index.html')