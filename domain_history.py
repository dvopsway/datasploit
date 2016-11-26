#!/usr/bin/env python

import sys
import json
import requests 
from bs4 import BeautifulSoup
import re
from termcolor import colored
import time

class style:
   BOLD = '\033[1m'
   END = '\033[0m'


def netcraft_domain_history(domain):
	ip_history_dict= {}
	print colored(style.BOLD + '\n---> Searching Domain history in Netcraft\n' + style.END, 'blue')
	time.sleep(0.3)
	endpoint =  "http://toolbar.netcraft.com/site_report?url=%s" % (domain)
	req = requests.get(endpoint)

	soup = BeautifulSoup(req.content, 'html.parser')
	urls_parsed = soup.findAll('a', href = re.compile(r'.*netblock\?q.*'))
	for url in urls_parsed:
		if (urls_parsed.index(url) != 0):
			ip_history_dict[str(url).split('=')[2].split(">")[1].split("<")[0]] = str(url.parent.findNext('td')).strip("<td>").strip("</td>")
	return ip_history_dict


def main():
	domain = sys.argv[1]
	dns_history = netcraft_domain_history(domain)
	for x in dns_history.keys():
		print "%s: %s" % (dns_history[x], x)
	print "\n-----------------------------\n"	

if __name__ == "__main__":
	main()
