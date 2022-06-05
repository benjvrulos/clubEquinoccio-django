from django.db import models
from persona.models import Persona

# Create your models here.
class Salida(models.Model):
    nombre_salida = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    hora = models.DateTimeField()
    personas = models.ManyToManyField('persona.Persona')


