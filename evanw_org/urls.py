from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from evanw_org import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^downloads/', include('downloads.urls')),
    url(r'^projects/', include('projects.urls')),
	url(r'^resume/', TemplateView.as_view(template_name='resume.html')),
    url(r'', include('blog.urls')),
    )
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
