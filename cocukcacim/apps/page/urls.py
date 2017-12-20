from django.conf.urls import url
from cocukcacim.apps.page import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'(?P<page_slug>[\w-]+)-(?P<page_id>\d+)', views.page, name='page'),
]
