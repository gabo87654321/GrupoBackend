from django.db import models
from django.contrib.auth.models import User  # Si usas el modelo de usuario predeterminado de Django
# Create your models here.
class Profesional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona con el usuario de Django
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre