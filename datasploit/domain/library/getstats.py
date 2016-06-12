import sys
import whois

def whoisnew(domain):
	print "\t\t\t[+] Gathering WhoIs Information...\n"
	whoisdict = {}
	w = whois.whois(domain)
	return w
