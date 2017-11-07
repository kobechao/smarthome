from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^generic', views.generic),
    url(r'^light', views.light),
    url(r'^fjs', views.fjs),
    url(r'^login', views.login),

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
