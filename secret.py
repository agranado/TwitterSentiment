import tweepy #The Twitter API

consumer_key = 'YhBVEIRyVNqrn3hr8YTQGU2cM'
consumer_secret = 'tQlfvhML9EIOMyKDeMgHIfWZS8gXMv4LbJp4w7xHZ6jUigYMYB'
access_token = '1076160163722248193-Akv2lZjA6S1mqG9ClFgU3ABu74Dw7b'
access_token_secret = '9VvNgdD8xQKqm9TZSE9dSTkmC9uthUWzwIexGVS2H7ozh'

def get_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return(auth)
