from django.contrib import admin
from .models import Profesional

@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'especialidad')
    search_fields = ('nombre', 'apellido', 'email', 'especialidad')
    list_filter = ('especialidad',)
    ordering = ('apellido', 'nombre')
