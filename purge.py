#!/usr/bin/env python
# *-* coding: utf-8 *-*

from twitterings import Base

twitter = Base()

for account in twitter.api.friends_ids():
	print 'Total Following Count: %s' % twitter.api.me().friends_count
	twitter.api.destroy_friendship(id=account)
