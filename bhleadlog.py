# import what we need
import os
from os.path import join
from lxml import etree
import csv
import re
import csv
import urllib
import time

# import this custom dictionary
from constants import eadids_and_unittitles

'''
first, lets get the unique ead identifiers and queries from the logs, and use the dictionary to tell us what the corresponding title proper is for each ead identifier'''

# empty lists for ead identifiers and queries
ead_identifiers = []
queries = []

# counts for requests, ead identifiers and queries
requests_count = 0
ead_identifiers_count = 0
queries_count = 0

# where are the log files?
log_files = 'C:/Users/Public/Documents/bhleadlog/subsetbhleadlog.csv'

# print that we're starting the logs
print 'Going through logs.'

# open the logs
with open(log_files, 'rb') as csvfile:
    # read the logs
    logreader = csv.reader(csvfile, delimiter=',')
    # go through each row
    for row in logreader:
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        # find the requests
        request = row[2]
        # update count
        requests_count += 1
        # find the ead identifiers
        ead_identifier_matches = re.findall('umich-bhl-\d+\.?-?\d', request)
        # go through them
        for ead_identifier in ead_identifier_matches:
            # make sure they are unique
            if ead_identifier not in ead_identifiers:
                # add them to empty list
                ead_identifiers.append(ead_identifier)
                # update count
                ead_identifiers_count += 1
        # find the queries
        query_matches = re.findall('(?<=q1=)(.*)(?=&Submit=Search)', request)
        # go through them
        for query in query_matches:
            # make sure they are unique
            if query not in queries:
                # add them to empty list
                queries.append(query)
                # update count
                queries_count += 1

# print that we're done with logs
print '\rLogs gone through.'               
                
# print requests
print 'REQUESTS'
print 'There were ' + str(requests_count) + ' requests today.'

'''
second, add unique ead identifiers and corresponding title to eadidentifiers.csv'''

# where is the output csv
eadidentifiers_csv = 'C:/Users/Public/Documents/bhleadlog/eadidentifiers.csv'

# create header row
with open(eadidentifiers_csv, 'ab') as csv_file:
    writer = csv.writer(csv_file, dialect='excel')
    writer.writerow(['eadid', 'titleproper'])

# print that we're starting on unique ead identifiers
print 'EAD IDENTIFIERS'
# let us know how many
print 'There were ' + str(ead_identifiers_count) + ' unique EADs accessed today.'
# let us know we're starting the csv
print 'Creating eadidentifiers.csv'
for i in ead_identifiers:
    with open(eadidentifiers_csv, 'ab') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        # give it a try
        try:
            # write the row
            writer.writerow([i, eadids_and_unittitles[i]])
        # if it doesn't work because somebody searched for and ead identifier that doesn't exist
        except:
            continue

# let us know the csv is finished...
print 'eadidentifiers.csv created.'

'''
third, add unique queries to queries.txt'''

# where is the output txt
queries_txt = 'C:/Users/Public/Documents/bhleadlog/queries.txt'

# print that we're starting on unique queries
print 'QUERIES'
# let us know how many
print 'There were ' + str(queries_count) + ' unique queries today.'
# let us know we're starting the txt
print 'Creating queries.txt.'
for i in queries:
    with open(queries_txt, "a") as txt_file:
        txt_file.write(i + '\n')
print 'queries.txt created'

'''
fourth, figure out where people are coming from'''

# empty counters
deepblue_counter = 0
finding_aids_counter = 0
bentley_counter = 0
mirlyn_counter = 0
university_of_michigan_counter = 0
google_counter = 0
yahoo_counter = 0
ask_counter = 0
bing_counter = 0
no_referral_counter = 0
other_counter = 0

# print that we're starting the logs again
print 'Going through logs again.'

# open the logs
with open(log_files, 'rb') as csvfile:
    # read the logs
    logreader = csv.reader(csvfile, delimiter=',')
    # go through each row
    for row in logreader:
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        # find the referrers
        referrer = row[3]
        # set up umich.edu finds
        university_of_michigan_matches = re.findall('umich.edu', referrer)  
        deepblue_matches = re.findall('deepblue.lib.umich.edu', referrer)
        finding_aids_matches = re.findall('quod.lib.umich.edu', referrer)
        bentley_matches = re.findall('bentley.umich.edu', referrer)
        mirlyn_matches = re.findall('mirlyn.lib.umich.edu', referrer)
        # go through them
        for university_of_michigan_match in university_of_michigan_matches:
            # deepblue
            if deepblue_matches:
                # update count
                deepblue_counter += 1
            # finding aids
            elif finding_aids_matches:
                # update count
                finding_aids_counter += 1
            # bentley
            elif bentley_matches:
                # update count
                bentley_counter += 1
            # eadids_and_titlepropers
            elif mirlyn_matches:
                # update count
                mirlyn_counter += 1
            else:
                # update university of michigan counter
                university_of_michigan_counter += 1
        # google
        google_matches = re.findall('google.com', referrer)
        for google_match in google_matches:
            google_counter += 1
        # yahoo
        yahoo_matches = re.findall('yahoo.com', referrer)
        for yahoo_match in yahoo_matches:
            yahoo_counter += 1
        # ask
        ask_matches = re.findall('ask.com', referrer)
        for ask_match in ask_matches:
            ask_counter += 1
        # bing
        bing_matches = re.findall('bing.com', referrer)
        for bing_match in bing_matches:
            bing_counter += 1
        # no referral
        no_referral_matches = re.findall('^-$', referrer)
        for no_referral_match in no_referral_matches:
            no_referral_counter += 1
        # other
        if university_of_michigan_matches and google_matches and yahoo_matches and ask_matches and bing_matches and no_referral_matches not in referrer:
            other_counter += 1
            
# print that we're done with logs again
print '\rLogs gone through again.'               
                
# create function for percentage
def percentage(count):
    total_referrals_count = deepblue_counter + finding_aids_counter + bentley_counter + mirlyn_counter + university_of_michigan_counter + google_counter + yahoo_counter + ask_counter + bing_counter + no_referral_counter + other_counter
    percent = float(count) / float(total_referrals_count) * 100
    return percent
                
# print referrers
print 'REFERRALS'
print str(deepblue_counter) + ' referrals came from DeepBlue today. That is ' + str(percentage(deepblue_counter)) + '%.'
print str(finding_aids_counter) + ' referrals came from the Finding Aids site today. That is ' + str(percentage(finding_aids_counter)) + '%.'
print str(bentley_counter) + " referrals came from the Bentley's site today. That is " + str(percentage(bentley_counter)) + '%.'
print str(mirlyn_counter) + ' referrals came from Mirlyn today. That is ' + str(percentage(mirlyn_counter)) + '%.'
print str(university_of_michigan_counter) + ' referrals came from the main University of Michigan site today. That is ' + str(percentage(university_of_michigan_counter)) + '%.'
print str(google_counter) + ' referrals came from Google today. That is ' + str(percentage(google_counter)) + '%.'
print str(yahoo_counter) + ' referrals came from Yahoo today. That is ' + str(percentage(yahoo_counter)) + '%.'
print str(ask_counter) + ' referrals came from Ask today. That is ' + str(percentage(ask_counter)) + '%.'
print str(bing_counter) + ' referrals came from Bing today. That is ' + str(percentage(bing_counter)) + '%.'
print str(no_referral_counter) + ' were not referred. That is ' + str(percentage(no_referral_counter)) + '%.'
print 'Other: ' + str(other_counter) + '. That is ' + str(percentage(other_counter)) + '%.'


'''
fifth, figure out if folks are getting any 404s <--  this is very imperfect'''

# print that we're starting the logs again
print 'Going through logs again.'

# match get requests
get_requests = re.compile('^GET')

# base dlxs url
base_url = 'http://quod.lib.umich.edu'

# counter
response_code_counter = 0
overloading_counter = 0

# emptydictionary
response_code_errors = {}

# open the logs
with open(log_files, 'rb') as csvfile:
    # read the logs
    logreader = csv.reader(csvfile, delimiter=',')
    # go through each row
    for row in logreader:
        # only look at get requests
        request = row[2]
        if get_requests.search(request):
            # don't overload the server
            time.sleep(1)
            # keep up with where we are
            print '\rWorking on it... |',
            print '\rWorking on it... /',
            print '\rWorking on it... -',
            print '\rWorking on it... \\',
            print '\rWorking on it... |',
            print '\rWorking on it... /',
            print '\rWorking on it... -',
            print '\rWorking on it... -',
            print '\rWorking on it... \\',
            request_url = base_url + request.replace('GET ', '')
            response_code = urllib.urlopen(request_url).getcode()
            if response_code == 200:
                continue
            elif response_code == 503:
                overloading_counter += 1
            else:
                response_code_counter += 1
                response_code_errors[request_url] = response_code
                
# print that we're done with logs again
print '\rLogs gone through again.'  

# print response code errors
print 'RESPONSE CODES'
print 'There were ' + str(response_code_counter) + " response code errors. We're not sure about " + str(overloading_counter) + ' because we are overloading the server.'
print 'Here they are:'
for key, value in response_code_errors.iteritems():
    print 'Request: ' + key
    print 'Response Code: ' + str(value)

'''
sixth, see what kinds of side things people click on'''

# print that we're starting the logs
print 'Going through logs yet again.'

# empty dictionary
focus_region_counts = {}

# open the logs
with open(log_files, 'rb') as csvfile:
    # read the logs
    logreader = csv.reader(csvfile, delimiter=',')
    # go through each row
    for row in logreader:
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        # find the requests
        request = row[2]
        # find the ead identifiers
        focus_regions = re.findall('(?<=focusrgn=)(.*?)(?=\;)', request)
        # go through them
        for focus_region in focus_regions:
            # create dictionary (http://stackoverflow.com/questions/3496518/python-using-a-dictionary-to-count-the-items-in-a-list)
            focus_region_counts[focus_region] = focus_region_counts.get(focus_region, 0) + 1
            
# print that we're done with logs
print '\rLogs gone through yet again.'               
                
# print requests
print 'FOCUS REGIONS'
print 'Found ' + str(len(focus_region_counts)) + ' focus regions.'
print 'Here they are: '

# calculate percentage
total_focus_region_count = 0
for key, value in focus_region_counts.iteritems():
    total_focus_region_count += value

# print the rest of requests
for key, value in focus_region_counts.iteritems():
    print 'Focus Region: ' + key
    print 'Count: ' + str(value) + ', which is ' + str(float(value) / float(total_focus_region_count) * 100) + '%.'
    
'''
seventh, how many mobile users?'''

# print that we're starting the logs
print 'Going through logs yet again.'

# empty dictionary
browser_os_counter = 0
mobile_devices_counter = 0

# open the logs
with open(log_files, 'rb') as csvfile:
    # read the logs
    logreader = csv.reader(csvfile, delimiter=',')
    # go through each row
    for row in logreader:
        browser_os_counter +=1
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        # find the requests
        browser_os = row[4]
        # find the ead identifiers
        mobile_devices = re.findall('Mobile', browser_os)
        # go through them
        for mobile_device in mobile_devices:
            mobile_devices_counter += 1
            
# print that we're done with logs
print '\rLogs gone through yet again.'               
                
# print requests
print 'MOBILE DEVICES'
print str(mobile_devices_counter) + ' of ' + str(browser_os_counter) + ' requests were made on mobile devices. That is ' + str(float(mobile_devices_counter) / float(browser_os_counter) * 100) + '%.'

'''
eighth, information on bookbag use'''

# print that we're starting the logs
print 'Going through logs yet again.'

# empty dictionary
bookbag_add_counter = 0
bookbag_look_counter = 0
requests_counter = 0

# open the logs
with open(log_files, 'rb') as csvfile:
    # read the logs
    logreader = csv.reader(csvfile, delimiter=',')
    # go through each row
    for row in logreader:
        requests_counter +=1
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        # find the requests
        request = row[2]
        # find adding to bookbag
        bookbag_add_matches = re.findall('bbaction=add', request)
        for bookbag_add_match in bookbag_add_matches:
            bookbag_add_counter += 1
        # find looking at bookbag
        bookbag_look_matches = re.findall('page=bbaglist', request)
        for bookbag_look_match in bookbag_look_matches:
            bookbag_look_counter += 1
 
# print that we're done with logs
print '\rLogs gone through yet again.'               
                
# print requests
print 'BOOKBAG USE'
print str(bookbag_add_counter) + ' requests added items to bookbags. That is ' + str(float(bookbag_add_counter) / float(requests_counter) * 100) + '%.'
print str(bookbag_look_counter) + ' requests looked at items in bookbags. That is ' + str(float(bookbag_look_counter) / float(requests_counter) * 100) + '%.'