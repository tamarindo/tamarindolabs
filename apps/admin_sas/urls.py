from django.conf.urls import patterns, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

adminsas_urls = patterns('apps.admin_sas.views',
    url(r'^/$','principal', name="principal"),
    url(r'^/login$', 'login', name="login"),
    url(r'^/logout$', 'v_logout', name="v_logout"),    
)  


