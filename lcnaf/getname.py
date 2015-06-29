'''
step one of https://github.com/mcarruthers/LCNAF-Named-Entity-Reconciliation, hopefully we'll get some lcnaf or viaf out of this'''

import lxml
from lxml import etree as ET
import os
from os.path import join
import re

# where are the eads?
ead_path = 'C:/Users/eckardm/GitHub/vandura/Real_Masters_all'

# where are the output files?
persname_output = 'persname.txt'
corpname_output = 'corpname.txt'
error_output = 'error.csv'

# regex
xml = re.compile('\.xml$')

# controlaccess xpath
controlaccess_xpath = '//ead/archdesc//controlaccess/*'

# error counter
error_counter = 0

# got through the files
for filename in os.listdir(ead_path):
    # only look at xml
    if xml.search(filename):
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        print '\rWorking on it... |',
        print '\rWorking on it... /',
        print '\rWorking on it... -',
        print '\rWorking on it... -',
        print '\rWorking on it... \\',
        ead_tree = ET.parse(join(ead_path, filename))
        for sub in ead_tree.xpath(controlaccess_xpath):
            if sub.tag == 'persname' and sub.text is not None:
                if '--' in sub.text:
                    output = sub.text.split('--')[0].strip()
                else:
                    output = sub.text
                with open(persname_output, 'a') as text_file:
                    text_file.write(output.encode("utf-8") + '\n')
            elif sub.tag == 'corpname' and sub.text is not None:
                if '--' in sub.text:
                    output = sub.text.split('--')[0].strip()
                else:
                    output = sub.text
                with open(corpname_output, 'a') as text_file:
                    text_file.write(output.encode("utf-8") + '\n')
                    
print '\rThere were ' + str(error_counter) + ' errors!'