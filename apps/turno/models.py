from django.db import models
from django.contrib.auth.models import User

class Turno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="turno")
    servicio = models.ForeignKey("servicio.Servicio", on_delete=models.CASCADE, related_name="turno")
    profesional = models.ForeignKey("profesional.Profesional", on_delete=models.CASCADE, related_name="turno")
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('confirmado', 'Confirmado'),
            ('cancelado', 'Cancelado'),
        ],
        default='pendiente'
    )

    class Meta:
        unique_together = ('profesional', 'fecha', 'hora')  # Restricción de unicidad

    def __str__(self):
        return f"Turno de {self.usuario.username} con {self.profesional} para {self.servicio} el {self.fecha} a las {self.hora}"
