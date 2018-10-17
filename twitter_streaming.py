# coding=utf-8
# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library

import tweepy
import datetime
from googletrans import Translator

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''

chaines_id = [192, 4, 80, 34, 47, 118, 111, 445, 119, 195, 446, 444, 78, 481, 226, 458, 482, 160, 1404, 1401, 1403, 1402, 1400, 1399, 112, 2111]

chaines_name = ["TF1", "France 2", "France 3", "Canal+", "France 5", "M6", "Arte", "C8", "W9", "TMC", "TFX", "NRJ 12", "France 4", "BFM TV", "CNews", "CStar", "Gulli", "France O", "TF1 Series Films", "L'equipe"$

now = datetime.datetime.now()

day = now.strftime("%Y-%m-%d")
translator = Translator()
final_text = []
print now.strftime("%B")
final_text.append("Programme  TV du " + str(now.day) + " " + translator.translate(now.strftime("%B"), dest='fr').text + " " + str(now.year))
for count in range (0, len(chaines_id)):
    filename = "dates_" + str(day) + "_id_chaines_" + str(chaines_id[count]) + ".json"
    file_object = open(filename, "r")
    file_content = file_object.read()
    file_content = json.loads(file_content)
    for emission in file_content["donnees"]:
        if emission["prime_time"] == 1:
            final_text.append(chaines_name[count] + " : " + emission["titre"])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
text_to_display = []
text_to_display.append("")
block = 0
i = 0

for text in final_text:
     if len(text) + len(text_to_display[i]) >= 280:
         text_to_display.append("")
         i += 1
     else:
         text_to_display[i] += text
         text_to_display[i] += "\n"

text = ""
for text in text_to_display:
    if block == 0:
        api.update_status(text)
        block = 1
    else:
        public_tweets = api.home_timeline()
        id_last_tweet = public_tweets[0].id
        api.update_status(text, in_reply_to_status_id = id_last_tweet)

