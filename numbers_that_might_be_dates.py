'''
first, import what we need'''

# csv implements classes to read and write tabular data in csv format
import csv

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

# where do we want to output report
numbers_that_might_be_dates_report = 'numbers_that_might_be_dates_report.csv'

# create the headers in that output report in super write mode
with open(numbers_that_might_be_dates_report, 'wb') as csv_file:
    # create the writer
    csv_file_writer = csv.writer(csv_file)
    # write the headers
    csv_file_writer.writerow(['Filename', 'XPath', 'Suspicious Number', 'Context'])

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
            
                # get the xpath for the report
                number_that_might_be_date_xpath = ead_tree.getpath(unittitle)
                
                # get the context for the report
                context = unittitle_string_without_unitdate.replace('<unittitle>', '').replace('</unittitle>', '').strip()
                
                # if this is not a nested title
                if ('<title' in context or '<unittitle' in context):
                    continue
                
                # if this **really** is not a nested title
                if (context.endswith(number_that_might_be_date) == False and ('"' in context.split(number_that_might_be_date)[0] and '"' in context.split(number_that_might_be_date)[1])):
                    continue

                # if it's not a range
                if '-' not in number_that_might_be_date:
                    # see if they are in the appropriate date range and don't have quotes
                    if 1800 <= int(number_that_might_be_date[:-4]) <= 2015:
                        
                        # add one to the counter
                        counter += 1
                        
                        # open the report in super append mode
                        with open(numbers_that_might_be_dates_report, 'ab') as csv_file:
                            # create the writer
                            csv_file_writer = csv.writer(csv_file)
                            # write the row
                            csv_file_writer.writerow([filename, number_that_might_be_date_xpath, number_that_might_be_date, context])
                        
                # if it is a range
                else:
                    # get the start date
                    number_that_might_be_date_start = number_that_might_be_date.split('-')[0].strip()
                    # get the end date
                    number_that_might_be_date_end = number_that_might_be_date.split('-')[1]
                    # see if they are in the appropriate date range and don't have quotes
                    if 1800 <= int(number_that_might_be_date_start) and int(number_that_might_be_date_end) <= 2015:
                        
                        # add one to the counter
                        counter += 1
                        
                        # open the report in super append mode
                        with open(numbers_that_might_be_dates_report, 'ab') as csv_file:
                            # create the writer
                            csv_file_writer = csv.writer(csv_file)
                            # write the row
                            csv_file_writer.writerow([filename, number_that_might_be_date_xpath, number_that_might_be_date, context])
            
# print it out
print 'found: ' + str(counter)
  