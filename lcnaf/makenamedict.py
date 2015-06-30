# import what we need
import csv

# what's coming form openrefine?
openrefine_persname = 'openrefine_persname.csv'
openrefine_corpname = 'openrefine_corpname.csv'

# empty dictionaries
persnames_dictionary = {}
corpnames_dictionary = {}

print 'Creating persname dictionary.'

# persnames
with open(openrefine_persname, 'rb') as persnames:
    openrefine_persname_reader = csv.reader(persnames)
    # skip the first row
    next(openrefine_persname_reader, None)
    # make dictionary
    for row in openrefine_persname_reader:
        original = row[0]
        link = row[2]
        if link is not None:
            persnames_dictionary[original] = link
            
print 'Persname dictionary created.'

print 'Creating corpname dictionary.'
            
# corpnames
with open(openrefine_persname, 'rb') as corpnames:
    openrefine_corpname_reader = csv.reader(corpnames)
    # skip the first row
    next(openrefine_corpname_reader, None)
    # make dictionary
    for row in openrefine_corpname_reader:
        original = row[0]
        link = row[2]
        if link is not None:
            corpnames_dictionary[original] = link

print 'Persname dictionary created.'

print 'Writing to constants.'
            
# where is constants.py?
constants = 'constants.py'

# put the dictionaries in constants.py
with open(constants, "a") as txt_file:
    txt_file.write('# dictionary for persnames\npersnames_dictionary = ' + str(persnames_dictionary))
    txt_file.write('\n\n# dictionary for corpnames\ncorpnames_dictionary = ' + str(corpnames_dictionary))
    
print 'Written to constants.'