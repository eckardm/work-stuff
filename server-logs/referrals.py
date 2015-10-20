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

def referrals(path):

	# set up some counters for umich stuff
	archivegrid = 0
	bhl_collection_highlights = 0
	bhl_subject_guides = 0 # legacy-support and not EAD
	bhl_ead_search = 0
	bhl_ead_a_to_z = 0
	bhl_ead_um = 0
	deepblue = 0
	mirlyn = 0
	finding_aids = 0
	finding_aids_older_interface = 0
	umich = 0
	digital_collections = 0

	# set up some counters for social media
	facebook = 0
	twitter = 0

	# set up some counters for search engines
	yahoo = 0
	aol = 0
	ask = 0
	bing = 0
	google = 0

	# and some others
	no = 0
	other = 0


	'''
	get the referrals for total users'''

	# go through each file in logs
	for filename in os.listdir(path):
		# if it's a parsed total csv no bhl
		if filename.endswith('_parsed-noBHL.csv'):

			with open('searches.txt', 'w') as text_file:

				# open it
				with open(join(path, filename), 'rb') as csv_file:
					# read it
					reader = csv.reader(csv_file)
					# skip the first line
					next(reader, None)

					# go through each row
					for row in reader: 

						# referrals
						request = row[4]

						# characterize them
						if request == '-':
							no += 1
						elif 'http://184.168.105.185/archivegrid' in request:
							archivegrid += 1
						elif 'http://bentley.umich.edu/collection-highlights' in request:
							bhl_collection_highlights += 1
						elif 'http://bentley.umich.edu/legacy-support/' in request and 'http://bentley.umich.edu/legacy-support/EAD/' not in request:
							bhl_subject_guides += 1
						elif request == 'http://bentley.umich.edu/legacy-support/EAD/':
							bhl_ead_search += 1
						elif request == 'http://bentley.umich.edu/legacy-support/EAD/ead_uofm.php':
							bhl_ead_um += 1
						elif 'http://bentley.umich.edu/legacy-support/EAD/ead_' in request:
							bhl_ead_a_to_z += 1
						elif 'http://deepblue.lib.umich.edu/handle/' in request:
							deepblue += 1
						elif 'facebook.com' in request:
							facebook += 1
						elif 'mirlyn.lib.umich.edu' in request:
							mirlyn += 1
						elif request == 'http://quod.lib.umich.edu/' or request == 'http://quod.lib.umich.edu/lib/colllist/':
							digital_collections += 1
						elif 'http://quod.lib.umich.edu/b/' in request:
							finding_aids += 1
						elif 'http://quod.lib.umich.edu/cgi/f/findaid/findaid-idx' in request:
							finding_aids_older_interface += 1
						elif 'search.yahoo' in request:
							yahoo += 1
						elif 'search.aol' in request:
							aol += 1
						elif 'http://umich.edu/search/keywords/' in request:
							umich += 1
						elif 't.co/' in request:
							twitter += 1
						elif 'ask.com' in request:
							ask += 1
						elif 'bing.com' in request:
							bing += 1
						elif 'google.' in request:
							google += 1
						else:
							other += 1

	'''
	calculate percentages and graph'''

	total = no + archivegrid + bhl_collection_highlights + bhl_subject_guides + bhl_ead_um + bhl_ead_a_to_z + bhl_ead_search + deepblue + facebook + mirlyn + digital_collections + finding_aids + finding_aids_older_interface + yahoo + aol + umich + twitter + ask + bing + google + other

	social_media = facebook + twitter

	search_engines = yahoo + aol + ask + bing + google

	def percentage(counter):
		percentage = float(counter) / (float(total) - float(no)) * 100
		return percentage

	fractions = [percentage(archivegrid), percentage(bhl_collection_highlights), percentage(bhl_subject_guides), percentage(bhl_ead_um), percentage(bhl_ead_a_to_z), percentage(bhl_ead_search), percentage(deepblue), percentage(facebook), percentage(mirlyn), percentage(digital_collections), percentage(finding_aids), percentage(finding_aids_older_interface), percentage(yahoo), percentage(aol), percentage(umich), percentage(twitter), percentage(ask), percentage(bing), percentage(google), percentage(other)]
	labels = ['ArchiveGrid', 'Collection Highlights', 'Subject Guides', 'Finding Aids (UM)', 'Finding Aids (A-Z)', 'Finding Aids (Search)', 'Deep Blue', 'Facebook', 'Mirlyn', 'Digital Collections', 'Finding Aids (Other)', 'Finding Aids (Older Interface)', 'Yahoo', 'AOL', 'University of Michigan', 'Twitter', 'Ask', 'Bing', 'Google', 'Other']
	plt.suptitle('Referrals (No BHL)', fontsize = 'x-large')
	plt.pie(fractions, labels = labels, autopct='%1.1f%%')
	plt.show()

	def percentage_subset(counter):
		percentage_subset = float(counter) / (float(total) - float(no) - float(finding_aids) - float(finding_aids_older_interface))
		return percentage_subset

	fractions_subset = [percentage_subset(archivegrid), percentage_subset(bhl_collection_highlights), percentage_subset(bhl_subject_guides), percentage_subset(bhl_ead_um), percentage_subset(bhl_ead_a_to_z), percentage_subset(bhl_ead_search), percentage_subset(deepblue), percentage_subset(mirlyn), percentage_subset(digital_collections), percentage_subset(social_media), percentage_subset(search_engines), percentage_subset(other)]
	labels_subset = ['ArchiveGrid', 'Collection Highlights', 'Subject Guides', 'Finding Aids (UM)', 'Finding Aids (A-Z)', 'Finding Aids (Search)', 'Deep Blue', 'Mirlyn', 'Digital Collections', 'Social Media', 'Search Engines', 'Other']
	print len(fractions_subset)
	print len(labels_subset)
	plt.suptitle('Referrals (No BHL, DLXS Filtered Out)', fontsize = 'x-large')
	plt.pie(fractions_subset, labels = labels_subset, autopct='%1.1f%%')
	plt.show()

referrals(path)
