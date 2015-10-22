import os
from os.path import join
from lxml import etree
import re
import csv

import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import seaborn as sns

path = 'C:\Users\Public\Documents\proquestMediaCuration'

for filename in os.listdir(path):
	the_filename = ''
	the_title = ''
	proquest_places = []
	stanford_ner_places = []

	if filename.endswith('.xml'):
		tree = etree.parse(join(path, filename))
		title = tree.xpath('/video_metadata/title')
		places = tree.xpath('/video_metadata/places/place')
		the_filename = filename.replace('.xml', '')
		the_title = title[0].text.encode('utf-8').strip()
		for place in places:
			proquest_places.append(place.text)

		with open(join(path, filename.replace('.xml', '-TAGGED.txt')), 'r') as f:
			raw = f.read()
			places = re.findall('(?<=<LOCATION>)(.*?)(?=</LOCATION>)', raw)
			for place in set(places):
				stanford_ner_places.append(place)

		venn2([set(proquest_places), set(stanford_ner_places)], set_labels=('ProQuest', 'Standford NER'))
		plt.suptitle(the_title + '\nPlaces', fontsize='x-large') 	
		plt.savefig(the_filename + '-PLACES.png')

		with open('places.txt', 'a') as f:
			
			f.write('FILENAME\n')
			f.write(the_filename + '\n')
			f.write('TITLE\n')
			f.write(the_title + '\n')
			
			f.write('SHARED\n')
			for i in proquest_places:
				if i in stanford_ner_places:
					f.write(i + '\n')

			f.write('PROQUEST\n')
			for i in proquest_places:
				if i not in stanford_ner_places:
					f.write(i + '\n')

			f.write('STANFORD NER\n')
			for i in stanford_ner_places:
				if i not in proquest_places:
					f.write(i + '\n')

			f.write('\n\n')
