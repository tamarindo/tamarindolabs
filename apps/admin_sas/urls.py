from django.conf.urls import patterns, url

admin_sas_urls = patterns('apps.admin_sas.views',
    url(r'^client/$', 'client', name="client"),
    url(r'^administrator/$', 'administrator', name="administrator"),
  
)


