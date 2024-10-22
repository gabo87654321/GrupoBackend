from django.db import models
from django.contrib.auth.models import User  # Si usas el modelo de usuario predeterminado de Django
# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre