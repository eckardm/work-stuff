# import what we need
import os
from os.path import join
from lxml import etree
import csv
import re
import csv

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

# where are the logfiles?
logfiles = 'C:/Users/Public/Documents/bhleadlog/subsetbhleadlog.csv'

# print that we're starting the logs
print 'Going through logs.'

# open the logs
with open(logfiles, 'rb') as csvfile:
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
eadidentifiers_csv = 'eadidentifiers.csv'

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
queries_txt = 'queries.txt'

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

# print that we're starting the logs
print 'Going through logs again.'

# open the logs
with open(logfiles, 'rb') as csvfile:
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
            
# print that we're done with logs
print '\rLogs gone through again.'               
                
# create function for percentage
def percentage(count):
    total_referrals_count = deepblue_counter + finding_aids_counter + bentley_counter + mirlyn_counter + university_of_michigan_counter + google_counter + yahoo_counter + ask_counter + bing_counter + no_referral_counter + other_counter
    percent = float(count) / float(total_referrals_count) * 100
    return percent
                
# print referrers
print 'REFERRERS'
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
fifth, figure out if folks are getting any 404s'''