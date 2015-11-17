from lxml import etree
import os
from os.path import join
import csv

path = r'C:\Users\eckardm\without-reservations\Real_Masters_all'

persnames_dic = {}
with open('persname-uris.csv', 'rb') as original_and_uri:
	reader = csv.reader(original_and_uri)
	next(reader, None)
	for row in reader:
		original = row[0]
		uri = row[1]
		persnames_dic[original] = uri

corpnames_dic = {}
with open('corpname-uris.csv', 'rb') as original_and_uri:
	reader = csv.reader(original_and_uri)
	next(reader, None)
	for row in reader:
		original = row[0]
		uri = row[1]
		corpnames_dic[original] = uri

famnames_dic = {}
with open('famname-uris.csv', 'rb') as original_and_uri:
	reader = csv.reader(original_and_uri)
	next(reader, None)
	for row in reader:
		original = row[0]
		uri = row[1]
		famnames_dic[original] = uri

def match(dictionary_to_use, agent_text):
	if agent_text in dictionary_to_use:
		ref = dictionary_to_use[agent_text]
	elif agent_text + '.' in dictionary_to_use:
		ref = dictionary_to_use[agent_text + '.']
	elif agent_text.rstrip('.') in dictionary_to_use:
		ref = dictionary_to_use[agent_text.rstrip('.')]
	return ref


for filename in os.listdir(path):
	tree = etree.parse(join(path, filename))
	agents = tree.xpath('//controlaccess/*')
	for agent in agents:
		agent_text = agent.text.split('--')[0].strip()
		print agent_text
		if agent.tag == "persname":
			agent.attrib["ref"] = match(persnames_dic, agent_text)

		elif agent.tag == 'corpname':
			agent.attrib["ref"] = match(corpnames_dic, agent_text)
		elif agent.tag == 'famname':
			agent.attrib["ref"] = match(famnames_dic, agent_text)

	with open(join(path, filename), 'w') as see_i_am_making_all_things_new:
		see_i_am_making_all_things_new.write(etree.tostring(tree, encoding='utf-8', xml_declaration=True))
