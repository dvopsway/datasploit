import config as cfg
import requests
import json
import sys
import socket
from celery import shared_task
from osint.utils import *
import config

@shared_task
def shodandomainsearch(domain, taskId):
	print "\t\t\t[+] Searching in Shodan" 
	if config.shodan_api:
		endpoint =  "https://api.shodan.io/shodan/host/search?key=%s&query=hostname:%s&facets={facets}" % (config.shodan_api, domain)
		req = requests.get(endpoint)
		data = json.loads(req.content)
		save_record(domain, taskId, "Shodan", data)
		return data

def main():
	domain = sys.argv[1]
	res_from_shodan = shodandomainsearch(domain, "abc")
	if 'matches' in res_from_shodan.keys():
		for x in res_from_shodan['matches']:
			print "IP: %s\nHosts: %s\nDomain: %s\nPort: %s\nData: %s\nLocation: %s\n" % (x['ip_str'], x['hostnames'], x['domains'], x['port'], x['data'].replace("\n",""), x['location'])
	print "-----------------------------\n"

#if __name__ == "__main__":
	#main()
