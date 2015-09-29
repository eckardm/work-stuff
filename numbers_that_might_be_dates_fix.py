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
production_eads = 'C:/Users/eckardm/vandura/Real_Masters_all'


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
        
        # keep up with where we are
        print 'Correcting ' + number_that_is_date + ' in ' + filename + ' at ' + xpath + '.'
        
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


        '''
        update the finding aids'''
        
        # open the ead in question
        ead_in = open(join(production_eads, filename), 'r')
        
        # make a tree out of it for lxml
        ead_tree = ET.parse(ead_in)
        
        # find the unittitle that needs to be corrected
        unittitle_to_be_corrected = ead_tree.xpath(xpath)
        
        # corrected unittitle, and the index is just a wierd lxml thing
        corrected_unittitle = ET.tostring(unittitle_to_be_corrected[0]).replace(number_that_is_date, corrected_date)
        
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
            
        # make it happen, and the index is just a wierd lxml thing
        unittitle_to_be_corrected[0].text = corrected_unittitle
        
        
        '''
        write it!'''
        
        # open the corresponding ead
        with open(join(production_eads, filename), mode="w") as see_i_am_making_all_things_new:
            # and write the corrected unittitle
            see_i_am_making_all_things_new.write(ET.tostring(ead_tree, xml_declaration=True, encoding='utf-8', pretty_print=True))
            
print "That's it, we're done!"
