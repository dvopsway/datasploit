import sys
import requests
from celery import shared_task
from osint.utils import *

@shared_task
def pagelinks(domain, taskId):
	req = requests.get('http://api.hackertarget.com/pagelinks/?q=%s'%(domain))
	page_links = req.content.split("\n")
	save_record(domain, taskId, "Page Links", page_links)
	return page_links

def main():
	domain = sys.argv[1]
	#domain pagelinks
	print "\t\t\t[+] Pagelinks\n"
	links=pagelinks(domain)	
	for x in links:
		print x
	print "\n-----------------------------\n"


#if __name__ == "__main__":
	#main()
