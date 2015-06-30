# import what we need
import os
from os.path import join
import csv
import lxml
from lxml import etree as ET
import re

# from constants import persnames_dictionary
from constants import corpnames_dictionary

# where are the eads?
ead_path_test = 'C:/Users/Public/Documents/Real_Masters_all'
ead_path_production = 'C:/Users/eckardm/GitHub/vandura/Real_Masters_all'

# regex
xml = re.compile('\.xml$')

# controlaccess xpath
controlaccess_xpath = '//ead/archdesc//controlaccess/*'

print 'Updating EADs.'

# go through the files
for filename in os.listdir(ead_path_test):
    # only look at xml
    if xml.search(filename):
        print filename
        # parse
        ead_tree = ET.parse(join(ead_path_test, filename))
        # go through the eads
        for sub in ead_tree.xpath(controlaccess_xpath):
            print '\rWorking on it... |',
            print '\rWorking on it... /',
            print '\rWorking on it... -',
            print '\rWorking on it... \\',
            print '\rWorking on it... |',
            print '\rWorking on it... /',
            print '\rWorking on it... -',
            print '\rWorking on it... -',
            print '\rWorking on it... \\',
            # persname
            if sub.tag == 'persname' and sub.text is not None and '--' not in sub.text:
                original = sub.text.strip()
                if original in persnames_dictionary:
                    persname_xpath = ead_tree.getpath(sub)
                    persname_update = ead_tree.xpath(persname_xpath)
                    persname_update[0].attrib['authfilenumber'] = persnaems_dictionary[original]
                    outfile = open(join(ead_path_test, filename), 'w')
                    outfile.write(ET.tostring(ead_tree, encoding="utf-8", xml_declaration=True))
                    outfile.close()
            # corpname 
            if sub.tag == 'corpname' and sub.text is not None and '--' not in sub.text:
                original = sub.text.strip()
                if original in corpnames_dictionary:
                    corpname_xpath = ead_tree.getpath(sub)
                    corpname_update = ead_tree.xpath(corpname_xpath)
                    corpname_update[0].attrib['authfilenumber'] = corpnames_dictionary[original]
                    outfile = open(join(ead_path_test, filename), 'w')
                    outfile.write(ET.tostring(ead_tree, encoding="utf-8", xml_declaration=True))
                    outfile.close()
                    
print '\rUpdated EADs'