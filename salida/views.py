from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from salida.models import Salida

# Create your views here.

class SalidaCreateView(CreateView):
    model = Salida
    fields = '__all__'
    success_url = reverse_lazy('home:home')


class SalidaListView(ListView):
    model = Salida
    context_object_name = 'salida_list'