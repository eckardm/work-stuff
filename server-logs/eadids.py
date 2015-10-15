'''
first things first, import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# csv implements classes to read and write tabular data in csv format
import csv

# collections implements specialized container datatypes providing alternatives to python's general purpose built-in containers, dict, list, set, and tuple
from collections import Counter	

# re provides regular expression matching operations similar to those found in perl
import re

# where are the logs?
path = r'C:\Users\Public\Documents\server-logs'

# i've already created this dictionary
from constants import eadids_and_unittitles


'''
preliminaries'''

# set up some empty histogram dictionaries
eadids_histogram_total = {}
eadids_histogram_total_no_bhl = {}


'''
get the searches for total users'''

# go through each file in logs
for filename in os.listdir(path):
	# if it's a parsed total csv
	if filename.endswith('_parsed.csv'):

		# open it
		with open(join(path, filename), 'rb') as csv_file:
			# read it
			reader = csv.reader(csv_file)
			# skip the first line
			next(reader, None)

			# go through each row
			for row in reader: 

				# requests
				request = row[2]

				# eadid
				eadid = re.search('(?<!d:)(idno=|bhlead\/)umich-bhl-.*?(?=\;|\?|\s|\&|\%)', request)

				# add eadid to histogram
				if eadid:
					eadid = eadid.string[eadid.start():eadid.end()].replace('idno=', '').replace('bhlead/', '')
					if eadid not in eadids_histogram_total:
						eadids_histogram_total[eadid] = 1
					else:
						eadids_histogram_total[eadid] +=1
						continue
				
	# same thing if it's a parsed total csv no bhl
	if filename.endswith('_parsed-noBHL.csv'):

		# open it
		with open(join(path, filename), 'rb') as csv_file:
			# read it
			reader = csv.reader(csv_file)
			# skip the first line
			next(reader, None)

			# go through each row
			for row in reader: 

				# requests
				request = row[2]

				# eadid
				eadid = re.search('(?<!d:)(idno=|bhlead\/)umich-bhl-.*?(?=\;|\?|\s|\&|\%)', request)

				# add eadid to histogram
				if eadid:
					eadid = eadid.string[eadid.start():eadid.end()].replace('idno=', '').replace('bhlead/', '')
					if eadid not in eadids_histogram_total_no_bhl:
						eadids_histogram_total_no_bhl[eadid] = 1
					else:
						eadids_histogram_total_no_bhl[eadid] +=1
						continue


'''
histograms'''

# print them in order for total
with open('eadids-counter.txt', 'w') as text_file:
	c = Counter(eadids_histogram_total)
	for k, v in c.most_common(65):
		with open('eadids-counter.txt', 'a') as text_file:
			text_file.write(k + ' (' + eadids_and_unittitles[k] + '): ' + str(v) + '\n')

# print them in order for total no bhl
with open('eadids-counter-noBHL.txt', 'w') as text_file:
	c = Counter(eadids_histogram_total_no_bhl)
	for k, v in c.most_common(65):
		with open('eadids-counter-noBHL.txt', 'a') as text_file:
			text_file.write(k + ' (' + eadids_and_unittitles[k] + '): ' + str(v) + '\n')


