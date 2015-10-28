# collections implements specialized container datatypes providing alternatives to python's general purpose built-in containers
from collections import defaultdict

# csv implements classes to read and write tabular data in csv format
import csv

# create an iterable list of the rows (reader objects are not iterable)
audio_digital_preservation_item_view_rows = []
with open(r'C:\Users\Public\Documents\audioDigitalPreservationItemView\audioDigitalPreservationItemView.mer') as csv_file:
	reader = csv.reader(csv_file)
	next(reader, None)
	for row in reader:
		audio_digital_preservation_item_view_rows.append(row)

# go through that list and fill in empty collection item numbers
for row in audio_digital_preservation_item_view_rows:
	# if it already has one, just skip it
	if row[9]:
		continue
	# else, go to the row right before that, grab the collection item number, and insert it in the proper spot
	else:
		row[9] = audio_digital_preservation_item_view_rows[audio_digital_preservation_item_view_rows.index(row) - 1][9]

# make a special dictionary that can take lists
coll_item_nos_and_audio_genres = defaultdict(list)

# go through that again, this time adding collection item numbers and lists of audio genres to the dictionary
for row in audio_digital_preservation_item_view_rows:
	if row[42] and row[42] not in coll_item_nos_and_audio_genres[row[9]]:
		coll_item_nos_and_audio_genres[row[9]].append(row[42])
	
# write it to a constants file and clean it up later
with open('coll_item_nos_and_audio_genres.py', 'w') as txt_file:
	txt_file.write(str(coll_item_nos_and_audio_genres))
	