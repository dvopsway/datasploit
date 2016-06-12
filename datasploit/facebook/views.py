from django.shortcuts import render_to_response ,HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def module_page(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('facebook.html', c ,context_instance=RequestContext(request))
