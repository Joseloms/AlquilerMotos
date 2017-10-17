from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import ClienteForm, AlquilerForm
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from .models import Cliente, Alquiler
from django.contrib import messages

# Create your views here.
class ClienteCreate(SuccessMessageMixin, CreateView):
    model = Cliente
    template_name = 'alquiler/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('alquiler:cliente_list')
    success_message = "%(nombre)s creado correctamente"

def busqueda(request):
   q = request.GET.get('q','')
   clientes = Cliente.objects.filter(nombre__icontains=q)
   return render(request, 'alquiler/cliente_busqueda.html', {'clientes': clientes})

def Cliente_crear(request):

    if request.method == 'POST':
        cliente = Cliente()
        carnet = request.POST.get('carnet')
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        telefono = request.POST.get('telefono')
        cliente.carnet = carnet
        cliente.nombre = nombre
        cliente.apellidos = apellidos
        cliente.telefono = telefono
        cliente.save()
        messages.success(request, 'Cliente creado.')
        return redirect(reverse_lazy('alquiler:cliente_list'))
    else:
        form = ClienteForm()
    context = {'form': form}
    return render(request, 'alquiler/cliente_form.html',context)

class ClienteUpdate(SuccessMessageMixin, UpdateView):
    model = Cliente
    template_name = 'alquiler/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('alquiler:cliente_list')
    success_message = "Modificado Correctamente"

class ClienteDelete(SuccessMessageMixin, DeleteView):
    model = Cliente
    template_name = 'alquiler/cliente_delete.html'
    success_url = reverse_lazy('alquiler:cliente_list')
    success_message = "Elimado Correctamente"

class ClienteList(ListView):
    model = Cliente
    template_name = 'alquiler/cliente_list.html'

class AlquilerCreate(SuccessMessageMixin, CreateView):
    model = Alquiler
    template_name = 'alquiler/alquiler_form.html'
    form_class = AlquilerForm
    success_url = reverse_lazy('alquiler:alquiler_list')
    success_message = "%(descripcion)s creado correctamente"

def Alquiler_crear(request):

    if request.method == 'POST':
        alquiler = Alquiler()
        cajero = User.username
        cliente = request.POST.get('cliente')
        vehiculos = request.POST.get('vehiculos')
        user_model = User()
        user_model.username = cajero
        cliente_model = Cliente()
        cliente_model.nombre = cliente
        alquiler.cajero = user_model
        alquiler.cliente =  cliente_model
        alquiler.vehiculos = vehiculos
        alquiler.save()
        messages.success(request, 'Alquiler creado.')
        return redirect(reverse_lazy('alquiler:alquiler_list'))
    else:
        form = AlquilerForm()
        context = {'form': form}
        return render(request, 'alquiler/alquiler_form.html',context)

class AlquilerUpdate(SuccessMessageMixin, UpdateView):
    model = Alquiler
    template_name = 'alquiler/alquiler_form.html'
    form_class = AlquilerForm
    success_url = reverse_lazy('alquiler:alquiler_list')
    success_message = "Modificado Correctamente"

class AlquilerDelete(SuccessMessageMixin, DeleteView):
    model = Alquiler
    template_name = 'alquiler/alquiler_delete.html'
    success_url = reverse_lazy('alquiler:alquiler_list')
    success_message = "Elimado Correctamente"

class AlquilerList(ListView):
    model = Alquiler
    template_name = 'alquiler/alquiler_list.html'