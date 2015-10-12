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

# set up some counters
total_users = 0
total_users_no_bhl = 0


'''
let's get down to business'''

# go through each file in logs
for filename in os.listdir(path):

	# if it's a parsed total csv
	if filename.endswith('_parsed.csv'):
		# set up a list of users
		users = []

		# open it
		with open(join(path, filename), 'rb') as csv_file:
			# read it
			reader = csv.reader(csv_file)
			# skip the first line
			next(reader, None)

			# go through each row
			for row in reader: 
				# find the user
				user = row[0]
				# add them to the list if they are unique
				if user not in users:
					users.append(user)

			# get the number of users
			row_count = len(users)

			# get the date
			date = filename.split('_')[1][:4] + '-' + filename.split('_')[1][-2:]

			# print the results, for now
			print 'monthly total users', date, row_count

			# add to total
			total_users += row_count

	# if it's a parsed no bhl csv		
	if filename.endswith('_parsed-noBHL.csv'):
		# set up a list of users
		users = []

		# open it
		with open(join(path, filename), 'rb') as csv_file:
			# read it
			reader = csv.reader(csv_file)
			# skip the first line
			next(reader, None)

			# go through each row
			for row in reader: 
				# find the user
				user = row[0]
				# add them to the list if they are unique
				if user not in users:
					users.append(user)

			# get the number of users
			row_count = len(users)

			# get the date
			date = filename.split('_')[1][:4] + '-' + filename.split('_')[1][-2:]

			# print the results for now
			print 'monthly total users no bhl', date, row_count
			
			# add to total no bhl
			total_users_no_bhl += row_count

# print total
print 'total users', total_users

# print total no bhl
print 'total users no bhl', total_users_no_bhl
