#!/usr/bin/env python

import config as cfg
import requests
import json
import sys
import socket

def shodansearch(ip):
	print "\t\t\t[+] Searching in Shodan" 
	endpoint =  "https://api.shodan.io/shodan/host/" + str(ip) + "?key=" + cfg.shodan_api
	req = requests.get(endpoint)
	return req.content

def domaintoip(domain):
	return socket.gethostbyname(domain)

def main():
	ip_addr = sys.argv[1]
	print ip_addr
	res_from_shodan = json.loads(shodansearch(ip_addr))
	print res_from_shodan
	print "\n-----------------------------\n"

if __name__ == "__main__":
	main()
