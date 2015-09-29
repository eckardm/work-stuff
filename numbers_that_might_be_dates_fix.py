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
test_eads = 'C:/Users/eckardm/Public/Documents/Real_Masters_all'

#where are the production eads?
production_eads = 'C:/Users/eckardm/GitHub/vandura/Real_Masters_all'
