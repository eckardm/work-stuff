import lxml
from lxml import etree as ET
import os
from os.path import join
import re

# where are the eads?
ead_path = 'S:/FindingAids/EAD/Master'

# where are the output files?
persname_output = 'persname.txt'
corpname_output = 'corpname.txt'
error_output = 'error.csv'

# how to tell xml
xml = re.compile('\.xml$')

# controlaccess xpath
controlaccess_xpath = '//ead/archdesc//controlaccess/*'

# error counter
error_counter = 0

# got through the files
for filename in os.listdir(ead_path):
    # only look at xml
    if xml.search(filename):
        ead_tree = ET.parse(join(ead_path, filename))
        for sub in ead_tree.xpath(controlaccess_xpath):
            try: 
                if sub.tag == 'persname':
                    with open(persname_output, 'wb') as text_file:
                        text_file.write(sub.text.encode("utf-8") + '\n')
                elif sub.tag == 'corpname':
                    with open(corpname_output, 'wb') as text_file:
                        text_file.write(sub.text.encode("utf-8") + '\n')
            except:
                error_counter += 1
                with open(error_output, 'wb') as text_file:
                    text_file.write(filename + ', ' + sub.tag + '\n')
                    
print 'There were ' + str(error_counter) + ' errors!'