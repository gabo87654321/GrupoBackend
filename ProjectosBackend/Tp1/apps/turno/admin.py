from django.contrib import admin
from apps.turno.models import Turno
# Register your models here.
@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display=["usuario", "profesional", "servicio", "fecha_hora"]
