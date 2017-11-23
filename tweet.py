''' 11/23/2017
    Sending tweets through the twitter api and tweepy
   '''

import tweepy
import random
import os

#constants

def get_api():
    with open("secrets.txt") as f:
        secrets = f.readlines()
    f.close()

    #set authorization variables
    CONSUMER_KEY = secrets[0].strip('\n')
    CONSUMER_SECRET = secrets[1].strip('\n')
    ACCESS_TOKEN = secrets[2].strip('\n')
    ACCESS_SECRET = secrets[3].strip('\n')

    #tweepy needs that info
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def send_tweet(api, content):
    print("tweeting....." + content)
    api.update_status(content)

def main():
    at = input("Who do we tweet at?")
    at = "@"+at+" "
    say_what = input("What do we say?")

    api = get_api()

    tweet = at + say_what
    send_tweet(api, tweet)

    print("Tweet sent!!")
main()
