#!/usr/bin/env python

import config as cfg
import requests
import json
import sys
import time

from termcolor import colored
class style:
   BOLD = '\033[1m'
   END = '\033[0m'

collected_emails = []

def emailhunter(domain):
	print colored(style.BOLD + '\n---> Harvesting Email Addresses:.\n' + style.END, 'blue')
	time.sleep(0.3)
	url="https://api.emailhunter.co/v1/search?api_key=%s&domain=%s" % (cfg.emailhunter, domain)
	res=requests.get(url)
	try:
		parsed=json.loads(res.text)
		if 'emails' in parsed.keys():
			for email in parsed['emails']:
				collected_emails.append(email['value'])
	except:
		print 'CAPTCHA has been implemented, skipping this for now.'

def main():
	domain = sys.argv[1]
	if cfg.emailhunter != "" and cfg.emailhunter != "":
		emailhunter(domain)
		for x in collected_emails:
			print str(x)
		print "\n\n-----------------------------\n"


if __name__ == "__main__":
	main()

