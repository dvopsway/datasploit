#!/usr/bin/env python

import sys
import whois
from termcolor import colored
import time

class style:
   BOLD = '\033[1m'
   END = '\033[0m'


def whoisnew(domain):
	print colored(style.BOLD + '---> Finding Whois Information.' + style.END, 'blue')
	time.sleep(0.3)
	whoisdict = {}
	w = whois.whois(domain)
	return w


def main():
	domain = sys.argv[1]
	print whoisnew(domain)
	print "\n-----------------------------\n"


if __name__ == "__main__":
	main()
