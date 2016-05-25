import requests
import sys
import json

ip_address = sys.argv[1]

def find_neighbours(ip_address):
	print "\t\t\t[+]Finding neighbours for %s" % (ip_address)
	list_repos = []
	url = "http://api.hackertarget.com/reverseiplookup/?q=%s" % (ip_address)
	req = requests.get(url)
	return req.content.split("\n")

def main():
	for x in find_neighbours(ip_address):
		print x

if __name__ == "__main__":
	main()