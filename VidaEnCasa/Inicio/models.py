from django.db import models

class Registro(models.Model):
    nombre = models.CharField(max_length=20, help_text="Nombre del Usuario")
    apellido = models.CharField(max_length=20, help_text="Apellido del Usuario")
    usuario = models.CharField(max_length=20, help_text="Nombre de Usuario")
    contrasena = models.CharField(max_length=20, help_text="Contraseña del Usuario")

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.usuario})"
    
    class Meta:
        verbose_name = "Registro"
        verbose_name_plural = "Registros"
        ordering = ['nombre', 'apellido']


