from django.urls import path
from salida.views import SalidaCreateView


app_name = 'salida'
urlpatterns = [
    path('', SalidaCreateView.as_view(), name='salida_form')
]