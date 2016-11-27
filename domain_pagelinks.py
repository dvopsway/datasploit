#!/usr/bin/env python

import sys
import requests
from termcolor import colored
import time

class style:
   BOLD = '\033[1m'
   END = '\033[0m'


def pagelinks(domain):
	print colored(style.BOLD + '\n---> Finding Pagelinks:\n' + style.END, 'blue')
	time.sleep(0.3)
	try:
		req = requests.get('http://api.hackertarget.com/pagelinks/?q=%s'%(domain))
		page_links = req.content.split("\n")
		return page_links
	except: 
		print 'Connection time out.'
		return []

def main():
	domain = sys.argv[1]
	#domain pagelinks

	links=pagelinks(domain)	
	for x in links:
		print x
	print "\n-----------------------------\n"


if __name__ == "__main__":
	main()
