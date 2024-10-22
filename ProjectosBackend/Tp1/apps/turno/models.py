from django.db import models
from django.contrib.auth.models import User  # Si usas el modelo de usuario predeterminado de Django

# Create your models here.
class Turno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    profesional = models.ForeignKey("profesional.Profesional", on_delete=models.CASCADE)
    servicio = models.ForeignKey("servicio.Servicio", on_delete=models.CASCADE)
    #calendario = models.ForeignKey(calendario, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"Turno de {self.usuario} con {self.profesional} el {self.fecha_hora}"