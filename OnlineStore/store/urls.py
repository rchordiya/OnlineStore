from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^store/$', views.store, name='store'),
    url(r'^location/$', views.location, name='location'),
]