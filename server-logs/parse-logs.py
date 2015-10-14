'''
first, import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# csv implements classes to read and write tabular data in csv format
import csv

from tqdm import *


'''
preliminaries'''

# where are the logs?
path = r'C:\Users\Public\Documents\server-logs'

def parse_logs(path):

    # bentley front computer ip adresses (best faith effort as of 2015-10-12)
    front_computers = ['141.211.39.59', '141.211.39.6', '141.211.39.69', '141.211.39.22', '141.211.39.19', '141.211.39.119', '141.211.39.56']


    '''
    time for business'''

    # go through folder
    for filename in os.listdir(path):

        # csv filenames for total and bentley removed
        output_csv_filename = filename.replace('.txt', '') + '_parsed.csv'
        output_csv_filename_no_bhl = filename.replace('.txt', '') + '_parsed-noBHL.csv'
        
        # only do this if we haven't done it before
        if filename.endswith('.csv') or output_csv_filename in os.listdir(path) or output_csv_filename_no_bhl in os.listdir(path):
            continue
        else:

            # write the csv headers for total
            with open(join(path, output_csv_filename), 'wb') as output_csv:
                writer = csv.writer(output_csv)
                writer.writerow(['User', 'Time', 'Request', 'Status Code', 'Referrer', 'Browswer'])

            # write the csv headers for no bhl
            with open(join(path, output_csv_filename_no_bhl), 'wb') as output_csv:
                writer = csv.writer(output_csv)
                writer.writerow(['User', 'Time', 'Request', 'Status Code', 'Referrer', 'Browswer'])

            # open each log
            log = open(join(path, filename), 'r')
            # go through log
            for line in tqdm(log, desc=filename):
                
                # parse the line
                user = line.split(' - - ')[0]
                time = line.split('[')[1].split(']')[0]
                request = line.split('"')[1]
                status_code = line.split('" ')[1].split(' ')[0]
                referrer = line.split('"')[3]
                browser = line.split('"')[5]

                if 'bot' in browser or 'Bot' in browser or 'spider' in browser or 'Spider' in browser:
                    continue

                # write the row for the total csv
                with open(join(path, output_csv_filename), 'ab') as output_csv:
                    writer = csv.writer(output_csv)
                    writer.writerow([user, time, request, status_code, referrer, browser])

                # write the row for the no bentley csv
                    if 'access_log' not in user or user.split(':')[1] in front_computers:
                        with open(join(path, output_csv_filename_no_bhl), 'ab') as output_csv:
                            writer = csv.writer(output_csv)
                            writer.writerow([user, time, request, status_code, referrer, browser])


'''
run the function'''

# here we go
parse_logs(path)
