import requests
from requests_oauthlib import OAuth1 
from urllib.parse import quote

def tsearch(keyword):
    my_API_key = "" # Fill in these strings
    my_API_key_secret = ""
    my_access_token = ""
    my_access_token_secret = ""
    auth = OAuth1(my_API_key, my_API_key_secret, my_access_token, my_access_token_secret)
    url = "https://api.twitter.com/1.1/search/tweets.json?q=" + quote(keyword)
    r = requests.get(url, auth=auth)
    r.close() # good hygiene - don't want to leave connections open for too long.
    # They might get closes from the other end, causing future calls to fail.
    # Better to make a new one each time through.
    return r
