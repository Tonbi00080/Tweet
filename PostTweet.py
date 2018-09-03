#coding:utf-8
from requests_oauthlib import OAuth1Session
import json, config

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
# ツイート投稿用のURL
url_text = "https://api.twitter.com/1.1/statuses/update.json"


print("何をつぶやきますか？")
tweet = input('>> ')
print('-----------------------------------')

# ツイート本文
params = {"status": tweet}

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, ATS)
req = twitter.post(url_text, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
