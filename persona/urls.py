from unicodedata import name
from persona.views import PersonaCreate, PersonaListView
from django.urls import path


app_name = 'persona'
urlpatterns = [
    path('register-salida/<int:parameter>', PersonaCreate, name='persona-create'), 
    path('list-personas/<int:id_salida>', PersonaListView.as_view(), name='persona-list'), 

]