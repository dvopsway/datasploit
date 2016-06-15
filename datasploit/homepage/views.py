from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf

# Create your views here.
def home(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html',c,context_instance=RequestContext(request))
