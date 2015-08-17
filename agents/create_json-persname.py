'''
first things first, import what we need'''

# csv implements classes to read and write tabular data in csv format
import csv

# json is a lightweight data interchange format inspired by javascript object literal syntax
import json


'''
open the csv and json files'''

# open the csv file in read mode
persname_csv = open('agents-persname.csv', 'r')

# open the json file in write mode
persname_json = open('agents-persname.json', 'w')


'''
indicate csv fieldnames for json'''

# set up a list
field_names = ('prefix', 'title', 'primary_name', 'rest_of_name', 'number', 'suffix', 'fuller_form', 'dates', 'authority_id', 'source', 'name_order')


'''
go through csv and create json'''

# read the csv as if it were a dictionary
persname_csv_reader = csv.DictReader(persname_csv, field_names)

# go through each row
for row in persname_csv_reader:
    # dump the json
    json.dump(row, persname_json)
    # add a newline
    persname_json.write('\n')
