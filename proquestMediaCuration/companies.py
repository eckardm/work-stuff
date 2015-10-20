import os
from os.path import join
from lxml import etree
import re
import csv

path = 'C:\Users\Public\Documents\proquestMediaCuration'

for filename in os.listdir(path):
	the_filename = ''
	the_title = ''
	proquest_companies = []
	stanford_ner_companies = []

	if filename.endswith('.xml'):
		tree = etree.parse(join(path, filename))
		title = tree.xpath('/video_metadata/title')
		companies = tree.xpath('/video_metadata/companies/company')
		the_filename = filename.replace('.xml', '')
		the_title = title[0].text.encode('utf-8').strip()
		for company in companies:
			proquest_companies.append(company.text)

		with open(join(path, filename.replace('.xml', '-TAGGED.txt')), 'r') as f:
    
			raw = f.read()
			companies = re.findall('(?<=<ORGANIZATION>)(.*?)(?=</ORGANIZATION>)', raw)
			for company in set(companies):
				stanford_ner_companies.append(company)


	print the_title
	print the_filename
	for i in proquest_companies:
		print 'pq', i
	for i in stanford_ner_companies:
		print 's', i
			