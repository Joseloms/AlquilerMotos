#encoding:utf-8
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from .forms import AlquilerCreateForm
from .forms import ClienteForm, AlquilerForm
from .models import Cliente, Alquiler
from decimal import Decimal



# Create your views here.
class ClienteCreate(SuccessMessageMixin, CreateView):
    model = Cliente
    template_name = 'alquiler/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('alquiler:cliente_list')
    success_message = "%(nombre)s creado correctamente"

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
    context_object_name = 'clientes'

class AlquilerCreate(SuccessMessageMixin, CreateView):
    model = Alquiler
    template_name = 'alquiler/alquiler_form.html'
    form_class = AlquilerForm
    success_url = reverse_lazy('alquiler:alquiler_list')
    success_message = "%(descripcion)s creado correctamente"

def busqueda(request):
   q = request.GET.get('q','')
   clientes = Cliente.objects.filter(nombre__icontains=q)
   return render(request, 'alquiler/cliente_list.html', {'clientes': clientes})

def Alquiler_crear(request):
    if request.method == 'POST':
        POST = request.POST.copy()
        POST['cajero'] = request.user.id
        inicio = datetime.strptime(datetime.now().strftime("%H:%M"), "%H:%M")
        fin = inicio + timedelta(minutes = int(POST['tiempo']))
        hora_fin = "%s:%s"%(fin.hour, fin.minute)
        POST["hora_inicio"] = datetime.now().strftime("%H:%M")
        POST['hora_fin'] = hora_fin
        form = AlquilerCreateForm(POST)
        if form.is_valid():
            form.save()
            alquiler = form.save()
            div = int(POST['tiempo'])
            if div == 120:
                alquiler.total = alquiler.get_precio()*2
            if div == 60:
                alquiler.total = alquiler.get_precio()
            if div == 30:
                alquiler.total = alquiler.get_precio()/2
            if div == 15:
                alquiler.total = alquiler.get_precio()*Decimal(0.25)
            alquiler.save()
            alquiler.vehiculo.all().update(activo=False)
            messages.success(request, 'Alquiler creado.')
            return redirect(reverse_lazy('alquiler:alquiler_list_activos'))
        else:
            messages.error(request, 'Verifique la informacion.')
            form = AlquilerForm(POST)
            context = {'form': form}
            return render(request, 'alquiler/alquiler_form.html',context)
    else:
        form = AlquilerForm()
        context = {'form': form}
        return render(request, 'alquiler/alquiler_form.html',context)

def Alquiler_finalizar(request, pk):
    ### Logica para saber si esta activo el Alquiler
    ### luego de eso se setea los Vehiculos status True
    try:
        alquiler = Alquiler.objects.get(id=pk)
    except:
        print "Error"
        return redirect(reverse_lazy('alquiler:alquiler_list_activos'))
    alquiler.vehiculo.all().update(activo=True)
    return redirect(reverse_lazy('alquiler:alquiler_list_activos'))

class AlquilerUpdate(SuccessMessageMixin, UpdateView):
    model = Alquiler
    template_name = 'alquiler/alquiler_form.html'
    form_class = AlquilerCreateForm
    success_url = reverse_lazy('alquiler:alquiler_list_activos')
    success_message = "Modificado Correctamente"

class AlquilerDelete(SuccessMessageMixin, DeleteView):
    model = Alquiler
    template_name = 'alquiler/alquiler_delete.html'
    success_url = reverse_lazy('alquiler:alquiler_list')
    success_message = "Elimado Correctamente"

class AlquilerList(ListView):
    model = Alquiler
    template_name = 'alquiler/alquiler_list.html'
    context_object_name = 'alquileres'


def AlquilerListActivos(request):
    alquileres = Alquiler.objects.filter(pagado=False)
    context = {'alquileres': alquileres}
    return render(request, 'alquiler/alquiler_list_activos.html', context)

class AlquilerDetail(DetailView):
    model = Alquiler
    template_name = 'alquiler/alquiler_detail.html'
    context_object_name = 'alquiler'