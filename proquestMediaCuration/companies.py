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
			total_proquest.append(company.text)

		with open(join(path, filename.replace('.xml', '-TAGGED.txt')), 'r') as f:
			raw = f.read()
			companies = re.findall('(?<=<ORGANIZATION>)(.*?)(?=</ORGANIZATION>)', raw)
			for company in set(companies):
				stanford_ner_companies.append(company)
				total_stanford_ner.append(company)

		# venn2([set(proquest_companies), set(stanford_ner_companies)], set_labels=('ProQuest', 'Standford NER'))
		# plt.suptitle(the_title + '\nCompanies', fontsize='x-large') 
		# plt.show()

		with open('companies.txt', 'a') as f:
			
			f.write(the_title + '\n')
			f.write(the_filename + '\n')
			
			f.write('SHARED\n')
			for i in sorted(set(proquest_companies)):
				if i in stanford_ner_companies:
					f.write(i + '\n')

			f.write('PROQUEST\n')
			for i in sorted(set(proquest_companies)):
				if i not in stanford_ner_companies:
					f.write(i + '\n')

			f.write('STANFORD NER\n')
			for i in sorted(set(stanford_ner_companies)):
				if i not in proquest_companies:
					f.write(i + '\n')

			f.write('\n\n')

venn2([set(total_proquest), set(total_stanford_ner)], set_labels=('ProQuest (Total)', 'Standford NER(Total)'))
plt.suptitle('Companies (Total)', fontsize='x-large') 	
plt.show()	
