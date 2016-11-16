import json
import requests
from Wappalyzer import Wappalyzer, WebPage
import sys
import time
from termcolor import colored

class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def wappalyzeit(domain):
	time.sleep(0.3)
	wappalyzer = Wappalyzer.latest()
	webpage = WebPage.new_from_url(domain)
	set1 = wappalyzer.analyze(webpage)
	if set1:
		print "[+] Third party libraries in Use:"
		for s in set1:
			print "\t%s" % s
	else:
		print "\t\t\t[-] Nothing found. Make sure domain name is passed properly"



def main():
	domain = sys.argv[1]
	print colored(style.BOLD + '---> Wapplyzing web page of base domain:\n' + style.END, 'blue')

	#make proper URL with domain. Check on ssl as well as 80.
	print "Hitting HTTP:\n",
	try:
		targeturl = "http://" + domain
		wappalyzeit(targeturl)
	except:
		print "[-] HTTP connection was unavailable"
	print "\nHitting HTTPS:\n",
	try:
		targeturl = "https://" + domain
		wappalyzeit(targeturl)
	except:
		print "[-] HTTPS connection was unavailable"
	print "\n-----------------------------\n"



if __name__ == "__main__":
	main()
