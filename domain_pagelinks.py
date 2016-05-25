import sys
import requests


def pagelinks(domain):
	req = requests.get('http://api.hackertarget.com/pagelinks/?q=%s'%(domain))
	page_links = req.content.split("\n")
	return page_links

def main():
	domain = sys.argv[1]
	#domain pagelinks
	print "\t\t\t[+] Pagelinks\n"
	links=pagelinks(domain)	
	for x in links:
		print x
	print "\n-----------------------------\n"


if __name__ == "__main__":
	main()
