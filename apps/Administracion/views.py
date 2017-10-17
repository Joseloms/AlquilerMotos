from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from apps.Administracion.forms import GroupForm, UserForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


from django.shortcuts import render
from django.utils import timezone

# Create your views here.

def IndexView(request):
    context = {'ahora': timezone.now()}
    return render(request, 'base/index.html', context)


class GrupoCreate(CreateView):
    model = Group
    template_name = 'administracion/grupo_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('administracion:grupo_list')


class GrupoUpdate(UpdateView):
    model = Group
    template_name = 'administracion/grupo_form.html'
    form_class = GroupForm
    success_url = reverse_lazy('administracion:grupo_list')


class GrupoDelete(DeleteView):
    model = Group
    template_name = 'administracion/grupo_delete.html'
    success_url = reverse_lazy('administracion:grupo_list')


class GrupoList(ListView):
    model = Group
    template_name = 'administracion/grupo_list.html'


class GrupoDetail(DetailView):
    model = Group
    template_name = 'administracion/grupo_detail.html'


class UsuarioCreate(CreateView):
    model = Group
    template_name = 'administracion/usuario_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:usuario_list')


class UsuarioUpdate(UpdateView):
    model = User
    template_name = 'administracion/usuario_form.html'
    form_class = UserForm
    success_url = reverse_lazy('administracion:usuario_list')


class UsuarioDelete(DeleteView):
    model = User
    template_name = 'administracion/usuario_delete.html'
    success_url = reverse_lazy('administracion:usuario_list')


class UsuarioList(ListView):
    model = User
    template_name = 'administracion/usuario_list.html'


class UsuarioDetail(DetailView):
    model = User
    template_name = 'administracion/usuario_detail.html'


def login_view(request):
    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('administracion:index'))
            else:
                mensaje = 'El usuario no esta activo'
                return render(request, 'administracion/login.html', {'mensaje': mensaje})
                pass
        mensaje = 'Nombre de usuario o contraseña no valido'
    return render(request, 'administracion/login.html', {'mensaje': mensaje})

def logout_view(request):
    logout(request)
    messages.success(request, 'Te has desconectado con exito.')
    return redirect(reverse('administracion:login'))