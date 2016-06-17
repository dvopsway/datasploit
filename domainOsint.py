#input domain name

#domain_osint

#pip lxml json 

#http://searchdns.netcraft.com/?restriction=site+contains&host=olacabs.com&lookup=wait..&position=limited

#completed

#punkspider, shodan, whois,

#show whois , dns, buildwith, wappalyzer, punkspider info
	#	subdomain find. knocy.py / google 
	#	server profiling of subdomains
	#	check for .git/htaccess/web.config/extractc.

#https://github.com/ivanlei/threatbutt
#	harvest emails
#	find files
#	extract info from files 
#	find information, harvest email. 
#	check on fb, relate to username. 
#	show possible graph search links
#	twiter graph on the username
#	namecheck with usernamejjjj
#	hibp

import time
import whois
import requests
import socket
import sys	
import json
from Wappalyzer import Wappalyzer, WebPage
from bs4 import BeautifulSoup
import dns.resolver
import config as cfg
import re
from urlparse import urlparse
import hashlib
import urllib



from domain_whois import whoisnew
from domain_dnsrecords import fetch_dns_records,parse_dns_records
from ip_shodan import shodansearch
from domain_zoomeye import get_accesstoken_zoomeye,search_zoomeye
from domain_checkpunkspider import checkpunkspider
from domain_wappalyzer import wappalyzeit
from domain_subdomains import check_and_append_subdomains,subdomains,find_subdomains_from_wolfram,subdomains_from_netcraft
from domain_pagelinks import pagelinks
from domain_history import netcraft_domain_history
from domain_emailhunter import emailhunter
from domain_github import github_search
from domain_forumsearch import boardsearch_forumsearch
from domain_wikileaks import wikileaks
from domain_censys import view,censys_search




collected_emails = []
subdomain_list = []
censys_list = []

######
##   Proram starts here  ##
######


def main(): 
	domain = sys.argv[1]
	
	API_URL = "https://www.censys.io/api/v1"
	#print cfg.zoomeyeuser


	#print WhoIs information
	print whoisnew(domain)
	print "\n-----------------------------\n"


	#print DNS Information
	dns_records = parse_dns_records(domain)
	for x in dns_records.keys():
		print x
		if "No" in dns_records[x] and "Found" in dns_records[x]:
			print "\t%s" % (dns_records[x])
		else:
			for y in dns_records[x]:
				print "\t%s" % (y)
			#print type(dns_records[x])
	print "\n-----------------------------\n"

	#converts domain to IP. Prints a statement for the same.
	ip_addr = socket.gethostbyname(domain)

	#checks for information at shodan, and comes back with whatever available.
	## need to apply filter here (lot of noise coming in)
	res_from_shodan = json.loads(shodansearch(ip_addr))
	print res_from_shodan
	#for iterate_shodan_list in res_from_shodan['data']:
	#	print "ISP: %s \n Hosts: %s \n IP: %s \n Data: %s\n" % (iterate_shodan_list['isp'], iterate_shodan_list['hostnames'], iterate_shodan_list['ip_str'], iterate_shodan_list['data'].strip("\n"))
	print "\n-----------------------------\n"

	#checks results from zoomeye
	#filters need to be applied
	zoomeye_results = search_zoomeye(domain)
	dict_zoomeye_results = json.loads(zoomeye_results)
	print dict_zoomeye_results
	print "\n-----------------------------\n"

	#convert domain to reverse_domain for passing to checkpunkspider()
	reversed_domain = ""
	for x in reversed(domain.split(".")):
		reversed_domain = reversed_domain + "." + x
	reversed_domain = reversed_domain[1:]
	checkpunkspider(reversed_domain)
	print "\n-----------------------------\n"

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

	#make Search github code for the given domain.
	print github_search(domain, 'Code')
	print "\n-----------------------------\n"
	
	#collecting emails for the domain and adding information in master email list. 
	emailhunter(domain)
	print "\t\t\t[+] Finding Email Ids\n"
	for x in collected_emails:
		print str(x) + ", ",
	print "\n-----------------------------\n"


	dns_history = netcraft_domain_history(domain)
	for x in dns_history.keys():
		print "%s: %s" % (dns_history[x], x)
	print "\n-----------------------------\n"	

	#subdomains [to be called before pagelinks so as to avoid repititions.]
	print "\t\t\t[+] Finding Subdomains and appending\n"
	subdomains(domain)
	##print "\t\t\t[+] Check_subdomains from wolframalpha"
	##find_subdomains_from_wolfram(domain)
	print "\n-----------------------------\n"

	

	#domain pagelinks
	print "\t\t\t[+] Pagelinks\n"
	links=pagelinks(domain)	
	for x in links:
		print x
	print "\n-----------------------------\n"

		#wikileaks
	print "\t\t\t[+] Associated WikiLeaks\n"
	leaklinks=wikileaks(domain)
	for tl,lnk in leaklinks.items():
		print "%s (%s)" % (lnk, tl)
	print "For all results, visit: "+ 'https://search.wikileaks.org/?query=&exact_phrase=%s&include_external_sources=True&order_by=newest_document_date'%(domain)
	print "\n-----------------------------\n"
	
	
	print "\t\t\t[+] Associated Forum Links\n"
	links=boardsearch_forumsearch(domain)
	for tl,lnk in links.items():
		print "%s (%s)" % (lnk, tl)
	print "\n-----------------------------\n"
	
	censys_search(domain)
	for x in censys_list:
		print x


	subdomains_from_netcraft(domain)
	print "\n\t\t\t[+] List of subdomains found\n"
	for sub in subdomain_list:
		print sub

if __name__ == "__main__":
	main()


