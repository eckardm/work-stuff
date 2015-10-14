'''
first things first, import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# csv implements classes to read and write tabular data in csv format
import csv


'''
preliminaries'''

# where are the logs?
path = r'C:\Users\Public\Documents\server-logs'

def searches(path):

	# set up some empty histogram dictionaries

	searches_histogram_total = {}

	searches_histogram_total_no_bhl = {}


	'''
	get the searches for total users'''

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

						# requests
						request = row[2]

						# advanced searches with three searches
						if '&Submit=Search' in request and 'q3=' in request and 'q3=&' not in request:
							search = request.split('q1=')[1].split('&')[0] + ' ' + request.split('op2=')[1].split('&')[0].upper() + ' ' + request.split('q2=')[1].split('&')[0] + ' ' + request.split('op3=')[1].split('&')[0].upper() + ' ' + request.split('q3=')[1].split('&')[0]
							search = search.replace('AND  AND', 'AND EMPTY AND')
							if search not in searches_histogram_total:
								searches_histogram_total[search] = 1
							else:
								searches_histogram_total[search] += 1
							with open('searches.txt', 'a') as text_file:
								text_file.write(search + '\n')

						# advanced searches with two	
						elif '&Submit=Search' in request and 'q2=' in request and '&q2=&' not in request:
							search = request.split('q1=')[1].split('&')[0] + ' ' + request.split('op2=')[1].split('&')[0].upper() + ' ' + request.split('q2=')[1].split('&')[0]
							if search not in searches_histogram_total:
								searches_histogram_total[search] = 1
							else:
								searches_histogram_total[search] += 1
							with open('searches.txt', 'a') as text_file:
								text_file.write(search + '\n')

						# advanced searches or just plain searches with just one
						elif '&Submit=Search' in request:
							search = request.split('q1=')[1].split('&')[0]
							if search not in searches_histogram_total:
								searches_histogram_total[search] = 1
							else:
								searches_histogram_total[search] += 1
							with open('searches.txt', 'a') as text_file:
								text_file.write(search + '\n')


		'''
		get the searches for total users no bhl'''

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

						# requests
						request = row[2]

						# advanced searches with three searches
						if '&Submit=Search' in request and 'q3=' in request and 'q3=&' not in request:
							search = request.split('q1=')[1].split('&')[0] + ' ' + request.split('op2=')[1].split('&')[0].upper() + ' ' + request.split('q2=')[1].split('&')[0] + ' ' + request.split('op3=')[1].split('&')[0].upper() + ' ' + request.split('q3=')[1].split('&')[0]
							search = search.replace('AND  AND', 'AND EMPTY AND')
							if search not in searches_histogram_total_no_bhl:
								searches_histogram_total_no_bhl[search] = 1
							else:
								searches_histogram_total_no_bhl[search] += 1
							with open('searches-noBHL.txt', 'a') as text_file:
								text_file.write(search + '\n')

						# advanced searches with two
						elif '&Submit=Search' in request and 'q2=' in request and '&q2=&' not in request:
							search = request.split('q1=')[1].split('&')[0] + ' ' + request.split('op2=')[1].split('&')[0].upper() + ' ' + request.split('q2=')[1].split('&')[0]
							if search not in searches_histogram_total_no_bhl:
								searches_histogram_total_no_bhl[search] = 1
							else:
								searches_histogram_total_no_bhl[search] += 1
							with open('searches-noBHL.txt', 'a') as text_file:
								text_file.write(search + '\n')

						# advanced searches or just plain searches with just one
						elif '&Submit=Search' in request:
							search = request.split('q1=')[1].split('&')[0]
							if search not in searches_histogram_total_no_bhl:
								searches_histogram_total_no_bhl[search] = 1
							else:
								searches_histogram_total_no_bhl[search] += 1
							with open('searches-noBHL.txt', 'a') as text_file:
								text_file.write(search + '\n')

	'''
	for now, just print the searches, in the future these should be historgrams?'''

	print searches_histogram_total
	print searches_histogram_total_no_bhl


'''
run it!'''

# here we go
searches(path)