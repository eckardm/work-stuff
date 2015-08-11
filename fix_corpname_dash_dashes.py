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


'''
go through the files, find corpnames with dash dashes and parse them out'''

# go through the files
for filename in tqdm(os.listdir(ead_path)):
    # only look at the xml files
    if filename.endswith('.xml'):

        # create lxml version of the ead
        ead_tree = etree.parse(path.join(ead_path, filename))

        # only look at controlaccess
        for controlaccess in ead_tree.xpath('//controlaccess/controlaccess'):
        
            # empty list to check existing controlaccess points
            controlaccess_stuff = []
            
            # checks all children to check for duplicates
            stuffs = controlaccess.xpath('./*')
            # goes through children
            for stuff in stuffs:
                # adds to list if not already there
                if stuff.text not in controlaccess_stuff:
                    controlaccess_stuff.append(stuff.text)
                        
            # empty lists that we'll use to check for duplicates
            corporate_entities = []
            subjects = []
            
            # getting a list of corpnames in controlaccess, relative to our current position
            corpnames = controlaccess.xpath('./corpname')
            
            # go through each of the corpnames
            for corpname in corpnames:
                # find the dash dashes
                if '--' in corpname.text:
                
                    # split on the dash dash to get the two parts and add to lists...
                    # corpnames
                    # parse
                    corporate_entity = corpname.text.split('--', 1)[0] + '.'
                     # add to list if not a duplicate
                    if corporate_entity not in corporate_entities:
                        corporate_entities.append(corporate_entity)
                        
                    # subjects
                    # parse
                    subject = corpname.text.split('--', 1)[1]
                    # add to list if not a duplicate 
                    if subject not in subjects:
                        subjects.append(subject)
                    
                    
                    '''
                    delete!'''
                    
                    # removes child from parent controlaccess
                    controlaccess.remove(corpname)
                    
            '''
            add them as new elements'''
            
            # corpnames
            # go through the list
            for corpname_itervar in corporate_entities:
                # check duplicates
                if corpname_itervar not in controlaccess_stuff:
                    # initalize and add tag name
                    new_corporate_entity = lxml.etree.Element('corpname')
                    # source
                    new_corporate_entity.attrib['source'] = 'lcnaf'
                    # marc field equivalent
                    new_corporate_entity.attrib['encodinganalog'] = '610'
                    # text
                    new_corporate_entity.text = corpname_itervar
                    # add it at the end
                    controlaccess.insert(-1, new_corporate_entity)
                    
            # subjects
            for subject_itervar in subjects:
                # check duplicates
                if subject_itervar not in controlaccess_stuff:
                    # initalize and add tag name
                    new_subject = lxml.etree.Element('subject')
                    # check for visual materials (we didn't think of this on our own: http://stackoverflow.com/questions/4843158/check-if-a-python-list-item-contains-a-string-inside-another-string)
                    if any('Visual Materials' in stuff_itervar for stuff_itervar in controlaccess_stuff):
                        new_subject.attrib['source'] = 'lctgm'
                    else:
                        # source
                        new_subject.attrib['source'] = 'lcsh'
                    # marc field equivalent
                    new_subject.attrib['encodinganalog'] = '650'
                    # text
                    new_subject.text = subject_itervar
                    # add it at the end
                    controlaccess.insert(-1, new_subject)
                    
        '''
        write it!'''
        
        # setup the writer
        with open(os.path.join(ead_path, filename), mode="w") as behold_i_am_making_all_things_new:
            # write
            behold_i_am_making_all_things_new.write(etree.tostring(ead_tree, xml_declaration=True, encoding='utf-8', pretty_print=True))
