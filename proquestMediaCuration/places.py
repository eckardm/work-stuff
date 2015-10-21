import os
from os.path import join
from lxml import etree
import re
import csv

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

	print the_title
	print the_filename
	for i in proquest_places:
		print 'pq', i
	for i in stanford_ner_places:
		print 's', i
			