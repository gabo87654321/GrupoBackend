from django.urls import path
from .views import (
    ListarProfesionalesView,
    DetalleProfesionalView,
    CrearProfesionalView,
    ActualizarProfesionalView,
    EliminarProfesionalView,
)

app_name = 'profesional'

urlpatterns = [
    # Ruta para listar todos los profesionales
    path('profesional/listarprofesinal/', ListarProfesionalesView.as_view(), name='listar_profesionales'),
    
    # Ruta para ver detalles de un profesional
    path('profesional/<int:pk>/', DetalleProfesionalView.as_view(), name='detalle_profesional'),
    
    # Ruta para crear un nuevo profesional
    path('profesional/', CrearProfesionalView.as_view(), name='crear_profesional'),
    
    # Ruta para actualizar un profesional existente
    path('profesional/<int:pk>/editar/', ActualizarProfesionalView.as_view(), name='editar_profesional'),
    
    # Ruta para eliminar un profesional
    path('profesinal/<int:pk>/eliminar/', EliminarProfesionalView.as_view(), name='eliminar_profesional'),
]
