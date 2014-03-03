from django.conf.urls import patterns, include, url
from apps.website.urls import website_urls
from apps.admin_sas.urls import adminsas_urls
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

print website_urls
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(website_urls)),
    url(r'^panel', include(adminsas_urls)),
)


urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))