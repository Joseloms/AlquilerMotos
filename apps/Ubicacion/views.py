from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import GpsForm, LimiteForm
from django.core.urlresolvers import reverse_lazy
from .models import GPS, Limite
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class GpsCreate(SuccessMessageMixin, CreateView):
    model = GPS
    template_name = 'ubicacion/gps_form.html'
    form_class = GpsForm
    success_url = reverse_lazy('ubicacion:gps_list')
    success_message = "%(descripcion)s creado correctamente"

class GpsUpdate(SuccessMessageMixin, UpdateView):
    model = GPS
    template_name = 'ubicacion/gps_form.html'
    form_class = GpsForm
    success_url = reverse_lazy('ubicacion:gps_list')
    success_message = "Modificado Correctamente"

class GpsDelete(SuccessMessageMixin, DeleteView):
    model = GPS
    template_name = 'ubicacion/gps_delete.html'
    success_url = reverse_lazy('ubicacion:gps_list')
    success_message = "Elimado Correctamente"

class GpsList(ListView):
    model = GPS
    template_name = 'ubicacion/gps_list.html'

class LimiteCreate(SuccessMessageMixin, CreateView):
    model = Limite
    template_name = 'ubicacion/limite_form.html'
    form_class = LimiteForm
    success_url = reverse_lazy('ubicacion:limite_list')
    success_message = "%(descripcion)s creado correctamente"

class LimiteUpdate(SuccessMessageMixin, UpdateView):
    model = Limite
    template_name = 'ubicacion/limite_form.html'
    form_class = LimiteForm
    success_url = reverse_lazy('ubicacion:limite_list')
    success_message = "Modificado Correctamente"

class LimiteDelete(SuccessMessageMixin, DeleteView):
    model = Limite
    template_name = 'ubicacion/limite_delete.html'
    success_url = reverse_lazy('ubicacion:limite_list')
    success_message = "Elimado Correctamente"

class LimiteList(ListView):
    model = Limite
    template_name = 'ubicacion/limite_list.html'