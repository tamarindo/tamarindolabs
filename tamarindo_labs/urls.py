from django.conf.urls import patterns, include, url
from apps.website.urls import website_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tamarindo_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(website_urls)),
)
