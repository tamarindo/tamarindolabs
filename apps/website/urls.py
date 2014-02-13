from django.conf.urls import patterns, url

website_urls = patterns('apps.website.views',
    url(r'^$', 'home', name="home"),
    url(r'^portafolio/$', 'portafolio', name="portafolio"),
    url(r'^servicios/$', 'servicios', name="servicios"),
    url(r'^contactenos/$', 'contactenos', name="contactenos"),
    url(r'^vista_portafolio/$', 'element_portafolio', name="element_portafolio"),     
)


