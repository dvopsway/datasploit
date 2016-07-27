import requests
import json
from bs4 import BeautifulSoup
import sys
import re
from celery import shared_task
from osint.utils import *

@shared_task
def boardsearch_forumsearch(domain, taskId):
	req = requests.get('http://boardreader.com/index.php?a=l&q=%s&d=0&extended_search=1&q1=%s&ltype=all&p=50'%(domain,domain))
	soup=BeautifulSoup(req.content, "lxml")
	text=soup.findAll('bdo',{"dir":"ltr"})
	links={}
	for lk in text:
		links[lk.text]=re.search("'(.+?)'", lk.parent['onmouseover']).group(1)
	save_record(domain, taskId, "Forum Search", links)
	return links


def main():
	domain = sys.argv[1]
	print "\t\t\t[+] Associated Forum Links\n"
	links=boardsearch_forumsearch(domain)
	for tl,lnk in links.items():
		print "%s (%s)" % (lnk, tl)
	print "\n-----------------------------\n"


#if __name__ == "__main__":
	#main()
