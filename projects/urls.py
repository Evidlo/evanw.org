from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^category/(?P<category>.*)$', index),
    url(r'^$', index),
    url(r'^(?P<project>.+)$', detail),
)
