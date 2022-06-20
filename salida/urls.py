from django.urls import path
from salida.views import (  SalidaCreateView,SalidaDeleteView, 
                            SalidaListView,SalidaDetailView, SalidaPersonaListView, 
                            SalidaUpdateView)

app_name = 'salida'
urlpatterns = [
    path('', SalidaListView.as_view(), name='salida-list'),
    path('create/', SalidaCreateView.as_view(), name='salida-form'),
    path('detail/<int:pk>', SalidaDetailView.as_view(), name='salida-detail') ,
    path('update/<int:pk>', SalidaUpdateView.as_view(), name='salida-update'),
    path('delete/<int:pk>', SalidaDeleteView.as_view(), name='salida-delete'),
    path('<int:id_salida>/lista-personas', SalidaPersonaListView.as_view(), name='salida_list-personas'),
]