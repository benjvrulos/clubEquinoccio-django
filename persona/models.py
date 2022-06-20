from django.db import models
# Create your models here.

class Persona(models.Model):
    rut = models.CharField(max_length=15,primary_key=True)
    nombres = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"RUT {self.rut} NAMES {self.nombres}"