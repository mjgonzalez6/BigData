import json
import pymongo
import tweepy

# Variables that contains the user credentials to access Twitter API
access_key = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        self.db = pymongo.MongoClient().carga_icc1002

    def on_data(self, tweet):
        self.db.icccualquiercosa.insert(json.loads(tweet))

    def on_error(self, status_code):
        return True  # Don't kill the stream

    def on_timeout(self):
        return True  # Don't kill the stream


for x in range(1, 1000):
    try:
        sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
        sapi.filter(track=['trump'])
    except Exception as e:
        print 'retrying'
