'''
11/23/2017
Sending tweets through the twitter api and tweepy
'''

import tweepy

from config import *

API = None
LAST_TWEETED = ""


#some unicode characters were making idle mad, let's kick them out
def BMP(s):
    return "".join((i if ord(i) < 10000 else '\ufffd' for i in s))


def get_mentions():
    global API
    mentions = tweepy.Cursor(API.mentions_timeline).items()
    mention_array = []
    
    for mention in mentions:
        user = mention.user.name
        text = BMP(mention.text)
        mention_array.append((user, text))
    return mention_array


def get_api():
    global API
    #tweepy needs that info
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    API = tweepy.API(auth)


def send_tweet(content):
    global API, LAST_TWEETED
    LOG.warning("tweeting....." + content)
    if len(LAST_TWEETED):
        status = API.update_status(content, LAST_TWEETED)
    else:
        status = API.update_status(content)
    LAST_TWEETED = status.id_str


def main():
    at = input("Who do we tweet at? ")
    say_what = input("What do we say? ")
    get_api()
    tweet = "@%s %s" % (at, say_what)
    send_tweet(tweet)
    #print(get_mentions())
    #print("Tweet sent!!")


if __name__=="__main__":
    main()
