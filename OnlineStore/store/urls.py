from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^store/$', views.store, name='store'),
    url(r'^location/$', views.location, name='location'),
    url(r'^searchedlocation/$', views.searchedlocation, name='searchedlocation'),
    url(r'^searchedlocation/storecontains/(.*)/$', views.storecontains, name='storecontains'),
]