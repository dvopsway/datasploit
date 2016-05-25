import requests
import json
import sys
import config as cfg

def get_accesstoken_zoomeye(domain):
	username = cfg.zoomeyeuser
	password = cfg.zoomeyepass
	datalogin = '{"username": "%s","password": "%s"}' % (username, password)
	s = requests.post("https://api.zoomeye.org/user/login", data=datalogin)
	responsedata = json.loads(s.text)
	access_token1 = responsedata['access_token']
	return access_token1


def search_zoomeye(domain):
	print "\t\t\t[+] Checking %s on Zoomeye" % (domain) 
	zoomeye_token = get_accesstoken_zoomeye(domain)
	authData = {"Authorization": "JWT " + str(zoomeye_token)}
	req = requests.get('http://api.zoomeye.org/web/search/?query=site:nokia.com&page=1', headers=authData)
	return req.text
	

def main():
	domain = sys.argv[1]
	#checks results from zoomeye
	#filters need to be applied
	zoomeye_results = search_zoomeye(domain)
	dict_zoomeye_results = json.loads(zoomeye_results)
	print dict_zoomeye_results
	print "\n-----------------------------\n"

if __name__ == "__main__":
	main()
