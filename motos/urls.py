from django.conf.urls import url

from . import views

urlpatterns = [
    # /motos/ | /
    url(r'^crear/$', views.ClienteCreateView.as_view(), name='motos.crear'),
    url(r'^crear1/$', views.MotoCreateView.as_view(), name='motos.crear1'),
    url(r'^crear2/$', views.AlquilerCreateView.as_view(), name='motos.crear2'),
    url(r'^alqList/$', views.AlquilerListView.as_view(), name='motos.alquiler_list'),
]