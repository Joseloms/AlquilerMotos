from django.shortcuts import render
from .forms import ClienteCreateForm, MotoCreateForm, AlquilerCreateForm
from .models import Cliente, Moto, Alquiler
from django.contrib import messages
from django.views import generic
from django.conf import settings

# Create your views here.

class ClienteCreateView(generic.CreateView):

    template_model = 'motos/cliente_form.html'
    model = Cliente
    form_class = ClienteCreateForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('motos.add_motos'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        # añadimos nuevas variables de contexto al diccionario
        context['title'] = 'Crear Cliente'
        context['nombre_btn'] = 'Crear'
        # devolvemos el contexto
        return context

    def form_valid(self, form): #Usuario que esta logeado
        form.instance.owner = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Creado correctamente')
        return super().form_valid(form)

class MotoCreateView(generic.CreateView):

    template_model = 'motos/moto_form.html'
    model = Moto
    form_class = MotoCreateForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('motos.add_motos'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        # añadimos nuevas variables de contexto al diccionario
        context['title'] = 'Crear Moto'
        context['nombre_btn'] = 'Crear'
        # devolvemos el contexto
        return context

    def form_valid(self, form): #Usuario que esta logeado
        form.instance.owner = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Creado correctamente')
        return super().form_valid(form)


class AlquilerCreateView(generic.CreateView):

    template_model = 'motos/moto_form.html'
    model = Alquiler
    form_class = AlquilerCreateForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('motos.add_motos'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        # añadimos nuevas variables de contexto al diccionario
        context['title'] = 'Crear Alquiler'
        context['nombre_btn'] = 'Crear'
        # devolvemos el contexto
        return context

    def form_valid(self, form): #Usuario que esta logeado
        form.instance.owner = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Creado correctamente')
        return super().form_valid(form)

class AlquilerListView(generic.ListView):

    template_model = 'motos/alquiler_list.html'
    model = Alquiler
    context_object_name = 'alquileres'