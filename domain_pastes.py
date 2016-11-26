#!/usr/bin/env python

import config as cfg
import requests
import json
import sys
import time
import re
from termcolor import colored
class style:
   BOLD = '\033[1m'
   END = '\033[0m'


def colorize(string):
	colourFormat = '\033[{0}m'
	colourStr = colourFormat.format(32)
	resetStr = colourFormat.format(0)
	lastMatch = 0
	formattedText = ''
	for match in re.finditer(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})|/(?:http:\/\/)?(?:([^.]+)\.)?nokia\.com/|/(?:http:\/\/)?(?:([^.]+)\.)?(?:([^.]+)\.)?nokia\.com/)', string):
	    start, end = match.span()
	    formattedText += string[lastMatch: start]
	    formattedText += colourStr
	    formattedText += string[start: end]
	    formattedText += resetStr
	    lastMatch = end
	formattedText += string[lastMatch:]
	return formattedText

def google_search(domain,start_index):
	print colored(style.BOLD + '\n---> Finding Paste(s).:.\n' + style.END, 'blue')
	time.sleep(0.3)
	url="https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=\"%s\"&start=%s" % (cfg.google_cse_key, cfg.google_cse_cx, domain, start_index)
	res=requests.get(url)
	results = json.loads(res.text)
	if 'items' in results.keys():
		for x in results['items']:
			return "Title: %s\nURL: %s\nSnippet: %s\n" % (x['title'], colorize(x['link']), colorize(x['snippet']))
	elif results['error']['code'] == 403:
		return "[-] Daily Rate Limit exceeded.."
	else:
		return "No data found"
	#return json.loads(res.text)
	

def main():
	domain = sys.argv[1]
	if cfg.google_cse_key != "" and cfg.google_cse_key != "XYZ" and cfg.google_cse_cx != "" and cfg.google_cse_cx != "XYZ":
		print google_search(domain, 10)

		print "\n\n-----------------------------\n"

if __name__ == "__main__":
	main()

