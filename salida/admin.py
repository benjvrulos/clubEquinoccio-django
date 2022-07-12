from django.contrib import admin
from salida.models import Salida

class SalidaAdmin(admin.ModelAdmin):
    list_display = ('nombre_salida','fecha_inicio','fecha_termino','modified_date','created_date')


admin.site.register(Salida,SalidaAdmin)