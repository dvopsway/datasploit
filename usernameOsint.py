import requests
import sys
import config as cfg
import clearbit
import json
import time
import hashlib
from bs4 import BeautifulSoup


def git_user_details(username):
	req = requests.get("https://api.github.com/users/%s" % (username))
	return json.loads(req.content)

	'''to add few more stuff
	https://api.github.com/users/anantshri/orgs
	https://api.github.com/search/issues?q=type:pr+is:merged+author:anantshri&per_page=100
	https://api.github.com/users/anantshri/starred?per_page=100&page
	https://api.github.com/users/anantshri/repos?per_page=100

	'''


def usernamesearch(username):
	data = {"username":username}
	req = requests.post('https://usersearch.org/results_normal.php',data=data, verify=False)
	soup=BeautifulSoup(req.content, "lxml")
	atag=soup.findAll('a',{'class':'pretty-button results-button'})
	profiles=[]
	for at in atag:
		 if at.text=="View Profile":
			profiles.append(at['href'])
	return profiles



username = sys.argv[1]


print "\t\t\t[+] Checking git user details\n"
git_data = git_user_details(username)
print "Login: %s" % git_data['login']
print "avatar_url: %s"  % git_data['avatar_url']
print "id: %s" % git_data['id']
print "Repos: %s" % git_data['repos_url']
print "Name: %s" % git_data['name']
print "Company: %s" % git_data['company']
print "Blog: %s" % git_data['blog']
print "Location: %s" % git_data['location']
print "Hireable: %s" % git_data['hireable']
print "Bio: %s" % git_data['bio']
print "On GitHub: %s" % git_data['created_at']
print "Last Activity: %s" % git_data['updated_at']
print "\n-----------------------------\n"




print "\n\t\t\t[+] Username found on:\n"
links=usernamesearch(username)
for lnk in links:
	print lnk
print "\n-----------------------------\n"


