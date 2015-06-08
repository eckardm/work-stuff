# import what we need
import os
from os.path import join
from lxml import etree
import re

#empty dictionary for ead identifier keys and title proper values
eadids_and_unittitles = {}

# where are the eads?
ead_path = 'S:/Curation/Projects/Mellon/ArchivesSpace/ATeam_Migration/EADs/Real_Masters_all'

# regex we'll need
eads = re.compile('\.xml$')

# xpaths we'll need
eadid_xpath = '//eadid'
collection_unittitle_xpath = '//did/unittitle'

# print that we're creating the dictionary
print 'Creating dictionary.'

# start a counter
counter = 0

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
        # get the collection unit title xml entity
        collection_unittitle = ead_tree.xpath(collection_unittitle_xpath)
        # get the eadid text
        eadid_text = eadid[0].text
        # get the collection unit title text, and get the line breaks and crazy spacing right
        collection_unittitle_text = etree.tostring(collection_unittitle[0])
        # more crazy spacing
        collection_unittitle_text = ' '.join(collection_unittitle_text.split())
        # remove the xml tags <-- this probably isn't the most elegant way to do this
        collection_unittitle_text = re.sub('<.*?>', '', collection_unittitle_text)
        # add both do the ead identifier and title proper dictionary
        eadids_and_unittitles[eadid_text] = collection_unittitle_text
        # update counter
        counter += 1

# where is constants.py?
constants = 'constants.py'
# get the time (http://stackoverflow.com/questions/13890935/timestamp-python)
import time
rightnow = time.time()
import datetime
datetime_rightnow = datetime.datetime.fromtimestamp(rightnow).strftime('%Y-%m-%d %H:%M:%S')
# put the dictionary in constants.py
with open(constants, "a") as txt_file:
    txt_file.write('# dictionary for eadid (key) and titleproper (value) accruate as of ' + datetime_rightnow + '\neadids_and_unittitles = ' + str(eadids_and_unittitles))

# print that dictionary got created
print '\rDictionary with ' + str(counter) + ' entries and accurate as of ' + datetime_rightnow + ' created.'