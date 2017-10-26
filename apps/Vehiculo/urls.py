from django.conf.urls import url

from . import views

urlpatterns = [
    # /Vehiculo/
    url(r'^crear/$', views.VehiculoCreate.as_view(), name='vehiculo_crear'),
    url(r'^list/$', views.VehiculoList.as_view(), name='vehiculo_list'),
    url(r'^editar/(?P<pk>[-\w]+)/$', views.VehiculoUpdate.as_view(), name='vehiculo_editar'),
    url(r'^eliminar/(?P<pk>[-\w]+)/$', views.VehiculoDelete.as_view(), name='vehiculo_eliminar'),
    url(r'^crear2/$', views.TipoCreate.as_view(), name='tipo_crear'),
    url(r'^list2/$', views.TipoList.as_view(), name='tipo_list'),
    url(r'^editar2/(?P<pk>[-\w]+)/$', views.TipoUpdate.as_view(), name='tipo_editar'),
    url(r'^eliminar2/(?P<pk>[-\w]+)/$', views.TipoDelete.as_view(), name='tipo_eliminar'),
    url(r'^crear3/$', views.TrabajoCreate.as_view(), name='trabajo_crear'),
    url(r'^list3/$', views.TrabajoList.as_view(), name='trabajo_list'),
    url(r'^editar3/(?P<pk>[-\w]+)/$', views.TrabajoUpdate.as_view(), name='trabajo_editar'),
    url(r'^eliminar3/(?P<pk>[-\w]+)/$', views.TrabajoDelete.as_view(), name='trabajo_eliminar'),
    url(r'^crear4/$', views.MantenimientoCreate.as_view(), name='mantenimiento_crear'),
    url(r'^list4/$', views.MantenimientoList.as_view(), name='mantenimiento_list'),
    url(r'^editar4/(?P<pk>[-\w]+)/$', views.MantenimientoUpdate.as_view(), name='mantenimiento_editar'),
    url(r'^eliminar4/(?P<pk>[-\w]+)/$', views.MantenimientoDelete.as_view(), name='mantenimiento_eliminar'),
    url(r'^filtro/$', views.busqueda, name='mantenimiento_busqueda'),

]