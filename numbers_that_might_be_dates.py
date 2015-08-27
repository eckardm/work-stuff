'''
first, import what we need'''

# lxml is a powerful xml document parser, you'll need to download it
from lxml import etree

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# tqdm adds a progress meter to loops, you'll need to install it
from tqdm import *

'''
go through eads and look for numbers that might be dates'''
