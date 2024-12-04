from django.urls import path
from .views import (
    ServicioListView,
    ServicioCreateView,
    ServicioUpdateView,
    ServicioDeleteView,
)

app_name = 'servicio'

urlpatterns = [
    # Listar servicios
    path('servicio/', ServicioListView.as_view(), name='servicio_list'),

    # Crear un nuevo servicio
    path('servicio/create/', ServicioCreateView.as_view(), name='servicio_create'),

    # Editar un servicio existente
    path('servicio/<int:pk>/editar/', ServicioUpdateView.as_view(), name='servicio_update'),

    # Eliminar un servicio
    path('servicio/<int:pk>/eliminar/', ServicioDeleteView.as_view(), name='servicio_delete'),
]
