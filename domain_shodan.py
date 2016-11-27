#!/usr/bin/env python

import config as cfg
import requests
import json
import sys
import socket
from termcolor import colored
import time


class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def shodandomainsearch(domain):
	print colored(style.BOLD + '\n---> Searching in Shodan:\n' + style.END, 'blue')
	time.sleep(0.3)
	endpoint =  "https://api.shodan.io/shodan/host/search?key=%s&query=hostname:%s&facets={facets}" % (cfg.shodan_api, domain)
	req = requests.get(endpoint)
	return req.content


def main():
	domain = sys.argv[1]
	res_from_shodan = json.loads(shodandomainsearch(domain))
	if 'matches' in res_from_shodan.keys():
		for x in res_from_shodan['matches']:
			print "IP: %s\nHosts: %s\nDomain: %s\nPort: %s\nData: %s\nLocation: %s\n" % (x['ip_str'], x['hostnames'], x['domains'], x['port'], x['data'].replace("\n",""), x['location'])
	print "-----------------------------\n"

if __name__ == "__main__":
	main()
