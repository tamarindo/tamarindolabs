from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext  # para hacer funcionar {% csrf_token %}

# Create your views here.

def login(request):
	template = "login.html"
	return render_to_response(template, locals(), context_instance=RequestContext(request))

def panel(request):
    template = "admistrator.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))

def p(request):

    # saveViewsLog(request, "apps.account.views.log_in")
    if not request.user.is_anonymous():
        return HttpResponseRedirect(reverse('personal_data'))
    if request.method == 'POST':
        auth_form = AuthenticationForm(data=request.POST)
        if auth_form.is_valid():
            return userLogin(request, request.POST['username'], request.POST['password'])
    else:
        auth_form = AuthenticationForm()
    return render_to_response('login.html', locals(), context_instance=RequestContext(request))

