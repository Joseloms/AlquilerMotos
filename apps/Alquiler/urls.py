from django.conf.urls import url

from . import views

urlpatterns = [
    # /Ubicacion/
    url(r'^crear/$', views.ClienteCreate.as_view(), name='cliente_crear'),
    url(r'^list/$', views.ClienteList.as_view(), name='cliente_list'),
    url(r'^list2/$', views.busqueda, name='cliente_busqueda'),
    url(r'^editar/(?P<pk>[-\w]+)/$', views.ClienteUpdate.as_view(), name='cliente_editar'),
    url(r'^eliminar/(?P<pk>[-\w]+)/$', views.ClienteDelete.as_view(), name='cliente_eliminar'),
    url(r'^crear2/$', views.Alquiler_crear, name='alquiler_crear'),
    url(r'^list2/$', views.AlquilerList.as_view(), name='alquiler_list'),
    url(r'^editar2/(?P<pk>[-\w]+)/$', views.AlquilerUpdate.as_view(), name='alquiler_editar'),
    url(r'^eliminar2/(?P<pk>[-\w]+)/$', views.AlquilerDelete.as_view(), name='alquiler_eliminar'),

]