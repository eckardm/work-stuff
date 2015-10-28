# lxml is a pythonic binding for the c libraries libxml2 and libxslt
from lxml.builder import E
from lxml import etree as ET

# csv implements classes to read and write tabular data in csv format
import csv

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# we made these earlier
from coll_item_nos_and_dig_file_calcs import coll_item_nos_and_dig_file_calcs
from coll_item_nos_and_audio_genres import coll_item_nos_and_audio_genres
from coll_item_nos_and_jpegs import coll_item_nos_and_jpegs
from batches import batches

# a list of programs, because these are exceptions to the rule
programs = ['8730', '90139', '87334', '87250', '8738']

# there is one encoding error that keeps throwing this off, for the time being, i'm putting it here
errors = []
jpeg_errors = []

# try statement is because of the encoding error, i intend to get rid of it
try:

	# open the export from beal and go through it
	with open(r'C:\Users\Public\Documents\audioDigitalPreservationItemView\audioDigitalPreservationItemView.mer') as csv_file:
		reader = csv.DictReader(csv_file)
		for row_dict in reader:
			if row_dict["CollItemNo"]:

				# start constructing the xml
				audio_item = E.audio_item(
					E("dc.identifier.other", row_dict["CollItemNo"]),
					E("dc.title", "Sound Recording - " + row_dict["ItemTitle"]),
					E("dc.contributor.author", row_dict["CollectionCreator"]),
					E("dc.date.issued", "2015"),
					E("dc.date.created", row_dict["Files_Return_Date"][-4:]),
					E("dc.coverage.temporal", row_dict["ItemDate"]),
					# this seems inelegant, but it has to do with the way beal does the export
					E("dc.type", str(coll_item_nos_and_audio_genres[row_dict["CollItemNo"]]).replace('[', '').replace(']', '').replace("'", '').replace(',', ';')),
					# E("dc.description.restriction"),
					E("dc.rights.access", "This material is available for research only in the Reading Room of the Bentley Historical Library at the University of Michigan (Ann Arbor, MI)."),
					E("dc.rights.copyright", "This recording may be protected by copyright law. Every audio, visual, or textual work has copyright protection unless that protection has expired over time or its creator has placed it in the public domain. It is the responsibility of anyone interested in reproducing, broadcasting or publishing content from the Bentley Historical Library collections to determine copyright holders and secure permissions accordingly."),
					E("dc.date.open", "2015"),
					E("dc.description", "Content note: The sound recording(s) associated with this repository item derive from a single audio reel tape. A single tape may yield multiple audio files if there were variations in tape stock, speed, or channels (i.e., stereo or mono). For more information see: http://deepblue.lib.umich.edu/handle/2027.42/108126.")
					)

				# this goes through each digital file associated with a collection item
				for dig_file_calc in coll_item_nos_and_dig_file_calcs[row_dict["CollItemNo"]]:

					# parsing digital file calculations to get descriptions, this is fairly inelegant
					if dig_file_calc.split('-')[0] in programs:
						if len(dig_file_calc.split('-')) == 6:
							description = "[Program " + dig_file_calc.split('-')[3] + "] : [Part " + dig_file_calc.split('-')[4] + "] : [Segment " + dig_file_calc.split('-')[5] + "]"
						elif len(dig_file_calc.split('-')) == 5:
							description = "[Program " + dig_file_calc.split('-')[3] + "] : [Part " + dig_file_calc.split('-')[4] + "]"
					else:
						if len(dig_file_calc.split('-')) == 5:
							description = "[Part " + dig_file_calc.split('-')[3] + "] : [Segment " + dig_file_calc.split('-')[4] + "]"
						elif len(dig_file_calc.split('-')) == 4:
							description = "[Part " + dig_file_calc.split('-')[3] + "]"

					# making abstract and appending it
					abstract = description + " : " + row_dict["NoteContent"]
					audio_item.append(E("dc.abstract", abstract))

					# appending bitstreams
					# archival master
					audio_item.append(
						E.bitstream(
							E("dc.title.filename", dig_file_calc + "-am.wav"),
							E("dc.description.filename", description),
							E("dc.format.mimetype", "audio/wav")
						)
					)

					# production master
					audio_item.append(
						E.bitstream(
							E("dc.title.filename", dig_file_calc + "-pm.wav"),
							E("dc.description.filename", description),
							E("dc.format.mimetype", "audio/wav")
						)
					)

					# access
					audio_item.append(
						E.bitstream(
							E("dc.title.filename", dig_file_calc + ".mp3"),
							E("dc.description.filename", description),
							E("dc.format.mimetype", "audio/mpeg3")
						)
					)

				# notes
				audio_item.append(
					E.bitstream(
						E("dc.title.filename", dig_file_calc + ".txt"),
						E("dc.description.filename", "Item Notes"),
						E("dc.format.mimetype", "text/plain")
					)
				)

				# mets
				audio_item.append(
					E.bitstream(
						E("dc.title.filename", dig_file_calc + ".xml"),
						E("dc.description.filename", "METS XML"),
						E("dc.format.mimetype", "text/xml")
					)
				)

				# jpegs
				# goes through each jpeg associated with folders on the nas box
				if coll_item_nos_and_jpegs[row_dict["CollItemNo"] + '-1']:
					for jpeg in (coll_item_nos_and_jpegs[row_dict["CollItemNo"] + '-1']):
						audio_item.append(
							E.bitstream(
								E("dc.title.filename", jpeg),
								E("dc.description.filename", "Item Photo"),
								E("dc.format.mimetype", "image/jpeg")
							)
						)

			
				# for now, dumping these
				with open(join('deep-blue-xml', row_dict["DigFile Calc"] + '.xml'), 'w') as xml_file:
					xml_file.write(ET.tostring(audio_item, encoding='utf-8', pretty_print=True))

# and, keeping up with errors
except:
 	errors.append(row_dict["DigFile Calc"])

print 'errors'
for i in errors:
	print i
print 'jpeg errors'
for i in jpeg_errors:
	print i
