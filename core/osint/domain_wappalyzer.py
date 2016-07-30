import json
import requests
from Wappalyzer import Wappalyzer, WebPage
import sys
from celery import shared_task
from osint.utils import *

@shared_task
def wappalyzeit(domain, taskId):
	try:
		wappalyzer = Wappalyzer.latest()
		odomain = "http://%s" % domain 
		webpage = WebPage.new_from_url(odomain)
		set1 = wappalyzer.analyze(webpage)
		wap = []
		if set1:
			print "[+] Third party libraries in Use:"
			for s in set1:
				wap.append(s)
		else:
			print "\t\t\t[-] Nothing found. Make sure domain name is passed properly"
		save_record(domain, taskId, "WapAlyzer", wap)
		return wap
	except:
		return []


def main():
	domain = sys.argv[1]
	#make proper URL with domain. Check on ssl as well as 80.
	print "\t\t\t[+] Wapplyzing " + domain 
	print "Hitting HTTP:\n",
	try:
		targeturl = "http://" + domain
		wappalyzeit(targeturl)
	except:
		print "[-] HTTP connection was unavailable"
	print "Hitting HTTPS:\n",
	try:
		targeturl = "https://" + domain
		wappalyzeit(targeturl)
	except:
		print "[-] HTTPS connection was unavailable"
	print "\n-----------------------------\n"



#if __name__ == "__main__":
	#main()
