from django.db import models
# Create your models here.

class Persona(models.Model):
    rut = models.CharField(max_length=15,primary_key=True)
    names = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"RUT {self.rut} NAMES {self.names}"