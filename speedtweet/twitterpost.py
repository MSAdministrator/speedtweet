import os
import requests
import tweepy
import random

from .littlebirdy import LittleBirdy

class TwitterPost(LittleBirdy):

    _TWEET = '''{account} I am experiencing issues with my internet. My speed is at {down} MB/s Down & {up} MB/s Up. 
This is {percent}% below what I am paying for.
'''
    
    def post(self, down_speed, up_speed, percent):
        auth = tweepy.OAuthHandler(
            self.config['twitter_consumer_key'],
            self.config['twitter_consumer_secret']
        )
        auth.set_access_token(
            self.config['twitter_access_token'],
            self.config['twitter_access_token_secret']
        )
        self.api = tweepy.API(auth)
        try:
            tweet = self._TWEET.format(
                account=self.config['speedtweet_at_account'],
                down=down_speed,
                up=up_speed, 
                percent=percent
            )
            self.api.update_status(tweet)
        except:
            self.post(down_speed, up_speed, percent)
