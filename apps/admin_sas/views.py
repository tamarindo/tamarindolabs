from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext  # para hacer funcionar {% csrf_token %}

# Create your views here.

def client(request):

    template = "client.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))

def administrator(request):

    template = "administrator.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))
   