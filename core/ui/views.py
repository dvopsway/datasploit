from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from osint import *

import re, json
from uuid import uuid4
from pymongo import MongoClient
from bson import json_util

# Create your views here.

def index(request):
	return render(request, 'index.html')

def search(request):
	if request.method == "POST":
		domain = request.POST.get("domain", None)
		if domain:
			domain = domain.lower()
			pattern = "^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$"
			check = re.match(pattern, domain)
			if check:
				functions = [domain_GooglePDF.run, domain_checkpunkspider.checkpunkspider, domain_dnsrecords.parse_dns_records, domain_emailhunter.emailhunter, domain_forumsearch.boardsearch_forumsearch, domain_github.github_search, domain_history.netcraft_domain_history, domain_pagelinks.pagelinks, domain_shodan.shodandomainsearch, domain_sslinfo.check_ssl_htbsecurity, domain_wappalyzer.wappalyzeit, domain_whois.whoisnew, domain_wikileaks.wikileaks]	
				
				taskId = str(uuid4())
				client = MongoClient()
			        db = client.database1
			        d = {"status_check": taskId, "count": len(functions), "type": "poller"}
			        result = db.domaindata.insert(d, check_keys=False)
				print result

				for fn in functions:
					fn.delay(domain, taskId)
				#print domain_whois.whoisnew.delay(domain)
				return render(request, 'search.html', {"domain": domain, "taskId": taskId}) 
			else:
				return redirect('osint:index')
		return HttpResponse("Search")
	else:
		return redirect('osint:index')

@csrf_exempt
def status(request):
	if request.method == "POST":
		taskId = request.POST.get("taskId", None)
		domain = request.POST.get("domain", None)
		if taskId and domain:
			client = MongoClient()
                        db = client.database1
			cursor = db.domaindata.find({"type": "poller", "status_check": taskId})
			if cursor.count() == 1:
				doc = cursor.next()
				cursor = db.domaindata.find({"targetname": domain, "taskId": taskId})
				if cursor.count() == doc['count']:
					scanned = []
					try:
                                                while True:
                                                        doc = cursor.next()
                                                        scanned.append(doc['record'])
					except:
						pass
					d = {"status": True, "message": scanned}
					j = json.dumps(d, default=json_util.default)
					return HttpResponse(j)
				else:
					scanned = ['']
					try:
						while True:
							doc = cursor.next()
							scanned.append(doc['record']['type'])
					except:
						pass
					d = {"status": False, "message": scanned}
					j = json.dumps(d)
					return HttpResponse(j)
			else:
				d = {"status": False, "message": "STOP"}
                                j = json.dumps(d)
                                return HttpResponse(j)
		else:
			return redirect('osint:index')
	else:
		return redirect('osint:index')












