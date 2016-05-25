
import config as cfg
import requests
import json
import sys


collected_emails = []

def emailhunter(domain):
	url="https://api.emailhunter.co/v1/search?api_key=%s&domain=%s" % (cfg.emailhunter, domain)
	res=requests.get(url)
	parsed=json.loads(res.text)
	for email in parsed['emails']:
		collected_emails.append(email['value'])

def main():
	domain = sys.argv[1]
	emailhunter(domain)
	print "\t\t\t[+] Finding Email Ids\n"
	for x in collected_emails:
		print str(x) + ", ",
	print "\n\n-----------------------------\n"


if __name__ == "__main__":
	main()
