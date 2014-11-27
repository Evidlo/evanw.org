from django.conf.urls import patterns, url
from downloads import views

urlpatterns = patterns('',
    url(r'^(?P<location>.*)$', views.downloads)
)
