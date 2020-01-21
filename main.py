# py -m venv env to create virtual env
import tweepy
import time



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()
# print(user.name)# followers count and screen name.
# super Generous Bot


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)
    # except StopIteration:
    #     break


for follower in limit_handler(tweepy.Cursor(api.lists_all).pages()):
    try:
        print(follower.name)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        print("BREAK THE PROGRM")
