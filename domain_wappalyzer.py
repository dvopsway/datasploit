import json
import requests
from Wappalyzer import Wappalyzer, WebPage
import sys

def wappalyzeit(domain):
	wappalyzer = Wappalyzer.latest()
	webpage = WebPage.new_from_url(domain)
	set1 = wappalyzer.analyze(webpage)
	if set1:
		print "[+] Third party libraries in Use:"
		for s in set1:
			print s
	else:
		print "\t\t\t[-] Nothing found. Make sure domain name is passed properly"



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



if __name__ == "__main__":
	main()
