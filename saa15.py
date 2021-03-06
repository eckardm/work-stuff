'''
first things first, import the python modules we'll need, listed in the order you'll need them'''

# os provides a portable way of using operating system dependent functionality
import os

# urllib2 opens URLs, it comes with python
import urllib2

# beautifulsoup pulls data out of HTML and XML files, you'll need to install it
from bs4 import BeautifulSoup

# re provides regular expression matching operations
import re

# time provides various time-related functions, we'll be using it to wait
import time


'''
go through events on saa page, go to the event, scrape title and description'''

education_sessions = urllib2.urlopen('http://archives2015.sched.org/overview/type/education+session#.VfnN3EZuPhW').read()
education_sessions_soup = BeautifulSoup(education_sessions)

education_session_urls = education_sessions_soup.find_all('a', {'class': 'name'})

for education_session_url in education_session_urls:


    education_session = urllib2.urlopen('http://archives2015.sched.org' + education_session_url['href']).read()
    education_session_soup = BeautifulSoup(education_session)
    
    title = education_session_soup.find('a', {'class': 'name'})
    
    print "TITLE: " + title.get_text()
    
    description = education_session_soup.find('div', {'class': 'tip-description'})
    
    FIX THIS REGEX AND YOU'VE GOT IT!
    
    description = re.sub(r'</?\[\d+>', '', description)
    
    print "DESCRIPTION: " + description.
    
    time.sleep(30) 
    
    