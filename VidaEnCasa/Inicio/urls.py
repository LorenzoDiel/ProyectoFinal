from django.urls import path
from . import views

app_name = 'Inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('index/', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
]