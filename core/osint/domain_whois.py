from __future__ import absolute_import
from celery import shared_task

import sys
import whois

from osint.utils import *

@shared_task
def whoisnew(domain, taskId):
	print "\t\t\t[+] Gathering WhoIs Information...\n"
	try:
		whoisdata = dict(whois.whois(domain))
	except:
		whoisdata = {}		
	save_record(domain, taskId, "WHOIS Information", whoisdata)
	return whoisdata


def main():
	domain = sys.argv[1]
	print whoisnew(domain)
	print "\n-----------------------------\n"


##if __name__ == "__main__":
#	#main()
