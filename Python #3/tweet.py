'''
Created on Sep 14, 2013

@author: Sai Chaitanya
'''
from __future__ import unicode_literals
import sys
import http.client
import urllib
from urllib.error import HTTPError
from urllib.request import http
from urllib.request import urlopen
import requests
from requests_oauthlib import OAuth1
from urllib.parse import parse_qs
#Connecting to Twitter API
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "h39lst85AG9uJu7kKPsWiw"
CONSUMER_SECRET = "jHBFJAcE7HAGHwrpOKYXKkoGWddqk7srJ8eeebyI"

OAUTH_TOKEN = "53001055-KcTGe18A5FI62oNayIe7y4CBpaFOMzMStD3HNEw"
OAUTH_TOKEN_SECRET = "wDh40jn30CRU9KMCN3s4dE3pZpsHa0MrdTonthHDRo"


def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)

    credentials = parse_qs(r.content)

    resource_owner_key = credentials[b'oauth_token'][0].decode(encoding='UTF-8')
    resource_owner_secret = credentials[b'oauth_token_secret'][0].decode(encoding='UTF-8')
    
    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print('Please go here and authorize: ' + authorize_url)
    
    verifier = input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials[b'oauth_token'][0].decode(encoding='UTF-8')
    secret = credentials[b'oauth_token_secret'][0].decode(encoding='UTF-8')

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print( "OAUTH_TOKEN: " + token )
        print( "OAUTH_TOKEN_SECRET: " + secret )
        print( )
    else:
        oauth = get_oauth()
        #opening a file to capture the data  from the r.json()
        f= open('tweet9.txt','w', encoding='utf-8')
        #Querying Api using Oauth authentication
        r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23zuckerberg%20filter%3Alinks&include_entities=true&count=1000", auth=oauth)
        #Json format
        data= r.json()
        print(type(data)) #Printing the format of the data
        f.write(str(data)) # converting into string to load into the file
        print(data.keys()) # Keys in the data load
        print(data['statuses'][0])   
        i=0
        g= open('urls.txt','w', encoding='utf-8')
        while (i < len(data['statuses'])):
                urls= data['statuses'][i]['entities']['urls']
                i+=1
                
                for url in urls:
                        new_url = url["url"]
                       
                        #print(new_url)
                        #headers={'User-Agent' : "Magic Browser"}
                        request = urllib.request.Request(new_url) 
                        try:    
                            response = urlopen(request)
                        except HTTPError as e:
                            print (response.geturl())
                            print (response.info())
                            print (response.getcode())
                            
                        else:
                            print (response)
                            print (response.info())
                            print (response.getcode())
                            print (response.geturl())
                            #return response
                        #m= requests.head(new_url)
                        
                        #print(m)
                        #Handling url redirects from display url (t.co) to actual url
                        
                        #opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler)
                        #fg = opener.open(request)
                        #print(fg.url)
                        
                        
                        #if m.status_code=='200':
                            #g.write(m)
                            #print(format(m.url))
                             
                        #elif m.status_code in range (300,400):
                            #print(format(m.headers['location']))
                        #else:
                            #print(format(m.status_code))
        g.close()