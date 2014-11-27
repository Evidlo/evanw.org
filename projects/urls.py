from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', project_index, name='project_index'),
)
