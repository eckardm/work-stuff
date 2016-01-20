import pickle
from lxml import etree
from operator import itemgetter

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

# build out umich presidency series
umich_presidency_c02 = etree.SubElement(digital_docs_c01, "c02")
umich_presidency_c02.attrib["level"] = "series"
umich_presidency_did = etree.SubElement(umich_presidency_c02, "did")
umich_presidency_unittitle = etree.SubElement(umich_presidency_did, "unittitle")
umich_presidency_unittitle.text = "University of Michigan Presidency" + ", "
umich_presidency_unitdate = etree.SubElement(umich_presidency_unittitle, "unitdate")
umich_presidency_unitdate.text = "1986-1997"
umich_presidency_unitdate.attrib["type"] = "inclusive"
umich_presidency_unitdate.attrib["normal"] = "1986/1997"
umich_presidency_scopecontent = etree.SubElement(umich_presidency_c02, "scopecontent")
umich_presidency_scopecontent_p = etree.SubElement(umich_presidency_scopecontent, "p")
umich_presidency_scopecontent_p.text = "Digital documents from Duderstadt's tenure as University President."

# build out speeches series
# populate speeches series
# build out idea files series
# populate idea files series
# build out strategy series
# populate strategy series
# build out position papers series
# populate position papers series
# build out presentations series
# populate presentations series
# build out write files series
# populate write files series
# build out legacy series
# populate legacy series
# build out digital images series
# populate digital images series

# build out faculty archives series
faculty_archives_c02 = etree.SubElement(digital_docs_c01, "c02")
faculty_archives_c02.attrib["level"] = "series"
faculty_archives_did = etree.SubElement(faculty_archives_c02, "did")
faculty_archives_unittitle = etree.SubElement(faculty_archives_did, "unittitle")
faculty_archives_unittitle.text = "Faculty Archives" + ", "
faculty_archives_unitdate = etree.SubElement(faculty_archives_unittitle, "unitdate")
faculty_archives_unitdate.text = "1968-ongoing"
faculty_archives_unitdate.attrib["type"] = "inclusive"
faculty_archives_unitdate.attrib["normal"] = "1968/9999"
faculty_archives_scopecontent = etree.SubElement(faculty_archives_c02, "scopecontent")
faculty_archives_scopecontent_p = etree.SubElement(faculty_archives_scopecontent, "p")
faculty_archives_scopecontent_p.text = "Includes speeches, presentations, writings and images. Portions of the collection are restricted. This collection represents the 'personal papers' of president Duderstadt."

'''
<c02 level="file">
  <did>
    <physloc>Online</physloc>
    <unittitle>Camp Shelby (basic training and MP training), <unitdate type="inclusive" normal="2011/2012">2011-2012</unitdate></unittitle>
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

# populate faculty archives series
sorted_metadata = sorted(metadata, key=itemgetter("unitdate"), reverse=False)

for sorted_metadatum in sorted_metadata:
    
    print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
    
    sorted_metadatum_c03 = etree.SubElement(faculty_archives_c02, "c03")
    sorted_metadatum_c03.attrib["level"] = "file"
    sorted_metadatum_did = etree.SubElement(sorted_metadatum_c03, "did")
    sorted_metadatum_physloc = etree.SubElement(sorted_metadatum_did, "physloc")
    sorted_metadatum_physloc.text = "Online"
    sorted_metadatum_unittitle = etree.SubElement(sorted_metadatum_did, "unittitle")
    sorted_metadatum_unittitle.text = sorted_metadatum["unittitle"].decode("utf-8") + ", "
    sorted_metadatum_unitdate = etree.SubElement(sorted_metadatum_unittitle, "unitdate")
    sorted_metadatum_unitdate.text = sorted_metadatum["unitdate"]
    sorted_metadatum_unitdate.attrib["type"] = "inclusive"
    sorted_metadatum_unitdate.attrib["normal"] = sorted_metadatum["unitdate"]   
    sorted_metadatum_physdesc = etree.SubElement(sorted_metadatum_did, "physdesc")
    sorted_metadatum_physfacet = etree.SubElement(sorted_metadatum_physdesc, "physfacet")
    sorted_metadatum_physfacet.text = sorted_metadatum["physfacet"]
    sorted_metadatum_dao = etree.SubElement(sorted_metadatum_did, "dao")
    sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
    sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
    sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
    sorted_metadatum_daodesc_p.text = "[view item]"
    if "accessrestrict" in sorted_metadatum:
        sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
        sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
        sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]
    
with open("duderst-updated.xml", mode="w") as ead_out:
    ead_out.write(etree.tostring(digital_docs_c01, pretty_print=True, encoding="utf-8", xml_declaration=True))
