
import requests
import sys
import config as cfg
import clearbit
import json
import time
import hashlib
from bs4 import BeautifulSoup


def facebook_username_osint(username):
	req = requests.post('https://api.pipl.com/search/v5/?username=%s&key=sample_key' % (username))
	return json.loads(req.content)



username = sys.argv[1]
data = facebook_username_osint(username)

if 'jobs' in data['available_data']['premium'].keys():
	print data['available_data']['premium']['jobs']

