#######
# This Python script uses the Twitter API/Tweepy function call 'Search' to get usernames that have tweeted a certain query such as "I have depression", "I am suicidal" or "I have been abused"
#######

import sys
import json
import csv
import tweepy
from tweepy import OAuthHandler
from tweepy import API
import re
import nltk
import time

# Setting up stopwords:
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))

# Setting up the serial keys and stuff:
consumer_key="skrtPlkUrqc3zqskPiup0Hl30"
consumer_secret="og2hCbNeWkhihoiLuIIJo1jY9qJcUPboHNVRO4FE6K0rTCqSLS"
access_token="785116862-zT7wQtAefZQe7RY2Ni1kODUGpfrk5rIjPPXpM2CK"
access_token_secret="xJRFeS1W40WCkRVdeqPTZaAwjKO266ndRxoaQP2R99Tnh"

# Setting up authenticati--kokokon and handling:
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creating the API object:
twitter_api = API(auth_handler=auth)

# Setting up the file that we write the user_ids to:
f = open("test.txt", "w+")

# Setting up the Tweet query to use
query = "I am depressed"

while True:
    try:
        for item in twitter_api.search(q=query,count=100,include_rts=False):
            print(item.screen_name)
    except tweepy.TweepError as  e: # In case of an error, it will re-attempt in 60 seconds.
        time.sleep(60) 
        print("Some error: " + str(e))
        continue
    
f.close()
            