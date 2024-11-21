from django.urls import path
from .views import TurnoListView, TurnoCreateView, TurnoUpdateView, TurnoDeleteView

app_name = 'turno'

urlpatterns = [
    path('', TurnoListView.as_view(), name='turno_list'),
    path('create/', TurnoCreateView.as_view(), name='turno_create'),
    path('<int:pk>/update/', TurnoUpdateView.as_view(), name='turno_update'),
    path('<int:pk>/delete/', TurnoDeleteView.as_view(), name='turno_delete'),
]
