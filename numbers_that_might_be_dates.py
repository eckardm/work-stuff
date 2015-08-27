'''
first, import what we need'''

# lxml is a powerful xml document parser, you'll need to download it
from lxml import etree

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# re provide regular expression matching operations
import re

# tqdm adds a progress meter to loops, you'll need to install it
from tqdm import *


'''
go through eads and look for numbers that might be dates'''

# go through each of the files in the ead folder
for filename in tqdm(os.listdir(ead_folder)):
    # but only do the ones that are actually eads (we can tell because they are xml files)
    if filename.endswith('.xml'):
        # create an etree (part of lxml) tree that we can parse
        ead_tree = etree.parse(join(ead_folder, filename))
        