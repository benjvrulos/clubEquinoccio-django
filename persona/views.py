from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from persona.forms import PersonaForm
from persona.models import Persona
from salida.models import Salida
from django.shortcuts import render, redirect

from django.urls import reverse_lazy


def PersonaCreate(request, parameter):
    if request.method == "POST":
        salida = Salida.objects.get(pk=parameter)
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save()
            salida.lista_personas.add(persona)
            return redirect('home:home')
    
    else:
        form = PersonaForm()
        context = {
            'form':form
        }

    return render(request, 'persona/persona_form.html', context)





