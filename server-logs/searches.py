'''
first things first, import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# csv implements classes to read and write tabular data in csv format
import csv

# collections implements specialized container datatypes providing alternatives to python's general purpose built-in containers, dict, list, set, and tuple
from collections import Counter	

# matplotlib is a python 2d plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms, you'll need to install it
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# seaborn is a python visualization library based on matplotlib
import seaborn as sns



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

		# if it's a parsed total csv no bhl
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
	histograms'''

	# print them in order for total
	with open('searches-counter.txt', 'w') as text_file:
		c = Counter(searches_histogram_total)
		for k, v in c.most_common(16):
			with open('searches-counter.txt', 'a') as text_file:
				text_file.write(k + ': ' + str(v) + '\n')

	# print them in order for total no bhl
	with open('searches-counter-noBHL.txt', 'w') as text_file:
		c = Counter(searches_histogram_total_no_bhl)
		for k, v in c.most_common(16):
			with open('searches-counter-noBHL.txt', 'a') as text_file:
				text_file.write(k + ': ' + str(v) + '\n')

	# matplotlib and seaborn it
	counter_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

	searches_counter_no_bhl_xticks = []
	searches_counter_no_bhl_y = []
	c = Counter(searches_histogram_total_no_bhl)
	for k, v in c.most_common(16):
		searches_counter_no_bhl_xticks.append(k)
		searches_counter_no_bhl_y.append(v)

	plt.bar(counter_x, searches_counter_no_bhl_y)
	plt.xticks(counter_x, searches_counter_no_bhl_xticks, rotation = 45)

	plt.suptitle('Searches (No BHL)', fontsize = 'x-large')
	plt.xlabel('Searches')
	plt.ylabel('Frequency')
	plt.setp(counter_x)
	plt.show()


'''
run it!'''

# here we go
searches(path)
