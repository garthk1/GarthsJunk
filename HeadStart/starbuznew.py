import urllib.request
import time
import sys


def get_price():
    page = urllib.request.urlopen("http://beans.itcarlow.ie/prices-loyalty.html")
    text = page.read().decode("utf8")
    where = text.find(">$")
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])


def send_to_twitter(msg):
    import tweepy
    CONSUMER_KEY = 'v45o0k7HCbpETKNrFJ1cfg'
    CONSUMER_SECRET = 'q20vHmxtiDM2a2sVYiOmLViVeJ2VveiTltKyAzjIymk'
    ACCESS_KEY = '277699969-FmuV8YsIfmeiwdz9B3qSRNHnix6aImwR6NPFb78a'
    ACCESS_SECRET = 'iugpTjwE0pP3FQ19BDn1K9oO84KNaax8ZldDB13xOWzR0'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status(msg)

# price = float(get_price())

price_now = input("Welcome, would you like to know the current price? Y/N ")

if price_now == "Y":
    print(get_price())
    send_to_twitter(get_price())
else:
    price = 99.99
    while price > 4.74:
        time.sleep(900)
        price = get_price()
    print("Buy!")

