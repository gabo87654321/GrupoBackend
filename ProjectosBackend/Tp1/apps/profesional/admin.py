from django.contrib import admin
from apps.profesional.models import Profesional

# Register your models here.
@admin.register(Profesional) #aca registro la clase profesional que se importa en la linea 2
class ProfesinalAdmin(admin.ModelAdmin):# aca creo una clase que hereda el modeladmin del modulo admin que se importa en la linea uno
    list_display =["user", "nombre", "especialidad"]
