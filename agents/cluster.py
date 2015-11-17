import os
from os.path import join
from lxml import etree
import csv

path = r'C:\Users\eckardm\vandura\Real_Masters_all'

origination_xpath =  '//origination/*'
controlaccess_xpath = '//controlaccess/*'


for filename in os.listdir(path):
	if filename.endswith('xml'):
		print filename
		ead_tree = etree.parse(join(path, filename))
		elements = ead_tree.xpath(origination_xpath) + ead_tree.xpath(controlaccess_xpath)
		for element in elements:
			if element.tag in ["persname"]:
				with open('cluster.csv', 'ab') as csv_file:
					writer = csv.writer(csv_file)
					writer.writerow([element.text.split('--')[0].strip().rstrip('.').encode('utf-8')])