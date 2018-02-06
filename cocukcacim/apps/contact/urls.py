from django.conf.urls import url
from cocukcacim.apps.contact.views import contact_view

urlpatterns = [
    url(r'^$', contact_view, name='contact'),
]
