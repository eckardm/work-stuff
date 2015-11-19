import os
from os.path import join
from lxml import etree
import re
import csv

import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import seaborn as sns

path = 'C:\Users\Public\Documents\proquestMediaCuration'

total_proquest = []
total_stanford_ner = []

for filename in os.listdir(path):
	proquest_people = []
	stanford_ner_people = []

	if filename.endswith('.xml'):
		tree = etree.parse(join(path, filename))
		title = tree.xpath('/video_metadata/title')
		people = tree.xpath('/video_metadata/people/person')
		the_filename = filename.replace('.xml', '')
		the_title = title[0].text.encode('utf-8').strip()
		for person in people:
			proquest_people.append(person.text.lower())
			total_proquest.append(person.text.lower())

		with open(join(path, filename.replace('.xml', '-TAGGED.txt')), 'r') as f:
			raw = f.read()
			people = re.findall('(?<=<PERSON>)(.*?)(?=</PERSON>)', raw)

			for person in people:
				if len(person.split(' ')) >= 2:
					stanford_ner_people.append(person.lower())
					total_stanford_ner.append(person.lower())

		# venn2([set(proquest_people), set(stanford_ner_people)], set_labels=('ProQuest', 'Standford NER'))
		# plt.suptitle(the_title + '\nPeople', fontsize='x-large') 	
		# plt.show()
		
		with open('people.txt', 'a') as f:
			
			f.write(the_title + '\n')
			f.write(the_filename + '\n')
			
			f.write('SHARED\n')
			for i in sorted(set(proquest_people)):
				if i in stanford_ner_people:
					f.write(i + '\n')

			f.write('PROQUEST\n')
			for i in sorted(set(proquest_people)):
				if i not in stanford_ner_people:
					f.write(i + '\n')

			f.write('STANFORD NER\n')
			for i in sorted(set(stanford_ner_people)):
				if i not in proquest_people:
					f.write(i + '\n')

			f.write('\n\n')

venn2([set(total_proquest), set(total_stanford_ner)], set_labels=('ProQuest (Total)', 'Stanford NER(Total)'))
plt.suptitle('People (Total)', fontsize='x-large') 	
plt.show()			
