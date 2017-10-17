from django.conf.urls import url

from . import views

urlpatterns = [
    # /Ubicacion/
    url(r'^crear/$', views.GpsCreate.as_view(), name='gps_crear'),
    url(r'^list/$', views.GpsList.as_view(), name='gps_list'),
    url(r'^editar/(?P<pk>[-\w]+)/$', views.GpsUpdate.as_view(), name='gps_editar'),
    url(r'^eliminar/(?P<pk>[-\w]+)/$', views.GpsDelete.as_view(), name='gps_eliminar'),
    url(r'^crear2/$', views.LimiteCreate.as_view(), name='limite_crear'),
    url(r'^list2/$', views.LimiteList.as_view(), name='limite_list'),
    url(r'^editar2/(?P<pk>[-\w]+)/$', views.LimiteUpdate.as_view(), name='limite_editar'),
    url(r'^eliminar2/(?P<pk>[-\w]+)/$', views.LimiteDelete.as_view(), name='limite_eliminar'),

]