import sys
import requests
from bs4 import BeautifulSoup
import json


def github_search(query, code):
	print "\t\t\t[+] Searching domain results in github" + code + ":" + query + "\n"
	endpoint_git =  "https://github.com/search?q=\"" + query + "\"&type=" + code
	req = requests.get(endpoint_git) 
	soup = BeautifulSoup(req.content, 'html.parser')
	mydivs = soup.findAll("span", { "class" : "counter" })
	return "%s Results found in github Codes. \nExplore results manually: %s" % (str(mydivs[0]).split(">")[1].split("<")[0], endpoint_git)


def main():
	domain = sys.argv[1]
	#make Search github code for the given domain.
	print github_search(domain, 'Code')
	print "\n-----------------------------\n"


if __name__ == "__main__":
	main()
