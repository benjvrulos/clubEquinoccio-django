from ast import arg
from audioop import reverse
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from persona.models import Persona

# Create your models here.
class Salida(models.Model):
    nombre_salida = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    foto_salida = models.ImageField(upload_to='salida',blank=True)
    # hora = models.DateTimeField()

    def get_absolute_url(self):
        return reverse('salida-detail',args= [str(self.id)])
        
    
    def __str__(self):
        return f'Nombre de salida: {self.nombre_salida}'