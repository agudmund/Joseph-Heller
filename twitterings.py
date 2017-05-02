#!/usr/bin/env python
# *-* coding: utf-8 *-*

from tweepy import OAuthHandler,API,Stream
from tweepy.streaming import StreamListener

class Base:
	def __init__(self, name=None, keyfile=None):
		self.name = 'Joseph Heller'
		self.auth = OAuthHandler('Bn5Jnz1mf3JXBHAM7XvgbJMnH', 'WSbrPB3N5cIJaHM36LEiUaEywA8k6Zzi89hxoIekjr139pnXV1')
		self.auth.set_access_token('853559235745107968-EXQDyL2bbbsAkof0xW5u2fg08rYwErE', 'fToyRaNywUAe5T4ShSGo6dnDLQfgnkETiE9fOfc2KwG6s' )
		self.api = API(self.auth)
		self.me = self.api.me()
		self.listen = StdOutListener()
		self.stream = Stream(self.auth, self.listen)

class StdOutListener(StreamListener):

	def on_data(self, data):
		print data

		return True

	def on_error(self, status):
		print status

		return False


if __name__ == '__main__':
	twitter = Base()