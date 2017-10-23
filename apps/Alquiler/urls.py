from django.conf.urls import url

from apps.Alquiler.views import AlquilerDetail
from . import views

urlpatterns = [
    # /Ubicacion/
    url(r'^crear/$', views.ClienteCreate.as_view(), name='cliente_crear'),
    url(r'^list/$', views.ClienteList.as_view(), name='cliente_list'),
    url(r'^filtro/$', views.busqueda, name='cliente_busqueda'),
    url(r'^editar/(?P<pk>[-\w]+)/$', views.ClienteUpdate.as_view(), name='cliente_editar'),
    url(r'^eliminar/(?P<pk>[-\w]+)/$', views.ClienteDelete.as_view(), name='cliente_eliminar'),
    url(r'^crear2/$', views.Alquiler_crear, name='alquiler_crear'),
    url(r'^list2/$', views.AlquilerList.as_view(), name='alquiler_list'),
    url(r'^list3/$', views.AlquilerListActivos, name='alquiler_list_activos'),
    url(r'^editar2/(?P<pk>[-\w]+)/$', views.AlquilerUpdate.as_view(), name='alquiler_editar'),
    url(r'^eliminar2/(?P<pk>[-\w]+)/$', views.AlquilerDelete.as_view(), name='alquiler_eliminar'),
    url(r'^alquiler/detalle/(?P<pk>\d+)/$', AlquilerDetail.as_view(), name='alquiler_detalle'),

]