'''
first things first, import what we need'''

# lxml is the most feature-rich and easy-to-use library for processing xml (and html), you'll need to install it
import lxml
from lxml import etree
# os provides a portable way of using operating system dependent functionality
import os
from os import path
# tqdm adds a progress meter to your loops in a second
from tqdm import *


'''
preliminaries'''

# where are the eads?
ead_path = 'C:\Users\Public\Documents\Real_Masters_all'
# ead_path = 'C:\Users\eckardm\GitHub\vandura\Real_Masters_all'

# where are we looking in the eads?
xpaths = ['//controlaccess/*', '//origination/*']


'''
go through the files, find corpnames with dash dashes and parse them out'''

def dash_dashes(xpath):

    # go through the files
    for filename in tqdm(os.listdir(ead_path)):
        # only look at the xml files
        if filename.endswith('.xml'):
    
            # create lxml version of the ead
            ead_tree = etree.parse(path.join(ead_path, filename))
        
            # go through each of the corpnames
            for xpath_itervar in ead_tree.xpath(xpath):
            
                # empty lists
                corporate_entities = []
                subjects = []
                
                # find the parent (we'll need it later)
                parent = ead_tree.getpath(xpath)
        
                # only look at corpnamess and dash dashes
                if xpath_itervar.tag == 'corpname' and '--' in xpath_itervar.text:
                    
                    # split on the dash dash to get the two parts and add to lists...
                    # corpnames
                    # parse
                    corporate_entity = xpath_itervar.text.split('--', 1)[0] + '.'
                    # add to list if not a duplicate
                    if corporate_entity not in corporate_entities:
                        corporate_entities.append(corporate_entity)
                    
                    # subjects
                    # parse
                    subject = xpath_itervar.text.split('--', 1)[1]
                    # add to list if not a duplicate 
                    if subject not in subjects:
                        subjects.append(subject)
                    
                    
                    '''
                    deletes the original element'''
                    # delete the child
                    parent.remove(xpath_itervar)
                    
                    
                '''
                add them as new elements'''
                
                # corpnames
                # go through the list
                for corpname_itervar in corporate_entities:
                    # initalize and add tag name
                    new_corporate_entity = lxml.etree.Element('corpname')
                    # source
                    new_corporate_entity.attrib['source'] = 'lcnaf'
                    # marc field equivalent
                    new_corporate_entity.attrib['encodinganalog'] = '610'
                    # text
                    new_corporate_entity.text = corpname_itervar
                    # add it
                    parent.addchild(new_corporate_entity)
                        
                # subjects
                for subject_itervar in subjects:
                    # initalize and add tag name
                    new_subject = lxml.etree.Element('subject')
                    # source
                    new_subject.attrib['source'] = 'lcsh'
                    # marc field equivalent
                    new_subject.attrib['encodinganalog'] = '650'
                    # text
                    new_subject.text = subject_itervar
                    # add it 
                    parent.addchild(new_subject)

        
        '''
        write it!'''
        
        # setup the writer
        with open(os.path.join(ead_path, filename), mode="w") as behold_i_am_making_all_things_new:
            # write
            behold_i_am_making_all_things_new.write(etree.tostring(ead_tree, xml_declaration=True, encoding='utf-8', pretty_print=True))
                    
                    
'''
run it!'''

for xpath in xpaths:
    dash_dashes(xpath)
