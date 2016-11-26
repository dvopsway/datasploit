#!/usr/bin/env python

import sys
import dns.resolver
from termcolor import colored
class style:
   BOLD = '\033[1m'
   END = '\033[0m'

def fetch_dns_records(domain,rec_type):
	try:
		answers = dns.resolver.query(domain, rec_type)
		rec_list = []
		for rdata in answers:
			rec_list.append(rdata)
		return rec_list
	except:
		return colored("No Records Found", 'red')


def parse_dns_records(domain):
	print colored(style.BOLD + '---> Finding DNS Records.\n' + style.END, 'blue')
	dict_dns_record = {}
	dict_dns_record['SOA Records'] = fetch_dns_records(domain,"SOA")
	dict_dns_record['MX Records'] = fetch_dns_records(domain,"MX")  	
	dict_dns_record['TXT Records'] = fetch_dns_records(domain,"TXT")
	dict_dns_record['A Records'] = fetch_dns_records(domain,"A")
	dict_dns_record['Name Server Records'] = fetch_dns_records(domain,"NS")
	dict_dns_record['CNAME Records'] = fetch_dns_records(domain,"CNAME")
	dict_dns_record['AAAA Records'] = fetch_dns_records(domain,"AAAA")
	return dict_dns_record


def main():
	domain = sys.argv[1]
	dns_records = parse_dns_records(domain)
	for x in dns_records.keys():
		print x
		if "No" in dns_records[x] and "Found" in dns_records[x]:
			print "\t%s" % (dns_records[x])
		else:
			for y in dns_records[x]:
				print "\t%s" % (y)
			#print type(dns_records[x])
	print "\n-----------------------------\n"

if __name__ == "__main__":
	main()
