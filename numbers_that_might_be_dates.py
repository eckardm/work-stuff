'''
first, import what we need'''

# lxml is a powerful xml document parser, you'll need to install it
from lxml import etree

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# re provide regular expression matching operations
import re

# tqdm adds a progress meter to loops, you'll need to install it
from tqdm import *


'''
preliminaries'''

# where are the eads?
ead_folder = 'C:/Users/eckardm/vandura/Real_Masters_all'

# counter
counter = 0


'''
go through eads and look for numbers that might be dates'''

# go through each of the files in the ead folder
for filename in tqdm(os.listdir(ead_folder)):
    # but only do the ones that are actually eads (we can tell because they are xml files)
    if filename.endswith('.xml'):
        # create an etree (part of lxml) tree that we can parse
        ead_tree = etree.parse(join(ead_folder, filename))
        
        # go through unittitles
        for unittitle in ead_tree.xpath('//unittitle'):
            # convert them to a string
            unittitle_string = etree.tostring(unittitle)
            # get rid of unitdate tags
            unittitle_string_without_unitdate = re.sub('(<unitdate.*>).*(<\/unitdate>)', '', unittitle_string)
            
            # find numbers that might be dates
            numbers_that_might_be_dates = re.findall('\s\d{4}\-?\d{4}?', unittitle_string_without_unitdate)
          
            # go through them
            for number_that_might_be_date in numbers_that_might_be_dates:
            
                               
               # if it's not a range
                if "-" not in number_that_might_be_date:
                    # see if they are in the appropriate date range and don't have quotes
                    if 1800 <= int(number_that_might_be_date[:-4]) <= 2015 and not unittitle_string_without_unitdate.split(number_that_might_be_date)[1].startswith('"'):
                        # add one to the counter
                        counter += 1
             
             # if it is a range
                else:
                    # get the start date
                    number_that_might_be_date_start = number_that_might_be_date.split('-')[0].strip()
                    # get the end date
                    number_that_might_be_date_end = number_that_might_be_date.split('-')[1]
                    # see if they are in the appropriate date range and don't have quotes
                    if 1800 <= int(number_that_might_be_date_start) and int(number_that_might_be_date_end) <= 2015 and not unittitle_string_without_unitdate.split(number_that_might_be_date_end)[1].startswith('"'):
                        # add one to the counter
                        counter += 1
                        
# print it out
print 'found: ' + str(counter)
  