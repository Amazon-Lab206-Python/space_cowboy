from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^', views.index),
    url(r'^form_process$', views.form_process),
    url(r'^dojo/create$', views.dojo_create),
]