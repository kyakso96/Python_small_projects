import tweepy


CONSUMER_KEY = 'ay4mtr53VVqzemWBZi6LF2DTL'
CONSUMER_SECRET = '0Vpwe9Mm9Fqxdp5WsK1kNlJYxw7BCTxUyl4k5Kak87hSWs9h7O'
ACCESS_KEY = '1547723601482199045-Rg4O1MQ7jN0IJzEY5xtnL7H3xJ8xrM'
ACCESS_SECRET = 'ubNjLJzN9MhCfDvs86vkF1gJkI9sbJsJjv82RgWvYn1wV'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
for mention in mentions:
	print(str(mention.id) + ' - ' + mention.text)
	if 'tweet tweet' in mention.text.lower():
		print('found tweet tweet')
		print('responding back...')
