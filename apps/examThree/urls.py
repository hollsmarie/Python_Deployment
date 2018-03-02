from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^update$', views.update, name='update'),
    url(r'^(?P<id>\d+)/remove$', views.remove, name='remove'),
    url(r'^(?P<id>\d+)/show$', views.show, name='show'),
    url(r'^(?P<id>\d+)/addfave$', views.addfave, name='addfave'),
]