import sys
import whois

def whoisnew(domain):
	whoisdict = {}
	w = whois.query(domain)
	return w
