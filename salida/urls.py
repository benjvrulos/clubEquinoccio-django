from django.urls import path
from salida.views import (  SalidaCreateView, SalidaListView ,
                            SalidaDetailView)

app_name = 'salida'
urlpatterns = [
    path('create', SalidaCreateView.as_view(), name='salida_form'),
    path('', SalidaListView.as_view(), name='salida_list'),
    path('detail/<int:pk>',SalidaDetailView.as_view(),name='salida_detail') ,
]