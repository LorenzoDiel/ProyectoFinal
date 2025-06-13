from django.urls import path
from . import views

app_name = 'ComidasSemanales'

urlpatterns = [
    path('', views.comidas_semanales, name='index'),
    path('crear/', views.crear_comida, name='crear_comida'),
    path('editar/', views.editar_comida, name='editar_comida'),
    path('eliminar/', views.eliminar_comida, name='eliminar_comida'),
    path('ver/', views.ver_comida, name='ver_comida'),
    path('ver/<int:dia>/', views.ver_comida_dia, name='ver_comida_dia'),
]