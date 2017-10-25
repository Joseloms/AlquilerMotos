"""tutorial_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# tutorial_django/urls.py

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^$', include('home.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^motos/', include('motos.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(
        # /media/:<mixed>path/
        url(
            regex=r'^media/(?P<path>.*)$',
            view='django.views.static.serve',
            kwargs={'document_root': settings.MEDIA_ROOT}))