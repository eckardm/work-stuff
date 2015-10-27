import lxml.etree as ET
from lxml.builder import E
import csv

from coll_item_nos_and_dig_file_calcs import coll_item_nos_and_dig_file_calcs

programs = ['8730', '90139', '87334', '87250', '8738']

errors = []

try:
	with open(r'C:\Users\Public\Documents\audioDigitalPreservationItemView\audioDigitalPreservationItemView.mer') as csv_file:
		reader = csv.DictReader(csv_file)
		for row_dict in reader:
			if row_dict["CollItemNo"]:
				audio_item = E.audio_item(
					E("dc.identifier.other", row_dict["CollItemNo"]),
					E("dc.title", "Sound Recording - " + row_dict["ItemTitle"]),
					E("dc.contributor.author", row_dict["CollectionCreator"]),
					E("dc.date.issued", "2015"),
					E("dc.date.created", row_dict["Files_Return_Date"][-4:]),
					E("dc.coverage.temporal", row_dict["ItemDate"]),
					E("dc.type", row_dict["Audio_Genre"]), # need to account for other rows
					# E("dc.description.restriction"),
					E("dc.rights.access", "This material is available for research only in the Reading Room of the Bentley Historical Library at the University of Michigan (Ann Arbor, MI)."),
					E("dc.rights.copyright", "This recording may be protected by copyright law. Every audio, visual, or textual work has copyright protection unless that protection has expired over time or its creator has placed it in the public domain. It is the responsibility of anyone interested in reproducing, broadcasting or publishing content from the Bentley Historical Library collections to determine copyright holders and secure permissions accordingly."),
					E("dc.date.open", "2015"),
					E("dc.description", "Content note: The sound recording(s) associated with this repository item derive from a single audio reel tape. A single tape may yield multiple audio files if there were variations in tape stock, speed, or channels (i.e., stereo or mono). For more information see: http://deepblue.lib.umich.edu/handle/2027.42/108126.")
					)

				for dig_file_calc in coll_item_nos_and_dig_file_calcs[row_dict["CollItemNo"]]:
					digital_file_components = dig_file_calc.split('-')
					if dig_file_calc.split('-')[0] in programs:
						if len(digital_file_components) == 6:
							description = "[Program " + dig_file_calc.split('-')[3] + "] : [Part " + dig_file_calc.split('-')[4] + "] : [Segment " + dig_file_calc.split('-')[5] + "]"
						elif len(digital_file_components) == 5:
							description = "[Program " + dig_file_calc.split('-')[3] + "] : [Part " + dig_file_calc.split('-')[4] + "]"
					else:
						if len(digital_file_components) == 5:
							description = "[Part " + dig_file_calc.split('-')[3] + "] : [Segment " + dig_file_calc.split('-')[4] + "]"
						elif len(digital_file_components) == 4:
							description = "[Part " + dig_file_calc.split('-')[3] + "] : "
					abstract = description + " : " + row_dict["NoteContent"]
					audio_item.append(E("dc.abstract", abstract))

					audio_item.append(
						E.bitstream(
							E("dc.title.filename", dig_file_calc + "-am.wav"),
							E("dc.description.filename", description),
							E("dc.format.mimetype", "audio/wav")
						)
					)
					audio_item.append(
						E.bitstream(
							E("dc.title.filename", dig_file_calc + "-pm.wav"),
							E("dc.description.filename", description),
							E("dc.format.mimetype", "audio/wav")
						)
					)
					audio_item.append(
						E.bitstream(
							E("dc.title.filename", dig_file_calc + ".mp3"),
							E("dc.description.filename", description),
							E("dc.format.mimetype", "audio/mpeg3")
						)
					)

			
			ET.dump(audio_item)

except:
 	errors.append(row_dict["DigFile Calc"])

print 'errors'
for i in errors:
		print i