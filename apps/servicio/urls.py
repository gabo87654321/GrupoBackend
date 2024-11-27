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
    path('', ServicioListView.as_view(), name='servicio_list'),

    # Crear un nuevo servicio
    path('create/', ServicioCreateView.as_view(), name='servicio_create'),

    # Editar un servicio existente
    path('<int:pk>/editar/', ServicioUpdateView.as_view(), name='servicio_update'),

    # Eliminar un servicio
    path('<int:pk>/eliminar/', ServicioDeleteView.as_view(), name='servicio_delete'),
]
