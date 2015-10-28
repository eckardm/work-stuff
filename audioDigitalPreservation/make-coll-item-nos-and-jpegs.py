#  provides a portable way of using operating system dependent functionality
import os

# collections implements specialized container datatypes providing alternatives to python's general purpose built-in containers
from collections import defaultdict

# locate all the batches
batches = ['R:/Digitization/Audio/Vendor Digitization/Reel-to-Reel Project/Batch 1/20130218/', 'R:/Digitization/Audio/Vendor Digitization/Reel-to-Reel Project/Batch 2/20130716/', 'R:/Digitization/Audio/Vendor Digitization/Reel-to-Reel Project/Batch 3/20140117/', 'R:/Digitization/Audio/Vendor Digitization/Reel-to-Reel Project/Batch 4/20140826/']

# hey, hey! use a function
def make_coll_item_nos_and_jpegs(batch):

	# make a special dictionary that can take lists
	coll_item_nos_and_jpegs = defaultdict(list)

	# go recursively (selectively) through each directory
	for collection_id in os.listdir(batch):

		# this try statement allows us to only get the stuff we need
		try:

			# get jpeg filenames
			for coll_item_no in os.listdir(batch + collection_id):
				for filename in os.listdir(batch + collection_id + '/' + coll_item_no):
					coll_item_nos_and_jpegs[coll_item_no].append(filename)
		
		# and if we don't, no big deal
		except:
			continue

	# write it to a constants file to clean up later			
	with open('coll_item_nos_and_jpegs.py', 'ab') as txt_file:
				txt_file.write(str(coll_item_nos_and_jpegs))

# do the function on each of the batches
for batch in batches:
	make_coll_item_nos_and_jpegs(batch)
