from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext  # para hacer funcionar {% csrf_token %}


def home(request):

    template = "home.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))

def portafolio(request):

    template = "portafolio.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))
   
def servicios(request):

    template = "servicios.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))
   
def contacto(request):

    template = "contacto.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))
   
