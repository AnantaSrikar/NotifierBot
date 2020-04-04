import tweepy
import json

def getTokens():
	allTokens = json.load(open('res/tokens.json', 'r'))
	return allTokens

auth = tweepy.OAuthHandler(getTokens()["API_key"], getTokens()["API_secret_key"])
auth.set_access_token(getTokens()["access_token"], getTokens()["access_token_secret"])

api = tweepy.API(auth, wait_on_rate_limit = True)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	# print((tweet.author.name))
	# print('Tweet : {}\n\n'.format(tweet.text))
	if('COVID-19' in tweet.text or 'Covid19' in tweet.text or 'positive' in tweet.text):
		try:
			tweet.retweet()
		except Exception as e:
			print('Exception : {}'.format(e))
			print('Tweet : {}\n\n'.format(tweet.text))

# tweetText = input('Enter the tweet :')

# api.update_status(tweetText)

user = api.me()
print('Screen name : {}'.format(user.screen_name))
print('Followers count : {}'.format(user.followers_count))
for friend in user.followers():
   print('Follower : {}'.format(friend.screen_name))