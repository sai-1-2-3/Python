'''
Created on Aug 11, 2014

@author: Sai Chaitanya
'''

# Run the program by passing an argument <abc.py> arg_url
# parse the url and search for a string/url and get the list of urls
# append the urls to domain name to get the final result
import sys
from bs4 import BeautifulSoup
import re
from urllib2 import urlopen
print ("Argument Provided:" , sys.argv[1]) #argv[0] name of the script
#Printing url info provided at the cli argument
raw_url = sys.argv[1]
#============================================================================================================
if raw_url == 'http://calendar.boston.com/lowell_ma/events/show/274127485-mrt-presents-shakespeares-will':     #Store the argument/url in a variable
    dn_name = 'http://calendar.boston.com'                                                                     #grab the parent url for appending
    soup = BeautifulSoup(urlopen(raw_url).read())                                                              #Read the html response
    result = ''.join([dn_name + events['href'] for events in soup.findAll('a', {"class": "z-listing-module-more"})])  #Filter the url based on the class
    grab_url = BeautifulSoup(urlopen(result).read())                                                             #Parse the url grabbed
    result   = [dn_name + link['href'] for link in grab_url.findAll('a', href=re.compile('\/show'))]             # Grabs the valid urls by filtering using regex on show
    print("List of Valid event urls\n" +"\n".join(list(set(result))))
#===========================================================================================================
#Grab the html response and parse
#Filter on class
#Get all the urls from the html response 
#Finally append it to the grabbed strings
elif raw_url == 'http://www.sfmoma.org/exhib_events/exhibitions/513':
    dn_name = 'http://www.sfmoma.org'
    soup = BeautifulSoup(urlopen(raw_url).read())
    print("list of Events for members")
    for link in soup.findAll('a', {"class": "summary"}):
        result = dn_name + link['href']
        print(result)  
#=============================================================================================================
#Grab the html response
#search for the string using regex from the html
#Replacing and appending the list with domain name/parent url
#Format accordingly by converting list into string
#Finally print the list of all the urls from the string
elif raw_url == 'http://www.workshopsf.org/?page_id=140&id=1368':
    domain_name = 'http://www.workshopsf.org'
    response= urlopen(raw_url)
    find_str = re.findall('window.location \= \'/\?[0-9a-zA-Z_=&-]+', response.read())
    clean_lines = [l.replace("window.location = '", domain_name) for l in find_str]
    new_line= "\n".join(clean_lines)
    print("List of Valid event urls" + "\n" +new_line) 
#==============================================================================================================
#Grab the html response
#search for the string using regex for the parent url from the html
#Filter on the url grabbed using class
#append domain name/parent_url to the list of the string grabbed which forms urls.
#Finally print the list of all the urls from the string
elif raw_url == 'http://events.stanford.edu/events/353/35309/':
    dn_name = 'http://events.stanford.edu'
    response = BeautifulSoup(urlopen(raw_url).read())
    parent_url = BeautifulSoup(urlopen(response.find('a' , href=re.compile('http://events.stanford.edu/'))['href']).read())
    print("List of valid event urls")
    for link in parent_url.findAll('a', {"class": "postcard-link"}):
        result = dn_name + link['href']
        print(result)
#========================================================================================================