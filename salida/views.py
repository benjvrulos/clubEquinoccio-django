from django.shortcuts import render
from django.views.generic import CreateView
from salida.models import Salida

# Create your views here.

class SalidaCreateView(CreateView):
    model = Salida
    fields = '__all__'