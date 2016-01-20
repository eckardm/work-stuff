import pickle
from lxml import etree

'''
<c02 level="file">
  <did>
    <physloc>Online</physloc>
    <unittitle>Camp Shelby (basic training and MP training)</unittitle>
    <unitdate type="inclusive" normal="2011/2012">2011-2012</unitdate>
    <physdesc>
      <physfacet>.ZIP file</physfacet>
    </physdesc>
    <dao href="http://hdl.handle.net/2027.42/101933" show="new" actuate="onrequest">
      <daodesc>
        <p>[view item]</p>
      </daodesc>
    </dao>
  </did>
  <accessrestrict>
    <p>[SR RESTRICTED until July 1 <date type="restriction" normal="2056-07-01">2056</date>]</p>
  </accessrestrict>
</c02>'''

'''
Digital Documents - University of Michigan Presidency, 1986-1997 - Speeches - 1989-1990 Speeches - Alumni 5.0'''

metadata = pickle.load(open("metadata.p", mode="rb"))

# build out digital docs subgroup
digital_docs_c01 = etree.Element("c01")
digital_docs_c01.attrib["level"] = "subgrp"
digital_docs_did = etree.SubElement(digital_docs_c01, "did")
digital_docs_unittitle = etree.SubElement(digital_docs_did, "unittitle")
digital_docs_unittitle.text = "Digital Documents"
digital_docs_physdesc = etree.SubElement(digital_docs_did, "physdesc")
digital_docs_physdesc.attrib["altrender"] = "whole"
digital_docs_extent = etree.SubElement(digital_docs_physdesc, "extent")
digital_docs_extent.attrib["altrender"] = "materialtype spaceoccupied"
digital_docs_extent.text = "5397 digital files"
digital_docs_physfacet = etree.SubElement(digital_docs_physdesc, "physfacet")
digital_docs_physfacet.text = "393 MB"
digital_docs_scopecontent = etree.SubElement(digital_docs_c01, "scopecontent")
digital_docs_p1 = etree.SubElement(digital_docs_scopecontent, "p")
digital_docs_p1.text = "There are 5397 digital files (393 MB) in the Digital Documents subgroup. At the time of the records accession to the Bentley Historical Library, the Macintosh operating system version 8.0 was in use. The original organization and arrangement of Duderstadt's digital files has been preserved. Duderstadt maintained seven archival directories: Speeches, Idea Files, Strategy, Position Papers, Presentations, Write Files, and Legacy. An additional series, Digital Images, was created when a collection of digital images of university building projects was accessioned to the collection early in 1998."
digital_docs_p2 = etree.SubElement(digital_docs_scopecontent, "p")
digital_docs_p2.text = "The arrangement of files within each directory is chronological by date starting with the 1986-1987 school year. This arrangement was designed and used by Duderstadt in the Speeches, Idea Files, and Write Files series and extended to the remaining series except the Digital Images during the processing phase of the project. The directory naming scheme effectively describes the type of record contained within the directory. File names are also in most cases descriptive of the content, however, researchers should note that Duderstadt used personal last names, initials, abbreviations, and numerous acronyms in naming files. A list of commonly used acronyms and abbreviations used for file naming purposes can be found in the 'Additional Descriptive Data' section of the finding aid. Researcher's Note: The file-naming scheme also reveals the specific version of a particular document. Duderstadt maintained the file name for the record and added a sequence of numbers to the file name to indicate various versions. For example, the record 'Project Athena' progresses from Project Athena .92, Project Athena 1.0, 1.01, 1.2, 2.1, to Project Athena 2.21."

with open("duderst-updated.xml", mode="w") as ead_out:
    ead_out.write(etree.tostring(digital_docs_c01, pretty_print=True, encoding="utf-8", xml_declaration=True))
