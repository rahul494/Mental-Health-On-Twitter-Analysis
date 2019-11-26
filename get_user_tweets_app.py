#######
# This python script gets Tweets from specific users who have specifically diagnosed having a particular mental illness/problem. It uses the Tweepy library to get up to 200 Tweets per user.
#######

import sys, json, csv, tweepy, re, nltk, time
from tweepy import OAuthHandler
from tweepy import API

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
f = open("user_id_sample_abused.txt", "r+")

# A function that removes unwanted information from tweets:
def preProcessTweet(tweet_text):
    tweet_text_useful = ""
    tweet_text = re.sub(r'https:\S+', '', tweet_text) # Removes link.
    tweet_text = re.sub(r'@[a-zA-Z0-9_]{1,15}', '', tweet_text)
    tweet_text = re.sub(r'[^\w\s]', '', tweet_text)
    for word in tweet_text.split(): 
        word = word.lower() # Makes it lowercase.
        if word not in stopWords and len(word) > 1: # Removes stopwords and single chars
            tweet_text_useful = tweet_text_useful + " " + word
    return tweet_text_useful

# For every user we stored in the file earlier, we get 200 of their tweets.
i = 0
with open('tweets_per_abused_user.csv','w') as csvStorage:
    # To write the tweets of a user to a .CSV file.
    csv_writer = csv.writer(csvStorage)
    for user in f:
        # We get the username.
        user = user.split("\n")[0]
        try:
            # If they're tweet isn't empty after processing, we add it to the .CSV
            for item in twitter_api.user_timeline(screen_name=user,count=250,include_rts=False):
                tweet_text = item.text
                tweet_text_useful = preProcessTweet(tweet_text)
                if tweet_text_useful != "":
                    csv_writer.writerow([user, tweet_text_useful])
            i = i + 1
            # Helps keep track of the iterations as this query can run for hours.
            print("User complete: " + user + " at the " + str(i) + "-th iteration.")
        except tweepy.TweepError as  e:
            # This is exception handling for when Twitter times us out. We just wait and try every 60 seconds until we're timed back in
            time.sleep(60)
            print("Some error: " + str(e))
            continue
            