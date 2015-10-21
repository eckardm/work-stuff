import lxml.etree as ET
from lxml.builder import E
import csv

with open(r'C:\Users\Public\Documents\audioDigitalPreservationItemView\audioDigitalPreservationItemView.mer') as csv_file:
	reader = csv.DictReader(csv_file)
	for row_dict in reader:

			audio_item = ET.Element('audio_item')
			dc_identifier_other = ET.SubElement(audio_item, 'dc.identifier.other')
			dc_identifier_other.text = row_dict["CollItemNo"]
			dc_title = ET.SubElement(audio_item, 'dc.title')
			dc_contributor_author = ET.SubElement(audio_item, 'dc.contributor.author')
			dc_date_issued = ET.SubElement(audio_item, 'dc.date.issued')
			dc_date_created = ET.SubElement(audio_item, 'dc.date.created')
			dc_coverage_temporal = ET.SubElement(audio_item, 'dc.coverage.temporal')
			dc_type = ET.SubElement(audio_item, 'dc.type')
			dc_description_restriction = ET.SubElement(audio_item, 'dc.description.restriction')
			dc_rights_access = ET.SubElement(audio_item, 'dc.rights.access')
			dc_rights_access.text = "This material is available for research only in the Reading Room of the Bentley Historical Library at the University of Michigan (Ann Arbor, MI)."
			dc_rights_copyright = ET.SubElement(audio_item, 'dc.rights.copyright')
			dc_rights_copyright.text = "This recording may be protected by copyright law. Every audio, visual, or textual work has copyright protection unless that protection has expired over time or its creator has placed it in the public domain. It is the responsibility of anyone interested in reproducing, broadcasting or publishing content from the Bentley Historical Library collections to determine copyright holders and secure permissions accordingly."
			dc_date_open = ET.SubElement(audio_item, 'dc.date.open')
			dc_description = ET.SubElement(audio_item, 'dc.description')
			dc_description.text = "Content note: The sound recording(s) associated with this repository item derive from a single audio reel tape. A single tape may yield multiple audio files if there were variations in tape stock, speed, or channels (i.e., stereo or mono). For more information see: http://deepblue.lib.umich.edu/handle/2027.42/108126."
			dc_abstract = ET.SubElement(audio_item, 'dc.abstract') # repeatable

			bitstream = ET.SubElement(audio_item, 'bitstream')

			dc_title_filename = ET.SubElement(bitstream, 'dc.title.filename')
			dc_description_filename = ET.SubElement(bitstream, 'dc.description.filename')
			dc_format_mimetype = ET.SubElement(bitstream, 'dc.format.mimetype')

			ET.dump(audio_item)


'''
Access_MP3_file, AudioPlayBackID, AV_Audio, AvItemID, AvTypeId, BhlBox, cassfilename, CatalogDate, CollectionID, CollItemNo, DigFile Calc, DigitalFile, ItemDate, ItemNo, ItemPart, ItemPart_Segment, ItemPartTitle, ItemQualityCheckNote, ItemQualityCheckSatus, ItemTitle, Master_WAV_file, MasterProd_WAV_file, MiVideoID, NoteContent, NoteInline, NoteTechnical, OriginItemNo, ProgramNo, ProgramTitle, QA_Technician, RevDate, SpellingNote, DateDigitized, digitize _status, Files_Return_Date, Orig_Return_Date, OrigBoxNo, Photographed, QC_Ccomplete_Date, ShippingBoxNo, ShippingDate, Audio_GenreID, Audio_Genre, Audio_Subject, Condition, Fidleity, ItemSourceLength, ReelSize, TapeSpeed, MP3_File_bitdepth, MP3_File_Date, MP3_File_Duration, MP3_File_Size_bytes, MP3_File_Temp_Loc, AudioSubjectID, Audio_WAVP_File_bitdepth, Audio_WAVP_File_Date, Audio_WAVP_File_Duration, Audio_WAVP_File_Size_bytes, Audio_WAVP_File_Size_mb, Audio_WAVP_Temp_Loc, WAV_File_bitdepth, WAV_File_Date, WAV_File_Duration, WAV_File_Size_bytes, WAV_File_Size_mb, WAV_Temp_Loc, AV_BrandID, AudioPresStatus, AvPresStatus, CollectionCreator, CollectionID, CollectionTitle, DeepBlueCollectionID, Vendor_Name'''