#!/usr/bin/env python

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
	temp_list = []
	time.sleep(0.3)
	wappalyzer = Wappalyzer.latest()
	webpage = WebPage.new_from_url(domain)
	set1 = wappalyzer.analyze(webpage)
	if set1:
		print "[+] Third party libraries in Use:"
		for s in set1:
			temp_list.append("\t%s" % s)
			print "\t%s" % s
		return temp_list
	else:
		print "\t\t\t[-] Nothing found. Make sure domain name is passed properly"
		return temp_list



def main():
	domain = sys.argv[1]
	print colored(style.BOLD + '\n---> Wapplyzing web page of base domain:\n' + style.END, 'blue')

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
