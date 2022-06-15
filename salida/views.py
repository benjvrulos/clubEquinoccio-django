from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse_lazy
from salida.models import Salida

class SalidaCreateView(CreateView):
    # model_form.html --> salida_form.html
    model = Salida
    fields = '__all__'
    success_url = reverse_lazy('home:home')


class SalidaListView(ListView):

    ## model_list.html --> salida_list.html
    model = Salida
    context_object_name = 'salida_list'

class SalidaDetailView(DetailView):

    # model_detial.html --> salida_detail.html
    model = Salida
    context_object_name = 'my_salida'

class SalidaUpdateView(UpdateView):
    # model_form.html like CreteView
    model = Salida
    fields = '__all__'
    success_url = reverse_lazy('salida:salida-list')