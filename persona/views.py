from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from persona.models import Persona
from django.urls import reverse_lazy


class PersonaCreateView(CreateView):
    model = Persona
    fields = '__all__'
    success_url = reverse_lazy('home:home')



