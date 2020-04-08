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

def checkCase(text):
	text = text.lower()
	return (('covid' in text) and ('positive' in text or 'new cases' in text or 'dead' in text or 'death' in text or 'deaths' in text or 'passed away' in text or 'dies' in text or 'bulletin' in text) and ('cure' not in text))

def updateTweetsInfected():
	public_tweets = api.home_timeline()
	for tweet in public_tweets:
		# print((tweet.author.name))
		# print('Tweet : {}\n\n'.format(tweet.text))
		if(checkCase(tweet.text)):#new could give bs
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
		time.sleep(60 * minutes)

if __name__ == '__main__':
	main()
