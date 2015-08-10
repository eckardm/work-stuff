'''
first things first, import what we need'''

# lxml is the most feature-rich and easy-to-use library for processing xml (and html), you'll need to install it
from lxml import etree
# os provides a portable way of using operating system dependent functionality
import os
from os import path


'''
preliminaries'''

# where are the eads?
ead_path = 'C:\Users\Public\Documents\Real_Masters_all'
# ead_path = 'C:\Users\eckardm\GitHub\vandura\Real_Masters_all'

# where are we looking in the eads?
corpname_xpath = '//corpname'


'''
go through the files, find corpnames with dash dashes and parse them out'''

# go through the files
for filename in os.listdir(ead_path):
    # only look at the xml files
    if filename.endswith('.xml'):
        # create lxml version of the ead
        ead_tree = etree.parse(path.join(ead_path, filename))
        
        # go through each of the corpnames
        for corpname in ead_tree.xpath(corpname_xpath):
            # only look at controlaccess and origination sub-elements
            if 'controlaccess' in ead_tree.getpath(corpname) or 'origination' in ead_tree.getpath(corpname):
                # find the ones with dash dashes
                if '--' in corpname.text:
                    # split on the dash dash to get the two parts
                    corporate_entity = corpname.text.split('--', 1)[0]
                    subject = corpname.text.split('--', 1)[1]
                    print 'found one'
                    print ead_tree.getpath(corpname)
                    print corpname.text
                    print corporate_entity
                    print subject
        