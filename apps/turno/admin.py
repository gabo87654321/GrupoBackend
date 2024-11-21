from django.contrib import admin
from .models import Turno

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'servicio', 'profesional', 'fecha', 'hora', 'estado')
    search_fields = ('usuario__username', 'profesional__nombre', 'servicio__nombre')
    list_filter = ('fecha', 'estado')
    ordering = ('-fecha', 'hora')

