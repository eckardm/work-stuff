# import what we need
import os
from os.path import join
import lxml
from lxml import etree as ET
import re
from tqdm import *

# where are the eads?
ead_path = 'C:/Users/eckardm/GitHub/vandura/Real_Masters_all'

# regex
xml = re.compile('\.xml$')

# controlaccess xpath
controlaccess_xpath = '//ead/archdesc//controlaccess/controlaccess/head'

ead_total = 0
ead_with_subject_type = 0

for filename in tqdm(os.listdir(ead_path)):
    if xml.search(filename):
        subject_type = 0
        ead_total += 1
        ead_tree = ET.parse(join(ead_path, filename))
        for sub in ead_tree.xpath(controlaccess_xpath):
            if sub.text.startswith('Subject'):
                subject_type += 1
        if subject_type >= 2:
            ead_with_subject_type += 1
        
print 'Number of EADs: ' + str(ead_total)
print 'Number of EADs with subject type headers: ' + str(ead_with_subject_type)

percentage = float(ead_with_subject_type) / float(ead_total) * 100

print "That's " + str(percentage) + '%'