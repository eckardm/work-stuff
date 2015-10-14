'''
first things first, import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# csv implements classes to read and write tabular data in csv format
import csv


import re

'''
preliminaries'''

# where are the logs?
path = r'C:\Users\Public\Documents\server-logs'

# set up some empty histogram dictionaries
eadid_histogram_total = {}
searches_histogram_total = {}
eadid_histogram_total_no_bhl = {}
searches_histogram_total_no_bhl = {}

'''
first, let's break up the csv by days for total users'''

# go through each file in logs
for filename in os.listdir(path):
	# if it's a parsed total csv
	if filename.endswith('_parsed.csv'):

		with open('searches.txt', 'w') as text_file:

			# open it
			with open(join(path, filename), 'rb') as csv_file:
				# read it
				reader = csv.reader(csv_file)
				# skip the first line
				next(reader, None)

				# go through each row
				for row in reader: 

					request = row[2]

					if '&Submit=Search' in request and 'q3=' in request and 'q3=&' not in request:
						search = request.split('q1=')[1].split('&')[0] + ' ' + request.split('op2=')[1].split('&')[0].upper() + ' ' + request.split('q2=')[1].split('&')[0] + ' ' + request.split('op3=')[1].split('&')[0].upper() + ' ' + request.split('q3=')[1].split('&')[0]
						search = search.replace('AND  AND', 'AND EMPTY AND')
						if search not in searches_histogram_total:
							searches_histogram_total[search] = 1
						else:
							searches_histogram_total[search] += 1
						with open('searches.txt', 'a') as text_file:
							text_file.write(search + '\n')

					elif '&Submit=Search' in request and 'q2=' in request and '&q2=&' not in request:
						search = request.split('q1=')[1].split('&')[0] + ' ' + request.split('op2=')[1].split('&')[0].upper() + ' ' + request.split('q2=')[1].split('&')[0]
						if search not in searches_histogram_total:
							searches_histogram_total[search] = 1
						else:
							searches_histogram_total[search] += 1
						with open('searches.txt', 'a') as text_file:
							text_file.write(search + '\n')

					elif '&Submit=Search' in request:
						search = request.split('q1=')[1].split('&')[0]
						if search not in searches_histogram_total:
							searches_histogram_total[search] = 1
						else:
							searches_histogram_total[search] += 1
						with open('searches.txt', 'a') as text_file:
							text_file.write(search + '\n')

	# if it's a parsed total csv
	if filename.endswith('_parsed-noBHL.csv'):

		with open('searches-noBHL.txt', 'w') as text_file:

			# open it
			with open(join(path, filename), 'rb') as csv_file:
				# read it
				reader = csv.reader(csv_file)
				# skip the first line
				next(reader, None)

				# go through each row
				for row in reader: 

					request = row[2]

					if '&Submit=Search' in request and 'q3=' in request and 'q3=&' not in request:
						search = request.split('q1=')[1].split('&')[0] + ' ' + request.split('op2=')[1].split('&')[0].upper() + ' ' + request.split('q2=')[1].split('&')[0] + ' ' + request.split('op3=')[1].split('&')[0].upper() + ' ' + request.split('q3=')[1].split('&')[0]
						search = search.replace('AND  AND', 'AND EMPTY AND')
						if search not in searches_histogram_total_no_bhl:
							searches_histogram_total_no_bhl[search] = 1
						else:
							searches_histogram_total_no_bhl[search] += 1
						with open('searches-noBHL.txt', 'a') as text_file:
							text_file.write(search + '\n')

					elif '&Submit=Search' in request and 'q2=' in request and '&q2=&' not in request:
						search = request.split('q1=')[1].split('&')[0] + ' ' + request.split('op2=')[1].split('&')[0].upper() + ' ' + request.split('q2=')[1].split('&')[0]
						if search not in searches_histogram_total_no_bhl:
							searches_histogram_total_no_bhl[search] = 1
						else:
							searches_histogram_total_no_bhl[search] += 1
						with open('searches-noBHL.txt', 'a') as text_file:
							text_file.write(search + '\n')

					elif '&Submit=Search' in request:
						search = request.split('q1=')[1].split('&')[0]
						if search not in searches_histogram_total_no_bhl:
							searches_histogram_total_no_bhl[search] = 1
						else:
							searches_histogram_total_no_bhl[search] += 1
						with open('searches-noBHL.txt', 'a') as text_file:
							text_file.write(search + '\n')

print searches_histogram_total
print searches_histogram_total_no_bhl
