from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
from salida.models import Salida


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salidas'] = Salida.objects.all()
        return context
    