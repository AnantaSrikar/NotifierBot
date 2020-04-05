import tweepy
import json
import time

def getTokens():
	allTokens = json.load(open('res/TOKENS.json', 'r'))
	return allTokens

minutes = 1

auth = tweepy.OAuthHandler(getTokens()["API_key"], getTokens()["API_secret_key"])
auth.set_access_token(getTokens()["access_token"], getTokens()["access_token_secret"])

api = tweepy.API(auth, wait_on_rate_limit = True)

def updateTweetsInfected():
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

def updateTweetsDead():
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		if('dead' in tweet.text or 'death' in tweet.text or 'deaths' in tweet.text or 'passed away' in tweet.text or 'dies' in tweet.text):
			try:
				tweet.retweet()
			except Exception as e:
				print('Exception : {}'.format(e))
				print('Tweet : {}\n\n'.format(tweet.text))

# tweetText = input('Enter the tweet :')

# api.update_status(tweetText))

def main():
	while True:
		updateTweetsInfected()
		time.sleep(5)
		updateTweetsDead()
		time.sleep(60 * minutes)

if __name__ == '__main__':
	main()
