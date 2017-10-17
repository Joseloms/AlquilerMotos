from .forms import VehiculoForm, TipoForm, MantenimientoForm, TrabajoForm
from .models import Vehiculo, Tipo, Trabajo, Mantenimiento
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin

class VehiculoCreate(CreateView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_form.html'
    form_class = VehiculoForm
    success_url = reverse_lazy('vehiculo:vehiculo_list')


class VehiculoUpdate(UpdateView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_form.html'
    form_class = VehiculoForm
    success_url = reverse_lazy('vehiculo:vehiculo_list')


class VehiculoDelete(DeleteView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_delete.html'
    success_url = reverse_lazy('vehiculo:vehiculo_list')


class VehiculoList(ListView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_list.html'

class TipoCreate(SuccessMessageMixin, CreateView):
    model = Tipo
    template_name = 'vehiculo/tipo_form.html'
    form_class = TipoForm
    success_url = reverse_lazy('vehiculo:tipo_list')
    success_message = "%(descripcion)s creado correctamente"


class TipoUpdate(SuccessMessageMixin, UpdateView):
    model = Tipo
    template_name = 'vehiculo/vehiculo_form.html'
    form_class = TipoForm
    success_url = reverse_lazy('vehiculo:tipo_list')
    success_message = "Modificado Correctamente"

class TipoDelete(SuccessMessageMixin, DeleteView):
    model = Tipo
    template_name = 'vehiculo/tipo_delete.html'
    success_url = reverse_lazy('vehiculo:tipo_list')
    success_message = "Elimado Correctamente"

class TipoList(ListView):
    model = Tipo
    template_name = 'vehiculo/tipo_list.html'

class TrabajoCreate(SuccessMessageMixin, CreateView):
    model = Trabajo
    template_name = 'vehiculo/trabajo_form.html'
    form_class = TrabajoForm
    success_url = reverse_lazy('vehiculo:trabajo_list')
    success_message = "%(descripcion)s creado correctamente"


class TrabajoUpdate(SuccessMessageMixin, UpdateView):
    model = Trabajo
    template_name = 'vehiculo/trabajo_form.html'
    form_class = TrabajoForm
    success_url = reverse_lazy('vehiculo:trabajo_list')
    success_message = "Modificado Correctamente"

class TrabajoDelete(SuccessMessageMixin, DeleteView):
    model = Trabajo
    template_name = 'vehiculo/trabajo_delete.html'
    success_url = reverse_lazy('vehiculo:trabajo_list')
    success_message = "Elimado Correctamente"

class TrabajoList(ListView):
    model = Trabajo
    template_name = 'vehiculo/trabajo_list.html'

class MantenimientoCreate(SuccessMessageMixin, CreateView):
    model = Mantenimiento
    template_name = 'vehiculo/mantenimiento_form.html'
    form_class = MantenimientoForm
    success_url = reverse_lazy('vehiculo:mantenimiento_list')
    success_message = "%(descripcion)s creado correctamente"


class MantenimientoUpdate(SuccessMessageMixin, UpdateView):
    model = Mantenimiento
    template_name = 'vehiculo/mantenimiento_form.html'
    form_class = MantenimientoForm
    success_url = reverse_lazy('vehiculo:mantenimiento_list')
    success_message = "Modificado Correctamente"

class MantenimientoDelete(SuccessMessageMixin, DeleteView):
    model = Mantenimiento
    template_name = 'vehiculo/mantenimiento_delete.html'
    success_url = reverse_lazy('vehiculo:mantenimiento_list')
    success_message = "Elimado Correctamente"

class MantenimientoList(ListView):
    model = Mantenimiento
    template_name = 'vehiculo/mantenimiento_list.html'
