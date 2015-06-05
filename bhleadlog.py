# import what we need
import csv
import re

# empty lists for ead identifiers and queries
ead_identifiers = []
queries = []

# counts for requests, ead identifiers and queries
requests_count = 0
ead_identifiers_count = 0
queries_count = 0

# where are the logfiles?
logfiles = 'subsetbhleadlog.csv'

# open the logs
with open(logfiles, 'rb') as csvfile:
    # read the logs
    logreader = csv.reader(csvfile, delimiter=',')
    # go through each row
    for row in logreader:
        # find the requests
        request = row[2]
        # update count
        requests_count += 1
        # find the ead identifiers
        ead_identifier_matches = re.findall('umich-bhl-\d+\.?\d', request)
        # go through them
        for ead_identifier in ead_identifier_matches:
            # make sure they are unique
            if ead_identifier not in ead_identifiers:
                # add them to empty list
                ead_identifiers.append(ead_identifier)
                # update count
                ead_identifiers_count += 1
        # find the queries
        query_matches = re.findall('(?<=q1=)(.*)(?=&Submit=Search)', request)
        # go through them
        for query in query_matches:
            # make sure they are unique
            if query not in queries:
                # add them to empty list
                queries.append(query)
                # update count
                queries_count += 1
                # add them to empty lis
                
# print requests
print 'There were ' + str(requests_count) + ' requests today.'

# print unique ead identifiers
print 'There were ' + str(ead_identifiers_count) + ' unique EADs accessed today.'
print 'Here they are:'
for i in ead_identifiers:
    print i
    
#print unique requests
print 'There were ' + str(queries_count) + ' unique queries today.'
print 'Here they are:'
for i in queries:
    print i