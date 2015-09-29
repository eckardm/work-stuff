'''
first, import what we need'''

# csv implements classes to read and write tabular data in csv format
import csv

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# lxml is a powerful and pythonic xml processing library
from lxml import etree as ET


'''
preliminaries'''

# where is the corrected csv?
numbers_that_might_be_dates = 'numbers_that_might_be_dates_report-no-typos-no-not-dates.csv'

# where are the test eads?
test_eads = 'C:/Users/Public/Documents/Real_Masters_all'

#where are the production eads?
production_eads = 'C:/Users/eckardm/GitHub/vandura/Real_Masters_all'


'''
use the csv to correct the numbers that might be dates'''

# open the corrected csv in read mode
with open(numbers_that_might_be_dates, 'r') as corrected_csv:
    # read it to get the data
    corrected_data = csv.reader(corrected_csv)
    
    # skip the first row
    next(corrected_data)
    
    # go through each row
    for row in corrected_data:
    
        # match up fields to row index
        filename = row[0]
        xpath = row[1]
        number_that_is_date = row[2]
        context = row[4]
        
        # break down number that might be dates
        begin_date = number_that_is_date[:4]
        end_date = number_that_is_date[-4:]

        # account for bulk
        if 'primarily ' in context or 'mainly ' in context or 'bulk ' in context:
            type = "bulk"
        else:
            type = "inclusive"
        
        # normalized
        normal = begin_date + '/' + end_date
        
        # corrected date, accounting for certainty
        if 'ca. ' in context or 'circa ' in context:
            corrected_date = '<unitdate normal="' + normal + '" type="' + type + '" certainty="approximate">' + number_that_is_date + '</unitdate>'
        else:
            corrected_date = '<unitdate normal="' + normal + '" type="' + type + '">' + number_that_is_date + '</unitdate>'
            
        print corrected_date


        '''
        update the finding aids'''
        
        # open the corresponding ead
        ead_tree = ET.parse(join(test_eads, filename))
        
        # my understanding is that this is just the way this works
        unittitle_to_be_corrected = ead_tree.xpath(xpath)[0]
        
        # corrected unittitle
        corrected_unittitle = ET.tostring(unittitle_to_be_corrected).replace(number_that_is_date, corrected_date)
        
        # this next little bit is rediculous
        if 'primarily ' in corrected_unittitle:
            corrected_unittitle = corrected_unittitle.replace('primarily ', '').replace(number_that_is_date, 'primarily ' + number_that_is_date)
        if 'mainly ' in corrected_unittitle:
            corrected_unittitle = corrected_unittitle.replace('mainly ', '').replace(number_that_is_date, 'mainly ' + number_that_is_date)
        if 'bulk ' in corrected_unittitle:
            corrected_unittitle = corrected_unittitle.replace('bulk ', '').replace(number_that_is_date, 'bulk ' + number_that_is_date)
        if 'ca. ' in corrected_unittitle:
            corrected_unittitle = corrected_unittitle.replace('ca. ', '').replace(number_that_is_date, 'ca. ' + number_that_is_date)
        if 'circa ' in corrected_unittitle:
            corrected_unittitle = corrected_unittitle.replace('circa ', '').replace(number_that_is_date, 'circa ' + number_that_is_date)
        
        print corrected_unittitle
        
        '''
        write it!'''
        