#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import sys
import json
from termcolor import colored
import time


class style:
   BOLD = '\033[1m'
   END = '\033[0m'


def wikileaks(domain):
	print colored(style.BOLD + '\n---> Searching through WikiLeaks\n' + style.END, 'blue')
	time.sleep(0.3)
	req = requests.get('https://search.wikileaks.org/?query=&exact_phrase=%s&include_external_sources=True&order_by=newest_document_date'%(domain))
	soup=BeautifulSoup(req.content, "lxml")
	count=soup.findAll('div',{"class":"total-count"})
	print "Total "+count[0].text
	divtag=soup.findAll('div',{'class':'result'})
	links={}
	for a in divtag:
		links[a.a.text.encode('utf-8')]=a.a['href']
	return links


def main():
	domain = sys.argv[1]
	#wikileaks
	leaklinks=wikileaks(domain)
	for tl,lnk in leaklinks.items():
		print "%s (%s)" % (lnk, tl)
	print "For all results, visit: "+ 'https://search.wikileaks.org/?query=&exact_phrase=%s&include_external_sources=True&order_by=newest_document_date'%(domain)
	print "\n-----------------------------\n"
	


if __name__ == "__main__":
	main()
