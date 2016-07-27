#import config as cfg
import requests
import json
import sys
from celery import shared_task
from osint.utils import *
import config

@shared_task
def emailhunter(domain, taskId):
	odomain = domain.replace("www.", "")
	if config.emailhunter:
		collected_emails = []
		url="https://api.emailhunter.co/v1/search?api_key=%s&domain=%s" % (config.emailhunter, odomain)
		res=requests.get(url)
		parsed=json.loads(res.text)
		if 'emails' in parsed.keys():
			for email in parsed['emails']:
				collected_emails.append(email['value'])
		save_record(domain, taskId, "Email Hunter", collected_emails)
		return collected_emails
	else:
		return []

def main():
	domain = sys.argv[1]
	api_key = "6c132ef72b64c40d64882b8fd4d0edfd7741d481"
	if api_key != "":
		collected_emails = emailhunter(domain)
		print "\t\t\t[+] Finding Email Ids\n"
		for x in collected_emails:
			print str(x) + ", ",
		print "\n\n-----------------------------\n"


if __name__ == "__main__":
	main()
