from django.urls import path
from salida.views import (  SalidaCreateView, SalidaListView ,
                            SalidaDetailView, SalidaUpdateView)

app_name = 'salida'
urlpatterns = [
    path('create', SalidaCreateView.as_view(), name='salida-form'),
    path('', SalidaListView.as_view(), name='salida-list'),
    path('detail/<int:pk>',SalidaDetailView.as_view(), name='salida-detail') ,
    path('update/<int:pk>', SalidaUpdateView.as_view(), name='salida-update'),
]