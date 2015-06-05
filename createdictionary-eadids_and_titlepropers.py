# import what we need
import os
from os.path import join
from lxml import etree
import re

#empty dictionary for ead identifier keys and title proper values
eadids_and_titlepropers = {}

# where are the eads?
ead_path = 'path/to/EADs'

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

# where is constants.py?
constants = 'constants.py'
with open(constants, "a") as txt_file:
    txt_file.write('eadids_and_titlepropers = ' + str(eadids_and_titlepropers))
        
# print that dictionary got created
print '\rDictionary created.'

print 'eadids_and_titlepropers = ' + str(eadids_and_titlepropers)