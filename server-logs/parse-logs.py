'''
first, import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# csv implements classes to read and write tabular data in csv format
import csv


'''
preliminaries'''

# where are the logs?
path = r'C:\Users\Public\Documents\server-logs'


'''
time for business'''

# go through folder
for filename in os.listdir(path):

    # csv filename
    output_csv_filename = filename + '_parsed.csv'

    # write the csv headers
    with open(join(path, output_csv_filename), 'w') as output_csv:
        writer = csv.writer(output_csv)
        writer.writerow(['User', 'Time', 'Request', 'Status Code', 'Referrer', 'Browswer'])

    # open each log
    log = open(join(path, filename), 'r')
    # go through log
    for line in log:
        
        # parse the line
        user = line.split(' - - ')[0]
        time = line.split('[')[1].split(']')[0]
        request = line.split('"')[1]
        status_code = line.split('" ')[1].split(' ')[0]
        referrer = line.split('"')[3]
        browser = line.split('"')[5]

        # write the row
        with open(join(path, output_csv_filename), 'a') as output_csv:
            writer = csv.writer(output_csv)
            writer.writerow([user, time, request, status_code, referrer, browser])