from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='LR_index'),
    url(r'^register$', views.register, name='LR_register'),
    url(r'^login$', views.login, name='LR_login'),
    url(r'^success$', views.success, name='LR_success'),
    url(r'^logout$', views.logout, name='LR_logout'),
]
