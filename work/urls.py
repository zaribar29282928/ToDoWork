from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^create_work$', views.create_work, name='create_work'),
    url(r'^register_work$', views.register_work, name='register_work'),
    url(r'^done/([0-9]{1,5})$', views.done, name='done'),
    url(r'^delete/([0-9]{1,5})$', views.delete, name='delete'),
    #url(r'^delete/(?P<id>[0-9]{1,3})$', views.delete, name='delete'),
]
