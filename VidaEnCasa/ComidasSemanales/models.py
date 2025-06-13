from django.db import models

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.unidad}"
    
class Comida(models.Model):
    nombre = models.CharField(max_length=100)

class Receta(models.Model):
    titulo = models.ForeignKey(Comida, on_delete=models.CASCADE, related_name='recetas', default=None)
    instrucciones = models.TextField()
    tiempo_preparacion = models.IntegerField(help_text="Tiempo en minutos")

    def __str__(self):
        return f"Receta de {self.titulo.nombre} - {self.tiempo_preparacion} min"

class IngredienteReceta(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='ingredientes_en_receta')
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=6, decimal_places=2, help_text="Cantidad del ingrediente")

    def __str__(self):
        return f"{self.cantidad} {self.ingrediente.unidad} de {self.ingrediente.nombre} para {self.receta.titulo}"
    
class ComidaSemanal(models.Model):
    dia = models.CharField(max_length=20)
    comida = models.ForeignKey(Comida, on_delete=models.CASCADE, related_name='comidas_semanales')
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='comidas_semanales')

    def __str__(self):
        return f"{self.dia}: {self.comida.nombre} - {self.receta.nombre}"
