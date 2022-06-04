from django.db import models

# Create your models here.
class Salida(models.Model):
    nombre_salida = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    hora = models.DateTimeField()


