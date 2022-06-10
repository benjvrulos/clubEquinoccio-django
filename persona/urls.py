from persona.views import PersonaCreateView
from django.urls import path


app_name = 'persona'
urlpatterns = [
    path('', PersonaCreateView.as_view())
]