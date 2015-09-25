import requests
from base64 import b64encode 
import json

consumer_key = "YOUR CONSUMER KEY"
consumer_secret  = "YOUR CONSUMER SECRET"
bearer_credentials = "{0}:{1}".format(consumer_key,consumer_secret).encode('ascii')
basic = 'Basic '.encode('ascii')
bearer_base64 = basic + b64encode(bearer_credentials)
header = {"Authorization": bearer_base64, "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
body = 'grant_type=client_credentials'
url = 'https://api.twitter.com/oauth2/token'

r = requests.post(url, headers=header, data=body)
token = json.loads(r.text)['access_token'].encode('ascii')

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?count=1&screen_name=camoni_cps'
bearer_str = 'Bearer '.encode('ascii')
header = { "Authorization" : bearer_str + token }
r = requests.get(url, headers=header)
print(json.loads(r.text)[0]['text'])
