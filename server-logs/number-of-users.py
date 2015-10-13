'''
first things first, import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# csv implements classes to read and write tabular data in csv format
import csv

# matplotlib is a python 2d plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms, you'll need to install it
import matplotlib.pyplot as plt

# seaborn is a python visualization library based on matplotlib
import seaborn as sns

import numpy as np


'''
preliminaries'''

# where are the logs?
path = r'C:\Users\Public\Documents\server-logs'

# make it a function
def number_of_users(path):

	# months
	months = {
		"Jan": "01",
		"Feb": "02",
		"Mar": "03",
		"Apr": "04",
		"May": "05",
		"Jun": "06",
		"Jul": "07",
		"Aug": "08",
		"Sep": "09",
		"Oct": "10",
		"Nov": "11",
		"Dec": "12",
	}

	# set up some counters
	total_users = 0
	total_users_no_bhl = 0

	# set up some lists for matplotlib and seaborn
	days_total_users = []
	users_per_day_total_users = []
	days_total_users_no_bhl = []
	users_per_day_total_users_no_bhl = []


	'''
	first, let's break up the csv by days for total users'''

	# go through each file in logs
	for filename in os.listdir(path):
		# if it's a parsed total csv
		if filename.endswith('_parsed.csv'):

			# set up an empty list for the days
			dates = []

			# open it
			with open(join(path, filename), 'rb') as csv_file:
				# read it
				reader = csv.reader(csv_file)
				# skip the first line
				next(reader, None)

				# go through each row
				for row in reader: 
					
					# find the day
					day = row[1][:11]
					# add them to the list if they are unique
					if day not in dates:
						dates.append(day)


			'''
			now, let's go through the days list and get the number of total users'''

			# empty list for users
			users = []

			# for each of those days
			for date in dates:

				# add formatted date to totals
				formatted_date = float(date[-4:] + months[date[3:6]] + date[:2])
				days_total_users.append(formatted_date)

				# reopen the csv
				with open(join(path,filename), 'rb') as csv_file:
					# read it
					reader = csv.reader(csv_file)
					# skip the first line
					next(reader, None)

					# go through each row
					for row in reader:

						# find the user and day
						user = row[0]
						day = row[1][:11]

						# find the number of users per day
						if day == date:
							# if we have a unique user, add it to the users list
							if user not in users:
								users.append(user)
							else:
								continue

				# add these things to local and global variables for total users
				number_of_users = len(users)
				total_users += number_of_users
				users_per_day_total_users.append(number_of_users)


	'''
	second, let's break up the csv by days for total users no bhl'''

	# go through each file in logs
	for filename in os.listdir(path):
		# if it's a parsed total csv
		if filename.endswith('_parsed-noBHL.csv'):

			# set up an empty list for the days
			dates = []

			# open it
			with open(join(path, filename), 'rb') as csv_file:
				# read it
				reader = csv.reader(csv_file)
				# skip the first line
				next(reader, None)

				# go through each row
				for row in reader: 
					
					# find the day
					day = row[1][:11]
					# add them to the list if they are unique
					if day not in dates:
						dates.append(day)


			'''
			now, let's go through the days list and get the number of total users no bhl'''

			# empty list for users
			users = []

			# for each of those days
			for date in dates:

				# add formatted date to totals
				formatted_date = float(date[-4:] + months[date[3:6]] + date[:2])
				days_total_users_no_bhl.append(formatted_date)

				# reopen the csv
				with open(join(path,filename), 'rb') as csv_file:
					# read it
					reader = csv.reader(csv_file)
					# skip the first line
					next(reader, None)

					# go through each row
					for row in reader:

						# find the user and day
						user = row[0]
						day = row[1][:11]

						# find the number of users per day
						if day == date:
							# if we have a unique user, add it to the users list
							if user not in users:
								users.append(user)
							else:
								continue

				# add these things to local and global variables for total users no bhl
				number_of_users = len(users)
				total_users_no_bhl += number_of_users
				users_per_day_total_users_no_bhl.append(number_of_users)


	'''
	now for the grand finale'''

	# print total
	print 'total users', total_users

	# print total no bhl
	print 'total users no bhl', total_users_no_bhl

	# matplotlib for total users
	plt.suptitle('Number of Users')
	plt.plot(days_total_users, users_per_day_total_users, label = "Total Users")
	plt.plot(days_total_users_no_bhl, users_per_day_total_users_no_bhl, label = "Total Users (No BHL)")
	plt.xlabel('Date')
	plt.ylabel('Users')
	plt.legend()
	plt.show()

'''
run the function'''

# here we go
number_of_users(path)
