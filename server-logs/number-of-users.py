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


'''
preliminaries'''

# where are the logs?
path = r'C:\Users\Public\Documents\server-logs'

# set up some counters
total_users = 0
total_users_no_bhl = 0

# set up some lists for matplotlib
month_by_month_total_users = []
users_by_month_total_users = []
month_by_month_total_users_no_bhl = []
users_by_month_total_users_no_bhl = []


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

			# get the number of users and add it to list
			row_count = len(users)
			users_by_month_total_users.append(row_count)

			# get the date and add it to list
			date = filename.split('_')[1]
			month_by_month_total_users.append(date)

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

			# get the number of users and add it to list
			row_count = len(users)
			users_by_month_total_users_no_bhl.append(row_count)

			# get the date and add it to list
			date = filename.split('_')[1]
			month_by_month_total_users_no_bhl.append(date)

			# print the results for now
			print 'monthly total users no bhl', date, row_count
			
			# add to total no bhl
			total_users_no_bhl += row_count

# print total
print 'total users', total_users

# print total no bhl
print 'total users no bhl', total_users_no_bhl

# matplotlib for total users
plt.suptitle('Total Users Over Time', fontsize = 14, fontweight = 'bold')
plt.plot(month_by_month_total_users, users_by_month_total_users)
plt.xlabel('Date')
plt.ylabel('Users')
plt.show()

# matplotlib for total users no bhl
plt.suptitle('Total Users Over Time (No BHL Users)', fontsize = 14, fontweight = 'bold')
plt.plot(month_by_month_total_users_no_bhl, users_by_month_total_users_no_bhl)
plt.xlabel('Date')
plt.ylabel('Users')
plt.show()
