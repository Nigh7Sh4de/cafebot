import tweepy
from textblob import TextBlob

# Twitter API Integration
consumer_key = 'RrIenEvIdqeczejM2QJHYHC6C'
consumer_secret = 'cLAKQFoNTiSyeH4dnKaAYIlQ8MLgWnukmBF5HSxK2dhYKmjnFM'

access_token = '2490622578-9EHuAvx1pmLSJtL29RFdv8Tm81Sl8Ki5bmRLiUu'
access_secret = 'gutWydSLUz4J1GvZ6EMfvs2XFhd59j3Pl9bBXwzqCiUtJ'

# Tweepy Authorization Handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# Create API variable
api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        analysis = TextBlob(status.text)
        analysis_sentiment = analysis.sentiment
        print(analysis_sentiment)

def lambda_function(event, context):
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=['cafebot18'])
