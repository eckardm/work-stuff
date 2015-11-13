from lxml import etree as ET
import os
from os.path import join
import csv

# where are the eads?
path = 'C:/Users/eckardm/GitHub/vandura/Real_Masters_all'

# uris
csvs = ['persname-uris.csv', 'corpname-uris.csv', 'famname-uris.csv']

def uri_attribute(agent_type):
	for filename in os.listdir(path):
	tree = etree.parse(join(path, filename))
	agent_types = tree.xpath('//controlaccess/' + agent_type)
	for agent_type in agent_types:
		if agent_type == original or agent_type.split('--')[0] == original:
			xpath = tree.getpath(agent_type):
			xpath.attrib['ref'] = uri
				with open(join(path, filename), 'w') as ead_out:
                ead_out.write(etree.tostring(tree, encoding='utf-8', xml_declaration=True))

def update_agents([csvs]):
	for csv in csvs:
		with open(csv, 'rb') as original_and_uri:
			reader = csv.reader(csv):
			next(reader, None)
			for row in reader:
				original = row[0]
				uri = row[1]
				for i in ['persname', 'corpname', 'famname']:
					if csv.startswith(i):
						uri_attribute(i)

update_agents(csvs)
