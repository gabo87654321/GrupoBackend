from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Turno

class TurnoListView(ListView):
    model = Turno
    template_name = 'turno_list.html'
    context_object_name = 'turnos'

class TurnoCreateView(CreateView):
    model = Turno
    template_name = 'turno_form.html'
    fields = ['usuario', 'servicio', 'profesional', 'fecha', 'hora', 'estado']
    success_url = reverse_lazy('turno_list')

class TurnoUpdateView(UpdateView):
    model = Turno
    template_name = 'turno_form.html'
    fields = ['usuario', 'servicio', 'profesional', 'fecha', 'hora', 'estado']
    success_url = reverse_lazy('turno_list')

class TurnoDeleteView(DeleteView):
    model = Turno
    template_name = 'turno_confirm_delete.html'
    success_url = reverse_lazy('turno_list')

