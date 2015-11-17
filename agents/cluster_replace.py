import os
from os.path import join
from lxml import etree
import csv


path = r'C:\Users\eckardm\vandura\Real_Masters_all'
new_csv = 'cluster-new.csv'

dictionary = {}

# open the csv file
with open(new_csv, 'rb') as csv_file:
    
    # "read" the csv file
    reader = csv.reader(csv_file)
    # skip a line, since our csv file now has headers from openrefine
    next(reader, None)
    
    # go through each row in csv
    for row in reader:
    
        # we need to tell python what columns/index correspond to what data
        old = row[0]
        new = row[1]
        
        # lets check to see if we need to actually do anything
        if old != new:

            dictionary[old] = new

for filename in os.listdir(path):
    print filename
    tree = etree.parse(join(path, filename))
    agents = tree.xpath('//origination/persname') + tree.xpath('//controlaccess/persname')


    for agent in agents:
        agent_text = agent.text.split('--')[0].strip().rstrip('.').encode('utf-8')
        
        if agent_text in dictionary:
            agent.text = dictionary[agent_text].encode('utf-8')


            with open(join(path, filename), 'w') as see_i_am_making_all_things_new:
              see_i_am_making_all_things_new.write(etree.tostring(tree, encoding='utf-8', xml_declaration=True))

print "That's it, we're done!"