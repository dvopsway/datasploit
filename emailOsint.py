import requests
import sys
import config as cfg
import clearbit
import json
import time
import hashlib
from bs4 import BeautifulSoup
import re

email = sys.argv[1]
print email


def haveIbeenpwned(email):
	print "\t\t\t[+] Checking on Have_I_Been_Pwned...\n"
	req = requests.get("https://haveibeenpwned.com/api/v2/breachedaccount/%s" % (email))
	return req.content


def clearbit(email):
	print "s"
	header = {"Authorization" : "Bearer %s" % (cfg.clearbit_apikey)}
	req = requests.get("https://person.clearbit.com/v1/people/email/%s" % (email), headers = header)
	person_details = json.loads(req.content)
	if ("error" in req.content and "queued" in req.content):
		time.sleep(20)
		clearbit(email)
	else:
		return person_details

def gravatar(email):
	gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() 
	return gravatar_url

def emaildom(email):
	req = requests.get('http://www.whoismind.com/email/%s.html'%(email))
	soup=BeautifulSoup(req.content, "lxml")
	atag=soup.findAll('a')
	domains=[]
	for at in atag:
		if at.text in at['href']:
			domains.append(at.text)
	domains=set(domains)
	return domains

def emailslides(email):
	req = requests.get('http://www.slideshare.net/search/slideshow?q=%s'%(email))
	soup=BeautifulSoup(req.content, "lxml")
	atag=soup.findAll('a',{'class':'title title-link antialiased j-slideshow-title'})
	slides={}
	for at in atag:
		slides[at.text]=at['href']
	return slides

def emailscribddocs(email):
	req = requests.get('https://www.scribd.com/search?page=1&content_type=documents&query=%s'%(email))
	soup=BeautifulSoup(req.content, "lxml")
	m = re.findall('(?<=https://www.scribd.com/doc/)\w+', req.text.encode('UTF-8'))
	m = set(m)
	m = list(m)
	links=[]
	length=len(m)
	for lt in range(0,length-1):
		links.append("https://www.scribd.com/doc/"+m[lt])
	return links
	
	
print haveIbeenpwned(email)
print "\n-----------------------------\n"

print "\t\t\t[+] Finding user information based on emailId\n"
print clearbit(email)
print "\n-----------------------------\n"

print "\t\t\t[+] Gravatar Link\n"
print gravatar(email)
print "\n-----------------------------\n"

print "\t\t\t[+] Associated Domains\n"
for doms in emaildom(email):
	print doms
print "\n-----------------------------\n"

print "\t\t\t[+] Associated Slides\n"
slds=emailslides(email)
for tl,lnk in slds.items():
	print tl+"http://www.slideshare.net"+lnk
print "\n-----------------------------\n"

print "\t\t\t[+] Associated Scribd Docs\n"
scdlinks=emailscribddocs(email)
for sl in scdlinks:
	print sl
	print "\n"
print "\n"
print "More results might be available:"
print "https://www.scribd.com/search?page=1&content_type=documents&query="+email
print "\n-----------------------------\n"