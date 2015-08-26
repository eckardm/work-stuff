'''
first things first, import what we need'''

# csv implements classes to read and write tabular data in csv format
import csv

# json is a lightweight data interchange format inspired by javascript object literal syntax
import json


'''
preliminaries'''

# where is the csv that has been exported from openrefine?
corpname_csv = 'agents-corpname.csv'

# preliminaries for using archivesspace api
# base url
base_url = 'http://localhost:8089"
# username default
username = 'admin'
# password default
password = 'password'


'''
go through csv, create a list of dictionaries for each entry'''


'''
for reference

 "names": [
    {
      "lock_version": 0,
      "primary_name": "Primary Part of Name",
      "subordinate_name_1": "Subordinate Name 1",
      "subordinate_name_2": "Subordinate Name 2",
      "number": "Number",
      "dates": "Dates",
      "qualifier": "Qualifier",
      "sort_name": "Primary Part of Name. Subordinate Name 1. Subordinate Name 2 (Number : Dates) (Qualifier)",
      "sort_name_auto_generate": true,
      "created_by": "admin",
      "last_modified_by": "admin",
      "create_time": "2015-08-26T13:47:36Z",
      "system_mtime": "2015-08-26T13:47:36Z",
      "user_mtime": "2015-08-26T13:47:36Z",
      "authorized": true,
      "is_display_name": true,
      "source": "naf",
      "jsonmodel_type": "name_corporate_entity",
      "use_dates": [
        
      ],
      "authority_id": "Authority ID"
    }
  ]'''

# open the corpname csv in read mode
with open(corpname_csv, 'r') as corpname_csv_file:
    # read it to get the data
    corpname_data = csv.reader(corpname_csv_file)
    
    # go through each row
    for row in corpname_data:
        
        # match up fields to row index
        # primary name
        primary_name = row[6]
        # subordinate name 1
        subordinate_name_1 = row[7]
        # subordinate name 2
        subordinate_name_2 = row[8]
        # qualifier
        qualifier = row[11]
        # authority id
        authority_id = row[2]
        
        # set up list and dictionaries
        row_dictionary = {}
        # empty list for corpname dictionaries
        corpname_list = []
        # empty dictionary
        corpname_dictionary = {}
        
        # add to dictionary
        # if primary name exists
        if primary_name:
            # append it
            corpname_dictionary["primary_name"] = primary_name
        # if subordinate name exists
        if subordinate_name_1:
            # append it
            corpname_dictionary["subordinate_name_1"] = subordinate_name_1
        # if a second subordinate name exists
        if subordinate_name_2:
            # append it
            corpname_dictionary["subordinate_name_1"] = subordinate_name_1
        # if a qualifer exists
        if qualifier:
            # append it
            print qualifier
        # if authority id exists
        if authority_id:
            # add it to dictionary
            corpname_dictionary["authority_id"] = authority_id
                
        # add other required fields to dictionary
        # source
        corpname_dictionary["source"] = "naf"
        # auto generate sort name
        corpname_dictionary["sort_name_auto_generate"] = True
        
        # add dictionary to list
        corpname_list.append(corpname_dictionary)
        
        # add list to dictionary
        row_dictionary["names"] = corpname_list
        
        
        '''
        create json out of this'''
        
        # create json
        corpname_json = json.dumps(row_dictionary)
        
        print corpname_json
