import requests
import sys
import config as cfg
import clearbit
import json
import time


username=sys.argv[1]

def insta_user_details(username):
	req = requests.get("https://api.instagram.com/v1/users/search?q=%s&count=999&access_token=%s" % (username, cfg.instagram_token))
	ret_req = json.loads(req.content)
	user_details = ret_req['data'][0]
	return user_details

def find_insta_media_by_userId(userId):
	url = "https://api.instagram.com/v1/users/%s/media/recent?&access_token=%s&count=999" % (userId, cfg.instagram_token)
	req = requests.get(url)
	ret_req = json.loads(req.content)
	media_data = ret_req['data']
	return media_data

def find_location_if_any_instaUser(media_data):
	location_data = []
	for x in media_data:
		user_location = x['location']
		if user_location is None:
			pass
		else:
			user_location['timestamp'] = x['caption']['created_time']
			location_data.append(user_location)
	return location_data

userId = insta_user_details(username)['id']
fullname = insta_user_details(username)['full_name']
print "Name: %s\nUserId: %s" % (fullname,userId)

media_data = find_insta_media_by_userId(userId)

print find_location_if_any_instaUser(media_data)
