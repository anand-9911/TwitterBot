# py -m venv env to create virtual env
import tweepy
import time

consumer_key = 'k2e5R5td9urQHTrfmnBFjbNwT'
consumer_secret = '03d63UAvmAjHKuVUmv1Dn6Mty2SeydkiBTcxcFm61SM3vEIzC2'
access_token = '4234977798-yPmVbGqvTpabnZTIUY6nTb79p8XVXwm4Ois4gjx'
access_token_secret = 'WwXIcaO47dWi6EsBNvBXY8lKD6PMy3dJSJlaiHNKv8OZg'

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
