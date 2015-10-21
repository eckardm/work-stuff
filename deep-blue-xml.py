import lxml.etree as ET
from lxml.builder import E
import csv

with open(r'C:\Users\Public\Documents\audioDigitalPreservationItemView\audioDigitalPreservationItemView.mer') as csv_file:
	reader = csv.DictReader(csv_file)
	for row_dict in reader:
		if row_dict["CollItemNo"]:

			audio_item = E.audio_item(
				E("dc.identifier.other", row_dict["DigFile Calc"]),
				E("dc.title", "Sound Recording - " + row_dict["ItemTitle"].decode("utf-8", "ignore")),
				E("dc.contributor.author"),
				E("dc.date.issued"),
				E("dc.date.created"),
				E("dc.coverage.temporal"),
				E("dc.type"),
				E("dc.description.restriction"),
				E("dc.rights.access", "This material is available for research only in the Reading Room of the Bentley Historical Library at the University of Michigan (Ann Arbor, MI)."),
				E("dc.rights.copyright", "This recording may be protected by copyright law. Every audio, visual, or textual work has copyright protection unless that protection has expired over time or its creator has placed it in the public domain. It is the responsibility of anyone interested in reproducing, broadcasting or publishing content from the Bentley Historical Library collections to determine copyright holders and secure permissions accordingly."),
				E("dc.date.open"),
				E("dc.description", "Content note: The sound recording(s) associated with this repository item derive from a single audio reel tape. A single tape may yield multiple audio files if there were variations in tape stock, speed, or channels (i.e., stereo or mono). For more information see: http://deepblue.lib.umich.edu/handle/2027.42/108126."),
				E("dc.abstract"),
				E("bitstream",
					E("dc.title.filename"),
					E("dc.description.filename"),
					E("dc.format.mimetype"),
					)
				)
			ET.dump(audio_item)


'''
for bitstream in sdfkljsd:
				audio_item.append(
					E(""))
Access_MP3_file, AudioPlayBackID, AV_Audio, AvItemID, AvTypeId, BhlBox, cassfilename, CatalogDate, CollectionID, CollItemNo, DigFile Calc, DigitalFile, ItemDate, ItemNo, ItemPart, ItemPart_Segment, ItemPartTitle, ItemQualityCheckNote, ItemQualityCheckSatus, ItemTitle, Master_WAV_file, MasterProd_WAV_file, MiVideoID, NoteContent, NoteInline, NoteTechnical, OriginItemNo, ProgramNo, ProgramTitle, QA_Technician, RevDate, SpellingNote, DateDigitized, digitize _status, Files_Return_Date, Orig_Return_Date, OrigBoxNo, Photographed, QC_Ccomplete_Date, ShippingBoxNo, ShippingDate, Audio_GenreID, Audio_Genre, Audio_Subject, Condition, Fidleity, ItemSourceLength, ReelSize, TapeSpeed, MP3_File_bitdepth, MP3_File_Date, MP3_File_Duration, MP3_File_Size_bytes, MP3_File_Temp_Loc, AudioSubjectID, Audio_WAVP_File_bitdepth, Audio_WAVP_File_Date, Audio_WAVP_File_Duration, Audio_WAVP_File_Size_bytes, Audio_WAVP_File_Size_mb, Audio_WAVP_Temp_Loc, WAV_File_bitdepth, WAV_File_Date, WAV_File_Duration, WAV_File_Size_bytes, WAV_File_Size_mb, WAV_Temp_Loc, AV_BrandID, AudioPresStatus, AvPresStatus, CollectionCreator, CollectionID, CollectionTitle, DeepBlueCollectionID, Vendor_Name'''