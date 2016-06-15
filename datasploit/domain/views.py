from django.shortcuts import render_to_response ,HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
import library.getstats as data_import

def module_page(request):
    c = {}
    c.update(csrf(request))
    request.session['search_activated'] = "no"
    return render_to_response('domain.html', c ,context_instance=RequestContext(request))

def search(request):
    request.session['search_activated'] = "yes"
    ip = request.POST.get('search').strip(" ")
    whois = data_import.whoisnew(ip)
    c = {}
    c.update(csrf(request))
    c['whois']= whois
    return render_to_response('domain.html', c ,context_instance=RequestContext(request))
