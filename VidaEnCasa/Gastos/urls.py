from django.urls import path
from . import views

app_name = 'Gastos'

urlpatterns = [
    path('', views.gastos, name='index'), 
]