''' 11/23/2017
    Sending tweets through the twitter api and tweepy
   '''

import tweepy
import random
import os

from config import *

#constants
test_acct = False
api = ""
last_tweeted = ""

#some unicode characters were making idle mad, let's kick them out
def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))

def get_mentions():
    mentions = tweepy.Cursor(api.mentions_timeline).items()
    mention_array = []
    
    for mention in mentions:
        user = mention.user.name
        mention = BMP(mention.text)
        mention_array.append(user+" -- "+mention)
    return mention_array

def get_api(test_acct):
    secrets = LAP_SECRETS
    if(test_acct):
        secrets = DEV_SECRETS

    #set authorization variables
    CONSUMER_KEY = secrets["CONSUMER_KEY"]
    CONSUMER_SECRET = secrets["CONSUMER_SECRET"]
    ACCESS_TOKEN = secrets["ACCESS_TOKEN"]
    ACCESS_SECRET = secrets["ACCESS_SECRET"]

    #tweepy needs that info
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    global api
    api = tweepy.API(auth)

def send_tweet(content, reply_to = ""):
    print("tweeting....." + content)
    if len(reply_to):
        status = api.update_status(content, reply_to)
    else:
        status = api.update_status(content)
    global last_tweeted
    last_tweeted = status.id_str

def main():
    test = input("Is this a dev test? (True or False) ")
    at = input("Who do we tweet at? ")
    at = "@"+at+" "
    say_what = input("What do we say? ")

    global test_acct
    if(test == "True"):
        test_acct = True
    get_api(test_acct)
    
    tweet = at + say_what
    send_tweet(tweet, last_tweeted)
    #print(get_mentions())
    #print("Tweet sent!!")
main()
