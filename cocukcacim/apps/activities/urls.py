from django.conf.urls import url
from cocukcacim.apps.activities.views import activity_view

urlpatterns = [
    url(r'^$', activity_view, name='activities'),
]
