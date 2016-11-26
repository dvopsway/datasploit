#!/usr/bin/env python

import requests
import sys
import json
import warnings
from termcolor import colored
import time
class style:
   BOLD = '\033[1m'
   END = '\033[0m'

warnings.filterwarnings("ignore")

def checkpunkspider(reversed_domain):
	print colored(style.BOLD + '\n---> Trying luck with PunkSpider\n' + style.END, 'blue')
	time.sleep(0.5)
	req= requests.post("http://www.punkspider.org/service/search/detail/" + reversed_domain, verify=False)
	try:
		return json.loads(req.content)
	except:
		return {}



def main():
	domain = sys.argv[1]
	#convert domain to reverse_domain for passing to checkpunkspider()
	reversed_domain = ""
	for x in reversed(domain.split(".")):
		reversed_domain = reversed_domain + "." + x
	reversed_domain = reversed_domain[1:]
	res = checkpunkspider(reversed_domain)
	if res is not None:
		if 'data' in res.keys() and len(res['data']) >= 1:
			print colored("Few vulnerabilities found at Punkspider", 'green')
			for x in res['data']:
				print "==> ", x['bugType']
				print "Method:", x['verb'].upper()
				print "URL:\n" + x['vulnerabilityUrl']
				print "Param:", x['parameter']
		else:
			print colored("[-] No Vulnerabilities found on PunkSpider", 'red')

if __name__ == "__main__":
	main()
