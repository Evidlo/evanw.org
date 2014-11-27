from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/?$', include('blog.urls')),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^downloads/?', include('downloads.urls')),
	url(r'^category/', include('blog.urls')),
    )
urlpatterns += staticfiles_urlpatterns()
