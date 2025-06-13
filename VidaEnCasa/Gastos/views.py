from django.shortcuts import render

def gastos(request):
    """
    Render the expenses page.
    This page displays the expenses incurred by the user.
    """
    return render(request, 'Gastos/index.html')

# Create your views here.
