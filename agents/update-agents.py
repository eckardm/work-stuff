from lxml import etree
import os
from os.path import join
import csv

path = r'C:\Users\eckardm\without-reservations\Real_Masters_all'

persnames_dic = {}
with open('persname-uris.csv', 'rb') as original_and_uri:
	reader = csv.reader(original_and_uri):
	next(reader, None)
	for row in reader:
		original = row[0]
		uri = row[1]
		persnames[original] = uri

corpnames_dic = {}
with open('corpname-uris.csv', 'rb') as original_and_uri:
	reader = csv.reader(original_and_uri):
	next(reader, None)
	for row in reader:
		original = row[0]
		uri = row[1]
		corpnames[original] = uri

famnames_dic = {}
with open('famname-uris.csv', 'rb') as original_and_uri:
	reader = csv.reader(original_and_uri):
	next(reader, None)
	for row in reader:
		original = row[0]
		uri = row[1]
		famnames[original] = uri

for filename in os.listdir(path):
	tree = etree.parse(join(path, filename))
	agents = tree.xpath('//controlaccess/*')
	for agent in agents:
		if agent.tag == 'persname':
			if '--' in agent.text:
				agent.attrib['ref'] = persnames_dic[agent.text.split('--')[0].strip()]
			else:
				agent.attrib['ref'] = persnames_dic[agent.text.strip()]
		elif agent.tag == 'corpname':
			if '--' in agent.text:
				agent.attrib['ref'] = corpnames_dic[agent.text.split('--')[0].strip()]
			else:
				agent.attrib['ref'] = corpnames_dic[agent.text.strip()]
		elif agent.tag == 'famname':
			if '--' in agent.text:
				agent.attrib['ref'] = famnames_dic[agent.text.split('--')[0].strip()]
			else:
				agent.attrib['ref'] = famnames_dic[agent.text.strip()]
		with open(join(path, filename), 'w') as see_i_am_making_all_things_new:
                see_i_am_making_all_things_new.write(etree.tostring(tree, encoding='utf-8', xml_declaration=True))
