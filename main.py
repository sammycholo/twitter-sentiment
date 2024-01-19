import os
from textblob import TextBlob
import tweepy
import sys

api_key = str(os.getenv("API_KEY"))
api_key_secret = str(os.getenv("API_KEY_SECRET"))
access_token = str(os.getenv("ACCESS_TOKEN"))
access_token_secret = str(os.getenv("ACCESS_TOKEN_SECRET"))

auth_handler = tweepy.OAuthHandler(api_key, api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler)

search_term = "spacex"
tweet_amount = 200

tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweet_amount)

polarity = 0
positive = 0
negative = 0
neutral = 0

for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(':')
        final_text = final_text[position + 2:]
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position + 2:]
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.sentiment.polarity  # Use analysis.sentiment.polarity instead of analysis.polarity
    if tweet_polarity > 0.00:
        positive += 1
    elif tweet_polarity < 0.00:
        negative += 1
    elif tweet_polarity == 0.00:
        neutral += 1
    polarity += tweet_polarity
    print(final_text)

print("Overall Polarity:", polarity)
print(f"Amount of Positive Tweets: {positive}")
print(f"Amount of Negative Tweets: {negative}")
print(f"Amount of Neutral Tweets: {neutral}")
