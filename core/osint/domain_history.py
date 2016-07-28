import sys
import json
import requests 
from bs4 import BeautifulSoup
import re
from celery import shared_task
from osint.utils import *

@shared_task
def netcraft_domain_history(domain, taskId):
	ip_history_dict= {}
	print "\t\t\t[+] Searching domain history in netcraft\n"
	endpoint =  "http://toolbar.netcraft.com/site_report?url=%s" % (domain)
	req = requests.get(endpoint)

	soup = BeautifulSoup(req.content, 'html.parser')
	urls_parsed = soup.findAll('a', href = re.compile(r'.*netblock\?q.*'))
	for url in urls_parsed:
		if (urls_parsed.index(url) != 0):
			ip_history_dict[str(url).split('=')[2].split(">")[1].split("<")[0]] = str(url.parent.findNext('td')).strip("<td>").strip("</td>")
	save_record(domain, taskId, "Domain History", ip_history_dict)
	return ip_history_dict


def main():
	domain = sys.argv[1]
	dns_history = netcraft_domain_history(domain)
	for x in dns_history.keys():
		print "%s: %s" % (dns_history[x], x)
	print "\n-----------------------------\n"	

#if __name__ == "__main__":
	#main()
