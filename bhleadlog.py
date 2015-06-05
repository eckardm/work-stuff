# import what we need
import os
from os.path import join
from lxml import etree
import csv
import re
import csv

'''
first, let's create a dictionary of ead identifiers and their corresponding title propers'''

#empty dictionary for ead identifier keys and title proper values
eadids_and_titlepropers = {}

# where are the eads?
ead_path = 'path/to/eads'

# make sure we only get the xml
eads = re.compile('\.xml$')

# xpaths we'll need
eadid_xpath = '//eadid'
titleproper_xpath = '//titlestmt/titleproper'

# print that we're creating the dictionary
print 'Creating dictionary.'

# go through the eads
for filename in os.listdir(ead_path):
    if eads.search(filename):
        # let us know we're still working on it
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        # parse the ead
        ead_tree = etree.parse(join(ead_path, filename))
        # get the eadid xml entity
        eadid = ead_tree.xpath(eadid_xpath)
        # get the titleproper xml entity
        titleproper = ead_tree.xpath(titleproper_xpath)
        # get the eadid text
        eadid_text = eadid[0].text
        # get the titleproper text, and get the line breaks and encoding right
        titleproper_text = titleproper[0].text.replace('\n', '').encode('ascii', 'ignore')
        # add both do the ead identifier and title proper dictionary
        eadids_and_titlepropers[eadid_text] = titleproper_text

# print that dictionary got created
print '\rDictionary created.'

'''
second, lets get the unique ead identifiers and queries from the logs, and use the dictionary to tell us what the corresponding title proper is for each ead identifier'''

# empty lists for ead identifiers and queries
ead_identifiers = []
queries = []

# counts for requests, ead identifiers and queries
requests_count = 0
ead_identifiers_count = 0
queries_count = 0
key_error_counter = 0

# where are the logfiles?
logfiles = 'path/to/logfile.csv'

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
add unique ead identifiers and corresponding title to eadidentifiers.csv'''

# where is the output csv
eadidentifiers_csv = 'path/to/eadidentifiers.csv'

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
            writer.writerow([i, eadids_and_titlepropers[i]])
        # if it doesn't work
        except:
            # write the row
            writer.writerow([i, 'UNIDENTIFIED TITLEPROPER'])
            # add key to dictionary with dummy value for future investigation
            eadids_and_titlepropers[i] = 'UNIDENTIFIED TITLEPROPER'
            # update count
            key_error_counter += 1

# let us know the csv is finished...
print 'eadidentifiers.csv created.'
# ...and how many errors there were
print 'There were ' + str(key_error_counter) + ' KEY ERROR(S) found.'

'''
add unique queries to queries.txt'''

# where is the output txt
queries_txt = 'path/to/queries.txt'

# print that we're starting on unique queries
print 'QUERIES'
# let us know how many
print 'There were ' + str(queries_count) + ' unique queries today.'
# let us know we're starting the txt
print 'Creating queries.txt.'
for i in queries:
    with open(queries_txt, "a") as txt_file:
        txt_file.write(i + '\n')
print 'queries.txt created.'