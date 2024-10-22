from django.contrib import admin
from apps.calendario.models import Calendario

# Register your models here.
@admin.register(Calendario)
class CalendarioAdmin (admin.ModelAdmin):
    list_display = ["profesional", "fecha_disponibilidad"]
    


