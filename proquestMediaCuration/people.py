import os
from os.path import join
from lxml import etree
import re
import csv

path = 'C:\Users\Public\Documents\proquestMediaCuration'

for filename in os.listdir(path):
	the_filename = ''
	the_title = ''
	proquest_people = []
	stanford_ner_people = []

	if filename.endswith('.xml'):
		tree = etree.parse(join(path, filename))
		title = tree.xpath('/video_metadata/title')
		people = tree.xpath('/video_metadata/people/person')
		the_filename = filename.replace('.xml', '')
		the_title = title[0].text.encode('utf-8').strip()
		for person in people:
			proquest_people.append(person.text)

		with open(join(path, filename.replace('.xml', '-TAGGED.txt')), 'r') as f:
    
			raw = f.read()
			people = re.findall('(?<=<PERSON>)(.*?)(?=</PERSON>)', raw)
			for person in set(people):
				stanford_ner_people.append(person)

	print the_title
	print the_filename
	if len(proquest_people) > len(stanford_ner_people):
		difference = len(proquest_people) - len(stanford_ner_people)
		i = 1
		while i <= difference:
			stanford_ner_people.append('')
			i += 1
		for iter in proquest_people:
			print 'PROQUEST: ' + iter + '\tNER: ' + stanford_ner_people[proquest_people.index(iter)]

		for i in stanford_ner_people:
			if i in proquest_people:
				print 'SHARED: ' + i
	else:
		difference = len(stanford_ner_people) - len(proquest_people)
		i = 1
		while i <= difference:
			proquest_people.append('')
			i += 1
		for iter in stanford_ner_people:
			print 'PROQUEST: ' + iter + ', NER: ' + proquest_people[stanford_ner_people.index(iter)]

		for i in proquest_people:
			if i in stanford_ner_people:
				print 'SHARED: ' + i

	for i in proquest_people:
		if i not in stanford_ner_people and i != '':
			print 'UNIQUE TO PROQUEST: ' + i
	for i in stanford_ner_people:
		if i not in proquest_people and i != '':
			print 'UNIQUE TO NER: ' + i
			