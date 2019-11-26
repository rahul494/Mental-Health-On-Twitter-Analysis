#######
# This python script is simply to assess how many remaining prompts/queries we can make before Twitter times us out every 15 minutes.
#######
import socket, sys, json, tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream

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
rate_limits = twitter_api.rate_limit_status()
print("\n######### SEARCH TWEET LIMIT #########")
print(str(rate_limits['resources']['search']['/search/tweets']['remaining'])+"/180 remaining.")
print("############## USER LIMIT ##############")
print(str(rate_limits['resources']['users']['/users/show/:id']['remaining'])+"/900 remaining.")
print("########## USER TIMELINE LIMIT ##########")
print(str(rate_limits['resources']['statuses']['/statuses/user_timeline']['remaining'])+"/900 remaining.")
print("#########################################\n")

