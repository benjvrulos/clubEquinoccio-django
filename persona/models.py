from django.db import models

# Create your models here.

class Persona(models.Model):
    rut = models.CharField(max_length=15,primary_key=True)
    names = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    salidas = models.ManyToManyField('salida.Salida')