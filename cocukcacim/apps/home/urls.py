from django.conf.urls import url
from cocukcacim.apps.home import views

urlpatterns = [
    url(r'^$', views.yasir, name='index'),
]
