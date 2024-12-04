from django.urls import path
from .views import TurnoListView, TurnoCreateView, TurnoUpdateView, TurnoDeleteView

app_name = 'turno'

urlpatterns = [
    path('turno', TurnoListView.as_view(), name='turno_list'),
    path('', TurnoCreateView.as_view(), name='turno_create'),
    path('turno/<int:pk>/update/', TurnoUpdateView.as_view(), name='turno_update'),
    path('turno/<int:pk>/delete/', TurnoDeleteView.as_view(), name='turno_delete'),
]
