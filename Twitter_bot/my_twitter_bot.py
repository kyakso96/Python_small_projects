import tweepy


CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
for mention in mentions:
	print(str(mention.id) + ' - ' + mention.text)
	if 'tweet tweet' in mention.text.lower():
		print('found tweet tweet')
		print('responding back...')
