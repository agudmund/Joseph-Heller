#!/usr/bin/env python
# *-* coding: utf-8 *-*

import sys
import json
import tweepy
from time import sleep
from random import choice,randint
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import API

class StdOutListener(StreamListener):

    def on_data(self, data):

        result = json.loads(data)
        twitter.api.create_friendship(result['user']['screen_name'])
        for n in [ n for n in result['entities']['user_mentions']]:
        	if not n==[]:
        		twitter.api.create_friendship(n['screen_name'])

        return True

    def on_error(self, status):
        print status

class Twitterings:
	def __init__(self):
		self.name = 'Jospeh Heller'
		self.auth = OAuthHandler('Bn5Jnz1mf3JXBHAM7XvgbJMnH', 'WSbrPB3N5cIJaHM36LEiUaEywA8k6Zzi89hxoIekjr139pnXV1')
		self.auth.set_access_token('853559235745107968-EXQDyL2bbbsAkof0xW5u2fg08rYwErE', 'fToyRaNywUAe5T4ShSGo6dnDLQfgnkETiE9fOfc2KwG6s' )
		self.api = tweepy.API(self.auth)
		self.me = self.api.me()
		self.listen = StdOutListener()
		self.stream = Stream(self.auth, self.listen)

if __name__ == '__main__':
	twitter = Twitterings()
	twitter.stream.filter(track=sys.argv[1:])
