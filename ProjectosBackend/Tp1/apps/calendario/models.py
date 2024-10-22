from django.db import models
from django.contrib.auth.models import User  # Si usas el modelo de usuario predeterminado de Django
# Create your models here.
class Calendario(models.Model):
    profesional = models.ForeignKey("profesional.Profesional", on_delete=models.CASCADE)
    fecha_disponibilidad = models.DateTimeField()
    

    def __str__(self):
        return f"{self.profesional}"
    