from lxml import etree as ET
import os
from os.path import join
import csv
from tqdm import *

# where are the eads?
ead_path = r'C:\Users\eckardm\without-reservations\Real_Masters_all'

# where are the output files?
famname_out = 'famname.csv'
corpname_out = 'corpname.csv'

# headers
famname_headers = ['Type', 'Publish', 'Authority ID', 'Source', 'Rules', 'ORIGINAL', 'Prefix', 'Family Name', 'Dates', 'Qualifier']
corpname_headers = ['Type', 'Publish', 'Authority ID', 'Source', 'Rules', 'ORIGINAL', 'Primary Part of Name', 'Subordinate Name 1', 'Subordinate Name 2', 'Number', 'Dates', 'Qualifier']

# empty list
list_ = []

# xpaths
origination_xpath =  '//origination/*'
controlaccess_xpath = '//controlaccess/*'

print 'Creating dictionary...'

for filename in tqdm(os.listdir(ead_path)):
    if filename.endswith('.xml'):
        ead_tree = ET.parse(join(ead_path, filename))
        elements = ead_tree.xpath(origination_xpath) + ead_tree.xpath(controlaccess_xpath)
        for controlaccess_subelement in elements:
            dictionary = {}
            if controlaccess_subelement.tag in ["famname", "corpname"]:
                dictionary['Type'] = controlaccess_subelement.tag
                dictionary['ORIGINAL'] = controlaccess_subelement.text.split("--")[0].strip()
                if 'authfilenumber' in controlaccess_subelement.attrib:
                    dictionary['Authority ID'] = controlaccess_subelement.get('authfilenumber')
                if 'source' in controlaccess_subelement.attrib:
                    dictionary['source'] = controlaccess_subelement.get('source')
                list_.append(dictionary)

print 'Creating <famname> CSV...'
        
with open(famname_out, 'wb') as famname_csv:
    famname_header_writer = csv.writer(famname_csv)
    famname_header_writer.writerow(famname_headers)

unique_list = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in list_)]

for dictionary_item in tqdm(unique_list):        
    famname_row = ['famname', 'TRUE']
    if dictionary_item['Type'] == 'famname':
        famname_row.append(dictionary_item.get('Authority ID', ""))
        famname_row.append(dictionary_item.get('source', ""))
        famname_row.append('')
        famname_row.append(dictionary_item['ORIGINAL'].encode('utf-8'))

        with open(famname_out, 'ab') as famname_csv_take_two:
            famname_writer = csv.writer(famname_csv_take_two)
            famname_writer.writerow(famname_row)

print 'Creating <corpname> CSV...'
        
with open(corpname_out, 'wb') as corpname_csv:
    corpname_header_writer = csv.writer(corpname_csv)
    corpname_header_writer.writerow(corpname_headers)
    
for dictionary_item in tqdm(unique_list):          
    corpname_row = ['corpname', 'TRUE']
    if dictionary_item['Type'] == 'corpname':
        corpname_row.append(dictionary_item.get('Authority ID', ""))
        corpname_row.append(dictionary_item.get('source', ""))
        corpname_row.append('')
        corpname_row.append(dictionary_item['ORIGINAL'].encode('utf-8'))

        with open(corpname_out, 'ab') as corpname_csv_take_two:
            corpname_writer = csv.writer(corpname_csv_take_two)
            corpname_writer.writerow(corpname_row)  
                    
print 'Done!'  
