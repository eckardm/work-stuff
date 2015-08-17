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


