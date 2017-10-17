from django.conf.urls import url
from . import views
from apps.Administracion.views import GrupoCreate, GrupoList, GrupoUpdate, GrupoDelete, GrupoDetail,UsuarioCreate,UsuarioUpdate,UsuarioDelete,UsuarioDetail,UsuarioList

urlpatterns = [

    url(r'^$', views.IndexView, name='index'),
    url(r'^grupo/nuevo/$', GrupoCreate.as_view(), name='grupo_crear'),
    url(r'^grupo/lista/$', GrupoList.as_view(), name='grupo_list'),
    url(r'^grupo/editar/(?P<pk>\d+)/$', GrupoUpdate.as_view(), name='grupo_editar'),
    url(r'^grupo/eliminar/(?P<pk>\d+)/$', GrupoDelete.as_view(), name='grupo_eliminar'),
    url(r'^grupo/detalle/(?P<pk>\d+)/$', GrupoDetail.as_view(), name='grupo_detalle'),
    url(r'^usuario/nuevo/$', UsuarioCreate.as_view(), name='usuario_crear'),
    url(r'^usuario/lista/$', UsuarioList.as_view(), name='usuario_list'),
    url(r'^usuario/editar/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='usuario_editar'),
    url(r'^usuario/eliminar/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='usuario_eliminar'),
    url(r'^usuario/detalle/(?P<pk>\d+)/$', UsuarioDetail.as_view(), name='usuario_detalle'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]