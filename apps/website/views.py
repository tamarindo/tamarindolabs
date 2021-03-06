from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext  # para hacer funcionar {% csrf_token %}
from apps.admin_sas.models import *
import pprint
import urllib 
from tamarindo_labs import settings as s

def home(request):

    template = "home.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))

def portafolio(request):
	implementaciones = implementation.objects.get_all_active().order_by('?')
	template = "portafolio.html"
	
	return render_to_response(template, locals() , context_instance=RequestContext(request))
   
def servicios(request):

    template = "servicios.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))
   
def contactenos(request):

    template = "contacto.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))
   
def element_portafolio(request):

	template="implementacion_portafolio.html"
	return render_to_response(template, locals(), context_instance=RequestContext(request))