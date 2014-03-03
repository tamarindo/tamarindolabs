from django.conf.urls import patterns, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

adminsas_urls = patterns('apps.admin_sas.views',
    url(r'^/$','login'),
    url(r'^/panel$', 'panel', name="panel"),  
)  


