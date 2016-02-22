from django.views import generic
from django.contrib import messages
from .models import Article
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from .forms import ArticleCreateForm

def ArticleCreateViewW(request):
    form = ArticleCreateForm()
    return render(request, 'blog/article_form.html', {'form': form})

class ArticleCreateView(generic.CreateView):

    template_model = 'blog/article_form.html'
    model = Article
    form_class = ArticleCreateForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('blog.add_article'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        # añadimos nuevas variables de contexto al diccionario
        context['title'] = 'Crear articulo'
        context['nombre_btn'] = 'Crear'
        # devolvemos el contexto
        return context

    def form_valid(self, form): #Usuario que esta logeado
        form.instance.owner = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Creado correctamente')
        return super().form_valid(form)

class ArticleUpdateView(generic.UpdateView):

    template_model = 'blog/article_form.html'
    model = Article
    form_class = ArticleCreateForm

    def dispatch(self, request, *args, **kwargs):
        # Al igual que con ArticleCreateView, dejo al lector
        # que cambie el comportamiento de este método para saber
        # si esta logueado y tiene permisos.
        # Ver el comentario de ArticleCreateView en el método
        # dispatch
        if not request.user.has_perms('blog.change_article'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        # añadimos nuevas variables de contexto al diccionario
        context['title'] = 'Editar articulo'
        context['nombre_btn'] = 'Editar'
        # devolvemos el contexto
        return context

    def form_valid(self, form): #Usuario que esta logeado
        form.instance.owner = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'Modificado correctamente')
        return super().form_valid(form)

class ArticleDeleteView(generic.DeleteView):

    template_name = 'blog/confirmar_eliminacion.html'
    success_url = reverse_lazy('blog.article_list')
    model = Article

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('blog.delete_article'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)
        
class ArticleListView(generic.ListView):

    template_model = 'blog/article_list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 3 #Mostrar los 3 ultimo
    ordering = '-create_at' #orden desendente por creacion

#def article_list_view(request):
#    articles = Article.objects.all()
#    context = {'articles': articles}
#    return render(request, 'blog/article_list.html', context)

class ArticleDetailView(generic.DetailView):

    template_model = 'blog/article_detail.html'
    model = Article
    context_object_name = 'article'