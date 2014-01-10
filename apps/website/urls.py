from django.conf.urls import patterns, url

website_urls = patterns('apps.website.views',
    url(r'^$', 'home', name="home"),
    url(r'^portafolio/$', 'portafolio', name="portafolio"),
    url(r'^servivios/$', 'servivios', name="servivios"),
    url(r'^contactenos/$', 'servivios', name="servivios"),   
)


