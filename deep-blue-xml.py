import lxml.etree as ET
from lxml.builder import E
import csv

errors = []

try:
	with open(r'C:\Users\Public\Documents\audioDigitalPreservationItemView\audioDigitalPreservationItemView.mer') as csv_file:
		reader = csv.DictReader(csv_file)
		for row_dict in reader:
			if row_dict["CollItemNo"]:
				audio_item = E.audio_item(
					E("dc.identifier.other", row_dict["DigFile Calc"]),
					E("dc.title", "Sound Recording - " + row_dict["ItemTitle"].replace('\x00','')),
					E("dc.contributor.author", row_dict["CollectionCreator"]),
					E("dc.date.issued", "2015"),
					E("dc.date.created", row_dict["Files_Return_Date"][-4:]),
					E("dc.coverage.temporal", row_dict["ItemDate"]),
					E("dc.type", row_dict["Audio_Genre"]), # need to account for other rows
					E("dc.description.restriction"),
					E("dc.rights.access", "This material is available for research only in the Reading Room of the Bentley Historical Library at the University of Michigan (Ann Arbor, MI)."),
					E("dc.rights.copyright", "This recording may be protected by copyright law. Every audio, visual, or textual work has copyright protection unless that protection has expired over time or its creator has placed it in the public domain. It is the responsibility of anyone interested in reproducing, broadcasting or publishing content from the Bentley Historical Library collections to determine copyright holders and secure permissions accordingly."),
					E("dc.date.open", "2015"),
					E("dc.description", "Content note: The sound recording(s) associated with this repository item derive from a single audio reel tape. A single tape may yield multiple audio files if there were variations in tape stock, speed, or channels (i.e., stereo or mono). For more information see: http://deepblue.lib.umich.edu/handle/2027.42/108126."),
					E("dc.abstract", row_dict["NoteContent"]), # need info in []s
					E("bitstream",
						E("dc.title.filename"),
						E("dc.description.filename"),
						E("dc.format.mimetype"),
						)
					)
				ET.dump(audio_item)
except:
	errors.append(row_dict["CollItemNo"])
	errors.append(row_dict["ItemTitle"])

print 'errors'
for i in errors:
		print i