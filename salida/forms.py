from dataclasses import field
from django.forms import ModelForm
from salida.models import Salida

class SalidaForm(ModelForm):
    class Meta:
        model = Salida
        fields = ['nombre_salida','fecha_inicio','fecha_termino']