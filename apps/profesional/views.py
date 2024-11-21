from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Profesional

# Listar profesionales
class ListarProfesionalesView(ListView):
    model = Profesional
    template_name = 'listar_profesionales.html'
    context_object_name = 'profesionales'

# Ver detalles de un profesional
class DetalleProfesionalView(DetailView):
    model = Profesional
    template_name = 'detalle_profesional.html'
    context_object_name = 'profesional'

# Crear un nuevo profesional
class CrearProfesionalView(CreateView):
    model = Profesional
    template_name = 'crear_profesional.html'
    fields = ['nombre', 'apellido', 'email', 'telefono', 'especialidad']
    success_url = reverse_lazy('profesional:listar_profesionales')

# Actualizar un profesional existente
class ActualizarProfesionalView(UpdateView):
    model = Profesional
    template_name = 'editar_profesional.html'
    fields = ['nombre', 'apellido', 'email', 'telefono', 'especialidad']
    success_url = reverse_lazy('profesional:listar_profesionales')

# Eliminar un profesional
class EliminarProfesionalView(DeleteView):
    model = Profesional
    template_name = 'eliminar_profesional.html'
    success_url = reverse_lazy('profesional:listar_profesionales')
