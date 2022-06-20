from unicodedata import name
from persona.views import PersonaCreate
from django.urls import path


app_name = 'persona'
urlpatterns = [
    path('register-salida/<int:parameter>', PersonaCreate, name='persona-create'),

]