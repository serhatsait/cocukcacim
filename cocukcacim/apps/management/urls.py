from django.conf.urls import url
from cocukcacim.apps.management.views import management_view

urlpatterns = [
    url(r'^$', management_view, name='management'),
]
