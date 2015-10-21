import xml.etree.ElementTree as ET

audio_item = ET.Element('audio_item')

dc_identifier_other = ET.SubElement(audio_item, 'dc.identifier.other')
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
