from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.servicio.models import Servicio


class ServicioListView(ListView):
    model = Servicio
    template_name = 'servicio_list.html'
    context_object_name = 'servicios'

class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'servicio_form.html'
    fields = ['nombre', 'descripcion', 'duracion_estimada', 'precio', 'profesionales']
    success_url = reverse_lazy('servicio_list')

class ServicioUpdateView(UpdateView):
    model = Servicio
    template_name = 'servicio_form.html'
    fields = ['nombre', 'descripcion', 'duracion_estimada', 'precio', 'profesionales']
    success_url = reverse_lazy('servicio_list')

class ServicioDeleteView(DeleteView):
    model = Servicio
    template_name = 'servicio_confirm_delete.html'
    success_url = reverse_lazy('servicio_list')
