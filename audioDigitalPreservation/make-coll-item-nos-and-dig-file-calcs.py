# collections implements specialized container datatypes providing alternatives to python's general purpose built-in containers
from collections import defaultdict

# csv implements classes to read and write tabular data in csv format
import csv

# get all of the unique collection item numbers
coll_item_nos = []
with open(r'C:\Users\Public\Documents\audioDigitalPreservationItemView\audioDigitalPreservationItemView.mer') as csv_file:
	reader = csv.DictReader(csv_file)
	for row_dict in reader:
		if row_dict["CollItemNo"] and row_dict["CollItemNo"] not in coll_item_nos:
			coll_item_nos.append(row_dict["CollItemNo"])

# make a special dictionary that can take lists
coll_item_nos_and_dig_file_calcs = defaultdict(list)

# go through the unique collection item numbers and get all of their associated digital file calculations
for i in coll_item_nos:
	with open(r'C:\Users\Public\Documents\audioDigitalPreservationItemView\audioDigitalPreservationItemView.mer') as csv_file:
		reader = csv.DictReader(csv_file)
		for row_dict in reader:
			if row_dict["CollItemNo"] == i:
				coll_item_nos_and_dig_file_calcs[i].append(row_dict["DigFile Calc"])

# write it to a constants file and clean it up later
with open('coll_item_nos_and_dig_file_calcs.py', 'w') as txt_file:
	txt_file.write(str(coll_item_nos_and_dig_file_calcs))
