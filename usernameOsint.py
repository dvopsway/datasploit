import requests
import sys
import config as cfg
import clearbit
import json
import time
import hashlib
from bs4 import BeautifulSoup

import os
import urllib
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

def profilepic(urls):
	
	imglinks=[]
	if len(urls) or git_data['avatar_url']:
		if not os.path.exists(username):
			os.makedirs(username)
	if git_data['avatar_url']:
		path=username+"/github.jpg"
		urllib.urlretrieve(git_data['avatar_url'], path)
	for url in urls:
		if 'etsy' in url:
			res=requests.get(url)
			soup=BeautifulSoup(res.content,"lxml")
			img=soup.find('meta',{'property':'og:image'})
			imglinks.append(img['content'])
			path=username+"/etsy.jpg"
			urllib.urlretrieve(img['content'], path)
			
			continue
		elif 'gravatar' in url:
			try:
				res=requests.get(url)
				soup=BeautifulSoup(res.content,"lxml")
				img=soup.find('a',{'class':'photo-0'})
				imglinks.append(img['href'])
				path=username+"/gravatar.jpg"
				urllib.urlretrieve(img['href'], path)
				continue
			except KeyError:
				pass
		elif 'youtube' in url:
			try:
				res=requests.get(url)
				soup=BeautifulSoup(res.content,"lxml")
				img=soup.find('link',{'itemprop':'thumbnailUrl'})
				imglinks.append(img['href'])	
				path=username+"/youtube.jpg"
				urllib.urlretrieve(img['href'], path)
				continue
			except KeyError:
				pass
		elif 'twitter' in url:
			res=requests.get(url)
			soup=BeautifulSoup(res.content,"lxml")
			img=soup.find('img',{'class':'ProfileAvatar-image'})
			imglinks.append(img['src'])
			path=username+"/twitter.jpg"
			urllib.urlretrieve(img['src'], path)
			continue			
		elif 'photobucket' in url:
			res=requests.get(url)
			soup=BeautifulSoup(res.content,"lxml")
			img=soup.find('img',{'class':'avatar smallProfile'})
			imglinks.append(img['src'])
			path=username+"/photobucket.jpg"
			urllib.urlretrieve(img['src'], path)
			continue
		elif 'pinterest' in url:
			res=requests.get(url)
			soup=BeautifulSoup(res.content,"lxml")
			img=soup.find('meta',{'property':'og:image'})
			imglinks.append(img['content'])
			path=username+"/pinterest.jpg"
			urllib.urlretrieve(img['content'], path)
			continue
		elif 'ebay' in url:
			res=requests.get(url)
			soup=BeautifulSoup(res.content,"lxml")
			img=soup.find('img',{'class':'prof_img img'})
			imglinks.append(img['src'])
			path=username+"/ebay.jpg"
			urllib.urlretrieve(img['src'], path)
			continue
		elif 'deviantart.' in url:
			res=requests.get(url)
			soup=BeautifulSoup(res.content,"lxml")
			img=soup.find('img',{'class':'avatar float-left'})
			imglinks.append(img['src'])
			path=username+"/deviantart.jpg"
			urllib.urlretrieve(img['src'], path)
			continue
		
	return imglinks

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

imagelinks=profilepic(links)
imagelinks.append(git_data['avatar_url'])
print "\t\t\t[+] Finding Profile Pics\n"
for x in imagelinks:
	print x
print "\n\n-----------------------------\n"
