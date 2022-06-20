from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from persona.forms import PersonaForm
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
    
    form = PersonaForm()
    context = {
        'form':form
        }

    return render(request, 'persona/persona_form.html', context)


# class PersonaListView(ListView):
#     template_name = 'persona/persona_list.html'
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(id=self.kwargs['id_salida'])








