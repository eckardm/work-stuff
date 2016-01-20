import pickle
from lxml import etree
from operator import itemgetter

'''
Digital Documents - University of Michigan Presidency, 1986-1997 - Speeches - 1989-1990 Speeches - Alumni 5.0'''

metadata = pickle.load(open("metadata.p", mode="rb"))
sorted_metadata = sorted(metadata, key=itemgetter("unitdate"), reverse=False)

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
digital_docs_extent.text = "5397 digital files" # <-- will need to be updated
digital_docs_physfacet = etree.SubElement(digital_docs_physdesc, "physfacet")
digital_docs_physfacet.text = "393 MB" # <-- will need to be updated
digital_docs_scopecontent = etree.SubElement(digital_docs_c01, "scopecontent")
digital_docs_p1 = etree.SubElement(digital_docs_scopecontent, "p")
digital_docs_p1.text = "There are 5397 digital files (393 MB) in the Digital Documents subgroup. At the time of the records accession to the Bentley Historical Library, the Macintosh operating system version 8.0 was in use. The original organization and arrangement of Duderstadt's digital files has been preserved. Duderstadt maintained seven archival directories: Speeches, Idea Files, Strategy, Position Papers, Presentations, Write Files, and Legacy. An additional series, Digital Images, was created when a collection of digital images of university building projects was accessioned to the collection early in 1998." # <-- will need to be updated
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
speeches_c03 = etree.SubElement(umich_presidency_c02, "c03")
speeches_c03.attrib["level"] = "series"
speeches_did = etree.SubElement(speeches_c03, "did")
speeches_unittitle = etree.SubElement(speeches_did, "unittitle")
speeches_unittitle.text = "Speeches" + ", "
speeches_unitdate = etree.SubElement(speeches_unittitle, "unitdate")
speeches_unitdate.text = "1986-1996"
speeches_unitdate.attrib["type"] = "inclusive"
speeches_unitdate.attrib["normal"] = "1986/1996"
speeches_physdesc = etree.SubElement(speeches_did, "physdesc")
speeches_physdesc.attrib["altrender"] = "whole"
speeches_extent = etree.SubElement(speeches_physdesc, "extent")
speeches_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_extent.text = "821 digital files" # <-- will need to be updated
speeches_scopecontent = etree.SubElement(speeches_c03, "scopecontent")
speeches_scopecontent_p1 = etree.SubElement(speeches_scopecontent, "p")
speeches_scopecontent_p1.text = "A main avenue President Duderstadt utilized as a means to communicate his ideas, objectives, and university strategic plan was to get out into the community and talk. During his presidency, Duderstadt frequently made several speeches a day to groups on campus and across the state, thus making the Speeches series (821 files, 1986-1996) the largest series in the Digital Documents subgroup. The early speech files from the years 1986 to 1992 were predominately composed using the MORE 3.1 outline program. However, after 1992 he drafted his speeches using a combination of MORE 3.1 and Microsoft Word 6.0. Major Speeches contained in this series include: The Cranbrook Address, The Challenge of K-12 Education, February, 1990, American Nuclear Society Keynote Address, A Future of Change, April, 1992, State Equity in Education Conference, The Michigan Mandate: A Progress Report, March, 1993, Vision 2017: The Third Century, November, 1993." # <-- will need to be updated
speeches_scopecontent_p2 = etree.SubElement(speeches_scopecontent, "p")
speeches_scopecontent_p2.text = "Researchers should note that a list of key speeches by title, year, and location can be found in the digital file titled 'Accomplishments' located in the Strategy series. Also, note that several iterations of particular speeches can be found in the Digital Documents subgroup. Duderstadt's file naming scheme reflects the change in a file by a series of numbers located after the file name."

# build out 1986-1987 speeches subseries
speeches_86_87_c04 = etree.SubElement(speeches_c03, "c04")
speeches_86_87_c04.attrib["level"] = "subseries"
speeches_86_87_did = etree.SubElement(speeches_86_87_c04, "did")
speeches_86_87_physloc = etree.SubElement(speeches_86_87_did, "physloc")
speeches_86_87_physloc.text = "Online"
speeches_86_87_unittitle = etree.SubElement(speeches_86_87_did, "unittitle")
speeches_86_87_unittitle.text = "1986-1987 Speeches"
speeches_86_87_physdesc = etree.SubElement(speeches_86_87_did, "physdesc")
speeches_86_87_physdesc.attrib["altrender"] = "whole"
speeches_86_87_extent = etree.SubElement(speeches_86_87_physdesc, "extent")
speeches_86_87_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_86_87_extent.text = "37 digital files" # <-- will need to be updated

# populate 1986-1987 speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1986-1987 Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(speeches_86_87_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1987-1988 speeches subseries
speeches_87_88_c04 = etree.SubElement(speeches_c03, "c04")
speeches_87_88_c04.attrib["level"] = "subseries"
speeches_87_88_did = etree.SubElement(speeches_87_88_c04, "did")
speeches_87_88_physloc = etree.SubElement(speeches_87_88_did, "physloc")
speeches_87_88_physloc.text = "Online"
speeches_87_88_unittitle = etree.SubElement(speeches_87_88_did, "unittitle")
speeches_87_88_unittitle.text = "1987-1988 Speeches"
speeches_87_88_physdesc = etree.SubElement(speeches_87_88_did, "physdesc")
speeches_87_88_physdesc.attrib["altrender"] = "whole"
speeches_87_88_extent = etree.SubElement(speeches_87_88_physdesc, "extent")
speeches_87_88_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_87_88_extent.text = "54 digital files" # <-- will need to be updated

# populate 1987-1988 speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1987-1988 Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(speeches_88_88_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1988-1989 speeches subseries
speeches_88_89_c04 = etree.SubElement(speeches_c03, "c04")
speeches_88_89_c04.attrib["level"] = "subseries"
speeches_88_89_did = etree.SubElement(speeches_88_89_c04, "did")
speeches_88_89_physloc = etree.SubElement(speeches_88_89_did, "physloc")
speeches_88_89_physloc.text = "Online"
speeches_88_89_unittitle = etree.SubElement(speeches_88_89_did, "unittitle")
speeches_88_89_unittitle.text = "1988-1989 Speeches"
speeches_88_89_physdesc = etree.SubElement(speeches_88_89_did, "physdesc")
speeches_88_89_physdesc.attrib["altrender"] = "whole"
speeches_88_89_extent = etree.SubElement(speeches_88_89_physdesc, "extent")
speeches_88_89_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_88_89_extent.text = "124 digital files" # <-- will need to be updated

# populate 1988-1989 speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1988-1989 Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(speeches_88_89_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1989-1990 speeches subseries
speeches_89_90_c04 = etree.SubElement(speeches_c03, "c04")
speeches_89_90_c04.attrib["level"] = "subseries"
speeches_89_90_did = etree.SubElement(speeches_89_90_c04, "did")
speeches_89_90_physloc = etree.SubElement(speeches_89_90_did, "physloc")
speeches_89_90_physloc.text = "Online"
speeches_89_90_unittitle = etree.SubElement(speeches_89_90_did, "unittitle")
speeches_89_90_unittitle.text = "1989-1990 Speeches"
speeches_89_90_physdesc = etree.SubElement(speeches_89_90_did, "physdesc")
speeches_89_90_physdesc.attrib["altrender"] = "whole"
speeches_89_90_extent = etree.SubElement(speeches_89_90_physdesc, "extent")
speeches_89_90_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_89_90_extent.text = "132 digital files" # <-- will need to be updated

# populate 1989-1990 speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1989-1990 Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(speeches_89_90_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1990-1991 speeches subseries
speeches_90_91_c04 = etree.SubElement(speeches_c03, "c04")
speeches_90_91_c04.attrib["level"] = "subseries"
speeches_90_91_did = etree.SubElement(speeches_90_91_c04, "did")
speeches_90_91_physloc = etree.SubElement(speeches_90_91_did, "physloc")
speeches_90_91_physloc.text = "Online"
speeches_90_91_unittitle = etree.SubElement(speeches_90_91_did, "unittitle")
speeches_90_91_unittitle.text = "1990-1991 Speeches"
speeches_90_91_physdesc = etree.SubElement(speeches_90_91_did, "physdesc")
speeches_90_91_physdesc.attrib["altrender"] = "whole"
speeches_90_91_extent = etree.SubElement(speeches_90_91_physdesc, "extent")
speeches_90_91_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_90_91_extent.text = "214 digital files" # <-- will need to be updated

# populate 1990-1991 speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1990-1991 Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(speeches_90_91_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1991-1992 speeches subseries
speeches_91_92_c04 = etree.SubElement(speeches_c03, "c04")
speeches_91_92_c04.attrib["level"] = "subseries"
speeches_91_92_did = etree.SubElement(speeches_91_92_c04, "did")
speeches_91_92_physloc = etree.SubElement(speeches_91_92_did, "physloc")
speeches_91_92_physloc.text = "Online"
speeches_91_92_unittitle = etree.SubElement(speeches_91_92_did, "unittitle")
speeches_91_92_unittitle.text = "1991-1992 Speeches"
speeches_91_92_physdesc = etree.SubElement(speeches_91_92_did, "physdesc")
speeches_91_92_physdesc.attrib["altrender"] = "whole"
speeches_91_92_extent = etree.SubElement(speeches_91_92_physdesc, "extent")
speeches_91_92_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_91_92_extent.text = "52 digital files" # <-- will need to be updated

# populate 1991-1992 speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1991-1992 Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(speeches_91_92_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1992-1993 speeches subseries
speeches_92_93_c04 = etree.SubElement(speeches_c03, "c04")
speeches_92_93_c04.attrib["level"] = "subseries"
speeches_92_93_did = etree.SubElement(speeches_92_93_c04, "did")
speeches_92_93_physloc = etree.SubElement(speeches_92_93_did, "physloc")
speeches_92_93_physloc.text = "Online"
speeches_92_93_unittitle = etree.SubElement(speeches_92_93_did, "unittitle")
speeches_92_93_unittitle.text = "1992-1993 Speeches"
speeches_92_93_physdesc = etree.SubElement(speeches_92_93_did, "physdesc")
speeches_92_93_physdesc.attrib["altrender"] = "whole"
speeches_92_93_extent = etree.SubElement(speeches_92_93_physdesc, "extent")
speeches_92_93_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_92_93_extent.text = "36 digital files" # <-- will need to be updated

# populate 1992-1993 speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1992-1993 Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(speeches_92_93_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1994-1995 speeches subseries
speeches_94_95_c04 = etree.SubElement(speeches_c03, "c04")
speeches_94_95_c04.attrib["level"] = "subseries"
speeches_94_95_did = etree.SubElement(speeches_94_95_c04, "did")
speeches_94_95_physloc = etree.SubElement(speeches_94_95_did, "physloc")
speeches_94_95_physloc.text = "Online"
speeches_94_95_unittitle = etree.SubElement(speeches_94_95_did, "unittitle")
speeches_94_95_unittitle.text = "1994-1995 Speeches"
speeches_94_95_physdesc = etree.SubElement(speeches_94_95_did, "physdesc")
speeches_94_95_physdesc.attrib["altrender"] = "whole"
speeches_94_95_extent = etree.SubElement(speeches_94_95_physdesc, "extent")
speeches_94_95_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_94_95_extent.text = "27 digital files" # <-- will need to be updated

# populate 1994-1995 speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1994-1995 Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(speeches_94_95_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1995-1996 speeches subseries
speeches_95_96_c04 = etree.SubElement(speeches_c03, "c04")
speeches_95_96_c04.attrib["level"] = "subseries"
speeches_95_96_did = etree.SubElement(speeches_95_96_c04, "did")
speeches_95_96_physloc = etree.SubElement(speeches_95_96_did, "physloc")
speeches_95_96_physloc.text = "Online"
speeches_95_96_unittitle = etree.SubElement(speeches_95_96_did, "unittitle")
speeches_95_96_unittitle.text = "1995-1996 Speeches"
speeches_95_96_physdesc = etree.SubElement(speeches_95_96_did, "physdesc")
speeches_95_96_physdesc.attrib["altrender"] = "whole"
speeches_95_96_extent = etree.SubElement(speeches_95_96_physdesc, "extent")
speeches_95_96_extent.attrib["altrender"] = "materialtype spaceoccupied"
speeches_95_96_extent.text = "135 digital files" # <-- will need to be updated

# populate 1995-1996 speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1995-1996 Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(speeches_95_96_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out athletic talks-speeches subseries
athletic_talks_c04 = etree.SubElement(speeches_c03, "c04")
athletic_talks_c04.attrib["level"] = "subseries"
athletic_talks_did = etree.SubElement(athletic_talks_c04, "did")
athletic_talks_physloc = etree.SubElement(athletic_talks_did, "physloc")
athletic_talks_physloc.text = "Online"
athletic_talks_unittitle = etree.SubElement(athletic_talks_did, "unittitle")
athletic_talks_unittitle.text = "Athletic Talks-Speeches"
athletic_talks_physdesc = etree.SubElement(athletic_talks_did, "physdesc")
athletic_talks_physdesc.attrib["altrender"] = "whole"
athletic_talks_extent = etree.SubElement(athletic_talks_physdesc, "extent")
athletic_talks_extent.attrib["altrender"] = "materialtype spaceoccupied"
athletic_talks_extent.text = "12 digital files" # <-- will need to be updated

# populate athletic talks-speeches subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "Athletic Talks-Speeches"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(athletic_talks_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out idea files series
idea_files_c03 = etree.SubElement(umich_presidency_c02, "c03")
idea_files_c03.attrib["level"] = "series"
idea_files_did = etree.SubElement(idea_files_c03, "did")
idea_files_unittitle = etree.SubElement(idea_files_did, "unittitle")
idea_files_unittitle.text = "Idea Files" + ", "
idea_files_unitdate = etree.SubElement(idea_files_unittitle, "unitdate")
idea_files_unitdate.text = "1986-1995"
idea_files_unitdate.attrib["type"] = "inclusive"
idea_files_unitdate.attrib["normal"] = "1986/1995"
idea_files_physdesc = etree.SubElement(idea_files_did, "physdesc")
idea_files_physdesc.attrib["altrender"] = "whole"
idea_files_extent = etree.SubElement(idea_files_physdesc, "extent")
idea_files_extent.attrib["altrender"] = "materialtype spaceoccupied"
idea_files_extent.text = "328 digital files" # <-- will need to be updated
idea_files_scopecontent = etree.SubElement(idea_files_c03, "scopecontent")
idea_files_scopecontent_p = etree.SubElement(idea_files_scopecontent, "p")
idea_files_scopecontent_p.text = "The Idea Files series (328 digital files, 1986-1995) is comprised of files created with the MORE 3.1 outline program. Many of the outline files in this series resemble a silhouette of ideas that Duderstadt later developed into strategic planning documents, position papers, and speeches. Other outlines in the series read as talking points Duderstadt used either to prepare for a meeting or an important conversation. Major topics addressed in this series include higher education, teaching and research, information technology, and affirmative action. Yearly progress reports on the status of Duderstadt's agenda and goals can be found within this series in files with titles such as 'Summary 1991-92' or 'The Year Past.' Researchers interested in additional biographical material should consult the digital file 'Biography' in the 1988-1989 Ideas subseries and the Biographical series in the Paper Documents subgroup."

# build out 1986-1987 ideas subseries
ideas_86_87_c04 = etree.SubElement(idea_files_c03, "c04")
ideas_86_87_c04.attrib["level"] = "subseries"
ideas_86_87_did = etree.SubElement(ideas_86_87_c04, "did")
ideas_86_87_physloc = etree.SubElement(ideas_86_87_did, "physloc")
ideas_86_87_physloc.text = "Online"
ideas_86_87_unittitle = etree.SubElement(ideas_86_87_did, "unittitle")
ideas_86_87_unittitle.text = "1986-1987 Ideas"
ideas_86_87_physdesc = etree.SubElement(ideas_86_87_did, "physdesc")
ideas_86_87_physdesc.attrib["altrender"] = "whole"
ideas_86_87_extent = etree.SubElement(ideas_86_87_physdesc, "extent")
ideas_86_87_extent.attrib["altrender"] = "materialtype spaceoccupied"
ideas_86_87_extent.text = "36 digital files" # <-- will need to be updated
ideas_86_87_accessrestrict = etree.SubElement(ideas_86_87_c04, "accessrestrict")
ideas_86_87_accessrestrict_p = etree.SubElement(ideas_86_87_accessrestrict, "p")
ideas_86_87_accessrestrict_p.text = "RESTRICTED until "
ideas_86_87_date = etree.SubElement(ideas_86_87_accessrestrict_p, "date")
ideas_86_87_date.attrib["type"] = "restriction"
ideas_86_87_date.attrib["normal"] = "2030-07-01"
ideas_86_87_date.text = "July 1, 2030"

# populate 1986-1987 ideas subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1986-1987 Ideas"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(ideas_86_87_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1987-1988 ideas subseries
ideas_87_88_c04 = etree.SubElement(idea_files_c03, "c04")
ideas_87_88_c04.attrib["level"] = "subseries"
ideas_87_88_did = etree.SubElement(ideas_87_88_c04, "did")
ideas_87_88_physloc = etree.SubElement(ideas_87_88_did, "physloc")
ideas_87_88_physloc.text = "Online"
ideas_87_88_unittitle = etree.SubElement(ideas_87_88_did, "unittitle")
ideas_87_88_unittitle.text = "1987-1988 Ideas"
ideas_87_88_physdesc = etree.SubElement(ideas_87_88_did, "physdesc")
ideas_87_88_physdesc.attrib["altrender"] = "whole"
ideas_87_88_extent = etree.SubElement(ideas_87_88_physdesc, "extent")
ideas_87_88_extent.attrib["altrender"] = "materialtype spaceoccupied"
ideas_87_88_extent.text = "28 digital files" # <-- will need to be updated
ideas_87_88_accessrestrict = etree.SubElement(ideas_87_88_c04, "accessrestrict")
ideas_87_88_accessrestrict_p = etree.SubElement(ideas_87_88_accessrestrict, "p")
ideas_87_88_accessrestrict_p.text = "RESTRICTED until "
ideas_87_88_date = etree.SubElement(ideas_87_88_accessrestrict_p, "date")
ideas_87_88_date.attrib["type"] = "restriction"
ideas_87_88_date.attrib["normal"] = "2030-07-01"
ideas_87_88_date.text = "July 1, 2030"

# populate 1987-1988 ideas subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1987-1988 Ideas"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(ideas_87_88_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1988-1989 ideas subseries
ideas_88_89_c04 = etree.SubElement(idea_files_c03, "c04")
ideas_88_89_c04.attrib["level"] = "subseries"
ideas_88_89_did = etree.SubElement(ideas_88_89_c04, "did")
ideas_88_89_physloc = etree.SubElement(ideas_88_89_did, "physloc")
ideas_88_89_physloc.text = "Online"
ideas_88_89_unittitle = etree.SubElement(ideas_88_89_did, "unittitle")
ideas_88_89_unittitle.text = "1988-1989 Ideas"
ideas_88_89_physdesc = etree.SubElement(ideas_88_89_did, "physdesc")
ideas_88_89_physdesc.attrib["altrender"] = "whole"
ideas_88_89_extent = etree.SubElement(ideas_88_89_physdesc, "extent")
ideas_88_89_extent.attrib["altrender"] = "materialtype spaceoccupied"
ideas_88_89_extent.text = "33 digital files" # <-- will need to be updated
ideas_88_89_accessrestrict = etree.SubElement(ideas_88_89_c04, "accessrestrict")
ideas_88_89_accessrestrict_p = etree.SubElement(ideas_88_89_accessrestrict, "p")
ideas_88_89_accessrestrict_p.text = "RESTRICTED until "
ideas_88_89_date = etree.SubElement(ideas_88_89_accessrestrict_p, "date")
ideas_88_89_date.attrib["type"] = "restriction"
ideas_88_89_date.attrib["normal"] = "2030-07-01"
ideas_88_89_date.text = "July 1, 2030"

# populate 1988-1989 ideas subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1988-1989 Ideas"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(ideas_88_89_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]


# build out 1989-1990 ideas subseries
ideas_89_90_c04 = etree.SubElement(idea_files_c03, "c04")
ideas_89_90_c04.attrib["level"] = "subseries"
ideas_89_90_did = etree.SubElement(ideas_89_90_c04, "did")
ideas_89_90_physloc = etree.SubElement(ideas_89_90_did, "physloc")
ideas_89_90_physloc.text = "Online"
ideas_89_90_unittitle = etree.SubElement(ideas_89_90_did, "unittitle")
ideas_89_90_unittitle.text = "1989-1990 Ideas"
ideas_89_90_physdesc = etree.SubElement(ideas_89_90_did, "physdesc")
ideas_89_90_physdesc.attrib["altrender"] = "whole"
ideas_89_90_extent = etree.SubElement(ideas_89_90_physdesc, "extent")
ideas_89_90_extent.attrib["altrender"] = "materialtype spaceoccupied"
ideas_89_90_extent.text = "47 digital files" # <-- will need to be updated
ideas_89_90_accessrestrict = etree.SubElement(ideas_89_90_c04, "accessrestrict")
ideas_89_90_accessrestrict_p = etree.SubElement(ideas_89_90_accessrestrict, "p")
ideas_89_90_accessrestrict_p.text = "RESTRICTED until "
ideas_89_90_date = etree.SubElement(ideas_89_90_accessrestrict_p, "date")
ideas_89_90_date.attrib["type"] = "restriction"
ideas_89_90_date.attrib["normal"] = "2030-07-01"
ideas_89_90_date.text = "July 1, 2030"

# populate 1989-1990 ideas subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1989-1990 Ideas"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(ideas_89_90_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1990-1991 ideas subseries
ideas_90_91_c04 = etree.SubElement(idea_files_c03, "c04")
ideas_90_91_c04.attrib["level"] = "subseries"
ideas_90_91_did = etree.SubElement(ideas_90_91_c04, "did")
ideas_90_91_physloc = etree.SubElement(ideas_90_91_did, "physloc")
ideas_90_91_physloc.text = "Online"
ideas_90_91_unittitle = etree.SubElement(ideas_90_91_did, "unittitle")
ideas_90_91_unittitle.text = "1990-1991 Ideas"
ideas_90_91_physdesc = etree.SubElement(ideas_90_91_did, "physdesc")
ideas_90_91_physdesc.attrib["altrender"] = "whole"
ideas_90_91_extent = etree.SubElement(ideas_90_91_physdesc, "extent")
ideas_90_91_extent.attrib["altrender"] = "materialtype spaceoccupied"
ideas_90_91_extent.text = "29 digital files" # <-- will need to be updated
ideas_90_91_accessrestrict = etree.SubElement(ideas_90_91_c04, "accessrestrict")
ideas_90_91_accessrestrict_p = etree.SubElement(ideas_90_91_accessrestrict, "p")
ideas_90_91_accessrestrict_p.text = "RESTRICTED until "
ideas_90_91_date = etree.SubElement(ideas_90_91_accessrestrict_p, "date")
ideas_90_91_date.attrib["type"] = "restriction"
ideas_90_91_date.attrib["normal"] = "2030-07-01"
ideas_90_91_date.text = "July 1, 2030"

# populate 1990-1991 ideas subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1990-1991 Ideas"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(ideas_90_91_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1991-1992 ideas subseries
ideas_91_92_c04 = etree.SubElement(idea_files_c03, "c04")
ideas_91_92_c04.attrib["level"] = "subseries"
ideas_91_92_did = etree.SubElement(ideas_91_92_c04, "did")
ideas_91_92_physloc = etree.SubElement(ideas_91_92_did, "physloc")
ideas_91_92_physloc.text = "Online"
ideas_91_92_unittitle = etree.SubElement(ideas_91_92_did, "unittitle")
ideas_91_92_unittitle.text = "1991-1992 Ideas"
ideas_91_92_physdesc = etree.SubElement(ideas_91_92_did, "physdesc")
ideas_91_92_physdesc.attrib["altrender"] = "whole"
ideas_91_92_extent = etree.SubElement(ideas_91_92_physdesc, "extent")
ideas_91_92_extent.attrib["altrender"] = "materialtype spaceoccupied"
ideas_91_92_extent.text = "20 digital files" # <-- will need to be updated
ideas_91_92_accessrestrict = etree.SubElement(ideas_91_92_c04, "accessrestrict")
ideas_91_92_accessrestrict_p = etree.SubElement(ideas_91_92_accessrestrict, "p")
ideas_91_92_accessrestrict_p.text = "RESTRICTED until "
ideas_91_92_date = etree.SubElement(ideas_91_92_accessrestrict_p, "date")
ideas_91_92_date.attrib["type"] = "restriction"
ideas_91_92_date.attrib["normal"] = "2030-07-01"
ideas_91_92_date.text = "July 1, 2030"

# populate 1991-1992 ideas subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1991-1992 Ideas"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(ideas_91_92_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1992-1993 ideas subseries
ideas_92_93_c04 = etree.SubElement(idea_files_c03, "c04")
ideas_92_93_c04.attrib["level"] = "subseries"
ideas_92_93_did = etree.SubElement(ideas_92_93_c04, "did")
ideas_92_93_physloc = etree.SubElement(ideas_92_93_did, "physloc")
ideas_92_93_physloc.text = "Online"
ideas_92_93_unittitle = etree.SubElement(ideas_92_93_did, "unittitle")
ideas_92_93_unittitle.text = "1992-1993 Ideas"
ideas_92_93_physdesc = etree.SubElement(ideas_92_93_did, "physdesc")
ideas_92_93_physdesc.attrib["altrender"] = "whole"
ideas_92_93_extent = etree.SubElement(ideas_92_93_physdesc, "extent")
ideas_92_93_extent.attrib["altrender"] = "materialtype spaceoccupied"
ideas_92_93_extent.text = "30 digital files" # <-- will need to be updated
ideas_92_93_accessrestrict = etree.SubElement(ideas_92_93_c04, "accessrestrict")
ideas_92_93_accessrestrict_p = etree.SubElement(ideas_92_93_accessrestrict, "p")
ideas_92_93_accessrestrict_p.text = "RESTRICTED until "
ideas_92_93_date = etree.SubElement(ideas_92_93_accessrestrict_p, "date")
ideas_92_93_date.attrib["type"] = "restriction"
ideas_92_93_date.attrib["normal"] = "2030-07-01"
ideas_92_93_date.text = "July 1, 2030"

# populate 1992-1993 ideas subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1992-1993 Ideas"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(ideas_92_93_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1993-1994 ideas subseries
ideas_93_94_c04 = etree.SubElement(idea_files_c03, "c04")
ideas_93_94_c04.attrib["level"] = "subseries"
ideas_93_94_did = etree.SubElement(ideas_93_94_c04, "did")
ideas_93_94_physloc = etree.SubElement(ideas_93_94_did, "physloc")
ideas_93_94_physloc.text = "Online"
ideas_93_94_unittitle = etree.SubElement(ideas_93_94_did, "unittitle")
ideas_93_94_unittitle.text = "1993-1994 Ideas"
ideas_93_94_physdesc = etree.SubElement(ideas_93_94_did, "physdesc")
ideas_93_94_physdesc.attrib["altrender"] = "whole"
ideas_93_94_extent = etree.SubElement(ideas_93_94_physdesc, "extent")
ideas_93_94_extent.attrib["altrender"] = "materialtype spaceoccupied"
ideas_93_94_extent.text = "57 digital files" # <-- will need to be updated
ideas_93_94_accessrestrict = etree.SubElement(ideas_93_94_c04, "accessrestrict")
ideas_93_94_accessrestrict_p = etree.SubElement(ideas_93_94_accessrestrict, "p")
ideas_93_94_accessrestrict_p.text = "RESTRICTED until "
ideas_93_94_date = etree.SubElement(ideas_93_94_accessrestrict_p, "date")
ideas_93_94_date.attrib["type"] = "restriction"
ideas_93_94_date.attrib["normal"] = "2030-07-01"
ideas_93_94_date.text = "July 1, 2030"

# populate 1993-1994 ideassubseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1993-1994 Ideas"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(ideas_93_94_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1994-1995 ideas subseries
ideas_94_95_c04 = etree.SubElement(idea_files_c03, "c04")
ideas_94_95_c04.attrib["level"] = "subseries"
ideas_94_95_did = etree.SubElement(ideas_94_95_c04, "did")
ideas_94_95_physloc = etree.SubElement(ideas_94_95_did, "physloc")
ideas_94_95_physloc.text = "Online"
ideas_94_95_unittitle = etree.SubElement(ideas_94_95_did, "unittitle")
ideas_94_95_unittitle.text = "1994-1995 Ideas"
ideas_94_95_physdesc = etree.SubElement(ideas_94_95_did, "physdesc")
ideas_94_95_physdesc.attrib["altrender"] = "whole"
ideas_94_95_extent = etree.SubElement(ideas_94_95_physdesc, "extent")
ideas_94_95_extent.attrib["altrender"] = "materialtype spaceoccupied"
ideas_94_95_extent.text = "31 digital files" # <-- will need to be updated
ideas_94_95_accessrestrict = etree.SubElement(ideas_94_95_c04, "accessrestrict")
ideas_94_95_accessrestrict_p = etree.SubElement(ideas_94_95_accessrestrict, "p")
ideas_94_95_accessrestrict_p.text = "RESTRICTED until "
ideas_94_95_date = etree.SubElement(ideas_94_95_accessrestrict_p, "date")
ideas_94_95_date.attrib["type"] = "restriction"
ideas_94_95_date.attrib["normal"] = "2030-07-01"
ideas_94_95_date.text = "July 1, 2030"

# populate 1994-1995 ideas subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1994-1995 Ideas"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(ideas_94_95_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out strategy series
strategy_c03 = etree.SubElement(umich_presidency_c02, "c03")
strategy_c03.attrib["level"] = "series"
strategy_did = etree.SubElement(strategy_c03, "did")
strategy_unittitle = etree.SubElement(strategy_did, "unittitle")
strategy_unittitle.text = "Strategy" + ", "
strategy_unitdate = etree.SubElement(strategy_unittitle, "unitdate")
strategy_unitdate.text = "1986-1997"
strategy_unitdate.attrib["type"] = "inclusive"
strategy_unitdate.attrib["normal"] = "1986/1997"
strategy_physdesc = etree.SubElement(strategy_did, "physdesc")
strategy_physdesc.attrib["altrender"] = "whole"
strategy_extent = etree.SubElement(strategy_physdesc, "extent")
strategy_extent.attrib["altrender"] = "materialtype spaceoccupied"
strategy_extent.text = "63 digital files" # <-- will need to be updated
strategy_scopecontent = etree.SubElement(strategy_c03, "scopecontent")
strategy_scopecontent_p1 = etree.SubElement(strategy_scopecontent, "p")
strategy_scopecontent_p1.text = "While the other series in the Duderstadt Digital Documents subgroup contain records which cover a variety of topics, the Strategy series (84 files, 1986-1996) is largely focused on issues specifically related to President Duderstadt's vision of higher education in the 21st century. The framework for his position of the future of education can be found in two key documents: 'Vision 2000: The Leaders and Best' and 'Vision 2017: Transforming the University.'"
strategy_scopecontent_p2 = etree.SubElement(strategy_scopecontent, "p")
strategy_scopecontent_p2.text = "Duderstadt's espousal of the changing environment and the need for traditional institutions to transform is captured in this series. A researcher interested in his views on organizational change should look at the files containing the word transformation or variants with 'trans' such as, 'Transformation Text 1.6,' 'Trans Team 2.0,' and 'Trans Course 2.1.' For a summary of Duderstadt's major strategic initiatives, priorities for the coming decade, and views of changes needed in education, research, and diversity consult the file 'The Decade Report.' This report outlines major initiatives introduced to the university by Duderstadt such as the Institute for the Humanities, the Media Union, Institute of Molecular Medicine, and the Tauber Manufacturing Institute. The digital file titled 'Accomplishments,' written in the fall of 1995, provides a very informative outline of Duderstadt's priorities for the decade, accomplishments, projects (listed by year), strategic plan (Phases I, II, III), major papers, and selected speeches (listed by year). Lastly, this series contains in the 1996-1997 Strategy subseries the records related to Duderstadt's vision of 'The New University' and 'The Millennium Project.'"

# build out 1986-1997 subseries
strategy_86_97_c04 = etree.SubElement(strategy_c03, "c04")
strategy_86_97_c04.attrib["level"] = "subseries"
strategy_86_97_did = etree.SubElement(strategy_86_97_c04, "did")
strategy_86_97_physloc = etree.SubElement(strategy_86_97_did, "physloc")
strategy_86_97_physloc.text = "Online"
strategy_86_97_unittitle = etree.SubElement(strategy_86_97_did, "unittitle")
strategy_86_97_unittitle.text = "1986-1997"
strategy_86_97_physdesc = etree.SubElement(strategy_86_97_did, "physdesc")
strategy_86_97_physdesc.attrib["altrender"] = "whole"
strategy_86_97_extent = etree.SubElement(strategy_86_97_physdesc, "extent")
strategy_86_97_extent.attrib["altrender"] = "materialtype spaceoccupied"
strategy_86_97_extent.text = "63 digital files" # <-- will need to be updated
strategy_86_97_accessrestrict = etree.SubElement(strategy_86_97_c04, "accessrestrict")
strategy_86_97_accessrestrict_p = etree.SubElement(strategy_86_97_accessrestrict, "p")
strategy_86_97_accessrestrict_p.text = "RESTRICTED until "
strategy_86_97_date = etree.SubElement(strategy_86_97_accessrestrict_p, "date")
strategy_86_97_date.attrib["type"] = "restriction"
strategy_86_97_date.attrib["normal"] = "2030-07-01"
strategy_86_97_date.text = "July 1, 2030"

# populate 1986-1997 subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Strategy" + " - " + "1986-1997"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(strategy_86_97_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out position papers series
position_papers_c03 = etree.SubElement(umich_presidency_c02, "c03")
position_papers_c03.attrib["level"] = "series"
position_papers_did = etree.SubElement(position_papers_c03, "did")
position_papers_unittitle = etree.SubElement(position_papers_did, "unittitle")
position_papers_unittitle.text = "Position Papers" + ", "
position_papers_unitdate = etree.SubElement(position_papers_unittitle, "unitdate")
position_papers_unitdate.text = "1986-1997"
position_papers_unitdate.attrib["type"] = "inclusive"
position_papers_unitdate.attrib["normal"] = "1986/1997"
position_papers_physdesc = etree.SubElement(position_papers_did, "physdesc")
position_papers_physdesc.attrib["altrender"] = "whole"
position_papers_extent = etree.SubElement(position_papers_physdesc, "extent")
position_papers_extent.attrib["altrender"] = "materialtype spaceoccupied"
position_papers_extent.text = "140 digital files" # <-- will need to be updated
position_papers_scopecontent = etree.SubElement(position_papers_c03, "scopecontent")
position_papers_scopecontent_p = etree.SubElement(position_papers_scopecontent, "p")
position_papers_scopecontent_p.text = "The Position Papers series (140 digital files, 1986-1997) contains Duderstadt's key addresses, white papers, planning documents, annual reports, and presidential essays. Major papers contained in this series include: 'The Michigan Mandate: A Strategic Linking of Academic Excellence and Social Diversity,' 'The Role of the Research University in Undergraduate Education,' 'Michigan's Challenge: Preparing for an Age of Knowledge,' 'The Michigan Agenda for Women: Toward a Full and Equal Partnership,' 'Intellectual Transformation.' A complete list of major position papers can be found in the digital file titled 'Accomplishments' located in the Strategy series. Researchers will note that several versions of a document are in the Digital Documents subgroup, and that Duderstadt used a numbering scheme to organize versions of an digital document. One example of his file naming scheme is a series of files from the 1991-1996 subseries entitled 'Women 3.2,' 'Women 3.3,' 'Women 3.4.'"

# build out 1986-1991 position papers subseries
position_papers_86_91_c04 = etree.SubElement(position_papers_c03, "c04")
position_papers_86_91_c04.attrib["level"] = "subseries"
position_papers_86_91_did = etree.SubElement(position_papers_86_91_c04, "did")
position_papers_86_91_physloc = etree.SubElement(position_papers_86_91_did, "physloc")
position_papers_86_91_physloc.text = "Online"
position_papers_86_91_unittitle = etree.SubElement(position_papers_86_91_did, "unittitle")
position_papers_86_91_unittitle.text = "1986-1991 Position Papers"
position_papers_86_91_physdesc = etree.SubElement(position_papers_86_91_did, "physdesc")
position_papers_86_91_physdesc.attrib["altrender"] = "whole"
position_papers_86_91_extent = etree.SubElement(position_papers_86_91_physdesc, "extent")
position_papers_86_91_extent.attrib["altrender"] = "materialtype spaceoccupied"
position_papers_86_91_extent.text = "74 digital files" # <-- will need to be updated
position_papers_86_91_accessrestrict = etree.SubElement(position_papers_86_91_c04, "accessrestrict")
position_papers_86_91_accessrestrict_p = etree.SubElement(position_papers_86_91_accessrestrict, "p")
position_papers_86_91_accessrestrict_p.text = "RESTRICTED until "
position_papers_86_91_date = etree.SubElement(position_papers_86_91_accessrestrict_p, "date")
position_papers_86_91_date.attrib["type"] = "restriction"
position_papers_86_91_date.attrib["normal"] = "2030-07-01"
position_papers_86_91_date.text = "July 1, 2030"

# populate 1986-1991 position papers subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Position Papers" + " - " + "1986-1991 Position Papers"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(position_papers_86_91_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1991-1996 position papers subseries
position_papers_91_96_c04 = etree.SubElement(position_papers_c03, "c04")
position_papers_91_96_c04.attrib["level"] = "subseries"
position_papers_91_96_did = etree.SubElement(position_papers_91_96_c04, "did")
position_papers_91_96_physloc = etree.SubElement(position_papers_91_96_did, "physloc")
position_papers_91_96_physloc.text = "Online"
position_papers_91_96_unittitle = etree.SubElement(position_papers_91_96_did, "unittitle")
position_papers_91_96_unittitle.text = "1991-1996 Position Papers"
position_papers_91_96_physdesc = etree.SubElement(position_papers_91_96_did, "physdesc")
position_papers_91_96_physdesc.attrib["altrender"] = "whole"
position_papers_91_96_extent = etree.SubElement(position_papers_91_96_physdesc, "extent")
position_papers_91_96_extent.attrib["altrender"] = "materialtype spaceoccupied"
position_papers_91_96_extent.text = "66 digital files" # <-- will need to be updated
position_papers_91_96_accessrestrict = etree.SubElement(position_papers_91_96_c04, "accessrestrict")
position_papers_91_96_accessrestrict_p = etree.SubElement(position_papers_91_96_accessrestrict, "p")
position_papers_91_96_accessrestrict_p.text = "RESTRICTED until "
position_papers_91_96_date = etree.SubElement(position_papers_91_96_accessrestrict_p, "date")
position_papers_91_96_date.attrib["type"] = "restriction"
position_papers_91_96_date.attrib["normal"] = "2030-07-01"
position_papers_91_96_date.text = "July 1, 2030"

# populate 1991-1996 position papers subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Position Papers" + " - " + "1991-1996 Position Papers"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(position_papers_91_96_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1996-1997 position papers subseries
position_papers_96_97_c04 = etree.SubElement(position_papers_c03, "c04")
position_papers_96_97_c04.attrib["level"] = "subseries"
position_papers_96_97_did = etree.SubElement(position_papers_96_97_c04, "did")
position_papers_96_97_physloc = etree.SubElement(position_papers_96_97_did, "physloc")
position_papers_96_97_physloc.text = "Online"
position_papers_96_97_unittitle = etree.SubElement(position_papers_96_97_did, "unittitle")
position_papers_96_97_unittitle.text = "1996-1997 Position Papers"
position_papers_96_97_physdesc = etree.SubElement(position_papers_96_97_did, "physdesc")
position_papers_96_97_physdesc.attrib["altrender"] = "whole"
position_papers_96_97_extent = etree.SubElement(position_papers_96_97_physdesc, "extent")
position_papers_96_97_extent.attrib["altrender"] = "materialtype spaceoccupied"
position_papers_96_97_extent.text = "4 digital files" # <-- will need to be updated
position_papers_96_97_accessrestrict = etree.SubElement(position_papers_96_97_c04, "accessrestrict")
position_papers_96_97_accessrestrict_p = etree.SubElement(position_papers_96_97_accessrestrict, "p")
position_papers_96_97_accessrestrict_p.text = "RESTRICTED until "
position_papers_96_97_date = etree.SubElement(position_papers_96_97_accessrestrict_p, "date")
position_papers_96_97_date.attrib["type"] = "restriction"
position_papers_96_97_date.attrib["normal"] = "2030-07-01"
position_papers_96_97_date.text = "July 1, 2030"

# populate 1996-1997 position papers subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Position Papers" + " - " + "1996-1997 Position Papers"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(position_papers_96_97_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]
            
# build out presentations series
presentations_c03 = etree.SubElement(umich_presidency_c02, "c03")
presentations_c03.attrib["level"] = "series"
presentations_did = etree.SubElement(presentations_c03, "did")
presentations_unittitle = etree.SubElement(presentations_did, "unittitle")
presentations_unittitle.text = "Presentations" + ", "
presentations_unitdate = etree.SubElement(presentations_unittitle, "unitdate")
presentations_unitdate.text = "1987-1997"
presentations_unitdate.attrib["type"] = "inclusive"
presentations_unitdate.attrib["normal"] = "1987/1997"
presentations_physdesc = etree.SubElement(presentations_did, "physdesc")
presentations_physdesc.attrib["altrender"] = "whole"
presentations_extent = etree.SubElement(presentations_physdesc, "extent")
presentations_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_extent.text = "64 digital files" # <-- will need to be updated
presentations_scopecontent = etree.SubElement(presentations_c03, "scopecontent")
presentations_scopecontent_p1 = etree.SubElement(presentations_scopecontent, "p")
presentations_scopecontent_p1.text = "The majority of records in the Presentations series (64 digital files, 1987-1996) were created using the software application PowerPoint by Microsoft. This application was designed specifically as a presentation tool. Many of the records in this series seem to be presentations given to Duderstadt's Executive Officers (EOs) and the Regents at retreat meetings (for example, 'Regents Retreat,' 'Tuition Retreat,' 'Leadership Retreat'). Other presentation topics included in this series are The Michigan Mandate, The Mission Plan, and University Resources."
presentations_scopecontent_p2 = etree.SubElement(presentations_scopecontent, "p")
presentations_scopecontent_p2.text = "Researchers will note that in the Digital Documents subgroup contextual and descriptive information such as audience, location, and exact date of the presentation or speech is not always explicit in the digital record."

# build out 1987-1988 presentations subseries
presentations_87_88_c04 = etree.SubElement(presentations_c03, "c04")
presentations_87_88_c04.attrib["level"] = "subseries"
presentations_87_88_did = etree.SubElement(presentations_87_88_c04, "did")
presentations_87_88_physloc = etree.SubElement(presentations_87_88_did, "physloc")
presentations_87_88_physloc.text = "Online"
presentations_87_88_unittitle = etree.SubElement(presentations_87_88_did, "unittitle")
presentations_87_88_unittitle.text = "1987-1988 Presentations"
presentations_87_88_physdesc = etree.SubElement(presentations_87_88_did, "physdesc")
presentations_87_88_physdesc.attrib["altrender"] = "whole"
presentations_87_88_extent = etree.SubElement(presentations_87_88_physdesc, "extent")
presentations_87_88_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_87_88_extent.text = "1 digital files" # <-- will need to be updated

# populate 1987-1988 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1987-1988 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_87_88_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1988-1989 presentations subseries
presentations_88_89_c04 = etree.SubElement(presentations_c03, "c04")
presentations_88_89_c04.attrib["level"] = "subseries"
presentations_88_89_did = etree.SubElement(presentations_88_89_c04, "did")
presentations_88_89_physloc = etree.SubElement(presentations_88_89_did, "physloc")
presentations_88_89_physloc.text = "Online"
presentations_88_89_unittitle = etree.SubElement(presentations_88_89_did, "unittitle")
presentations_88_89_unittitle.text = "1988-1989 Presentations"
presentations_88_89_physdesc = etree.SubElement(presentations_88_89_did, "physdesc")
presentations_88_89_physdesc.attrib["altrender"] = "whole"
presentations_88_89_extent = etree.SubElement(presentations_88_89_physdesc, "extent")
presentations_88_89_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_88_89_extent.text = "5 digital files" # <-- will need to be updated

# populate 1988-1989 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1988-1989 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_88_89_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1989-1990 presentations subseries
presentations_98_90_c04 = etree.SubElement(presentations_c03, "c04")
presentations_98_90_c04.attrib["level"] = "subseries"
presentations_98_90_did = etree.SubElement(presentations_98_90_c04, "did")
presentations_98_90_physloc = etree.SubElement(presentations_98_90_did, "physloc")
presentations_98_90_physloc.text = "Online"
presentations_98_90_unittitle = etree.SubElement(presentations_98_90_did, "unittitle")
presentations_98_90_unittitle.text = "1989-1990 Presentations"
presentations_98_90_physdesc = etree.SubElement(presentations_98_90_did, "physdesc")
presentations_98_90_physdesc.attrib["altrender"] = "whole"
presentations_98_90_extent = etree.SubElement(presentations_98_90_physdesc, "extent")
presentations_98_90_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_98_90_extent.text = "8 digital files" # <-- will need to be updated

# populate 1989-1990 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1989-1990 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_89_90_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]
            
# build out 1990-1991 presentations subseries
presentations_90_91_c04 = etree.SubElement(presentations_c03, "c04")
presentations_90_91_c04.attrib["level"] = "subseries"
presentations_90_91_did = etree.SubElement(presentations_90_91_c04, "did")
presentations_90_91_physloc = etree.SubElement(presentations_90_91_did, "physloc")
presentations_90_91_physloc.text = "Online"
presentations_90_91_unittitle = etree.SubElement(presentations_90_91_did, "unittitle")
presentations_90_91_unittitle.text = "1990-1991 Presentations"
presentations_90_91_physdesc = etree.SubElement(presentations_90_91_did, "physdesc")
presentations_90_91_physdesc.attrib["altrender"] = "whole"
presentations_90_91_extent = etree.SubElement(presentations_90_91_physdesc, "extent")
presentations_90_91_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_90_91_extent.text = "13 digital files" # <-- will need to be updated

# populate 1990-1991 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1990-1991 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_90_91_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1991-1992 presentations subseries
presentations_91_92_c04 = etree.SubElement(presentations_c03, "c04")
presentations_91_92_c04.attrib["level"] = "subseries"
presentations_91_92_did = etree.SubElement(presentations_91_92_c04, "did")
presentations_91_92_physloc = etree.SubElement(presentations_91_92_did, "physloc")
presentations_91_92_physloc.text = "Online"
presentations_91_92_unittitle = etree.SubElement(presentations_91_92_did, "unittitle")
presentations_91_92_unittitle.text = "1991-1992 Presentations"
presentations_91_92_physdesc = etree.SubElement(presentations_91_92_did, "physdesc")
presentations_91_92_physdesc.attrib["altrender"] = "whole"
presentations_91_92_extent = etree.SubElement(presentations_91_92_physdesc, "extent")
presentations_91_92_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_91_92_extent.text = "17 digital files" # <-- will need to be updated

# populate 1991-1992 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1991-1992 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_91_92_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]
            
# build out 1992-1993 presentations subseries
presentations_92_93_c04 = etree.SubElement(presentations_c03, "c04")
presentations_92_93_c04.attrib["level"] = "subseries"
presentations_92_93_did = etree.SubElement(presentations_92_93_c04, "did")
presentations_92_93_physloc = etree.SubElement(presentations_92_93_did, "physloc")
presentations_92_93_physloc.text = "Online"
presentations_92_93_unittitle = etree.SubElement(presentations_92_93_did, "unittitle")
presentations_92_93_unittitle.text = "1992-1993 Presentations"
presentations_92_93_physdesc = etree.SubElement(presentations_92_93_did, "physdesc")
presentations_92_93_physdesc.attrib["altrender"] = "whole"
presentations_92_93_extent = etree.SubElement(presentations_92_93_physdesc, "extent")
presentations_92_93_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_92_93_extent.text = "3 digital files" # <-- will need to be updated

# populate 1992-1993 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1992-1993 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_92_93_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1993-1994 presentations subseries
presentations_93_94_c04 = etree.SubElement(presentations_c03, "c04")
presentations_93_94_c04.attrib["level"] = "subseries"
presentations_93_94_did = etree.SubElement(presentations_93_94_c04, "did")
presentations_93_94_physloc = etree.SubElement(presentations_93_94_did, "physloc")
presentations_93_94_physloc.text = "Online"
presentations_93_94_unittitle = etree.SubElement(presentations_93_94_did, "unittitle")
presentations_93_94_unittitle.text = "1993-1994 Presentations"
presentations_93_94_physdesc = etree.SubElement(presentations_93_94_did, "physdesc")
presentations_93_94_physdesc.attrib["altrender"] = "whole"
presentations_93_94_extent = etree.SubElement(presentations_93_94_physdesc, "extent")
presentations_93_94_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_93_94_extent.text = "1 digital files" # <-- will need to be updated

# populate 1993-1994 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1993-1994 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_93_94_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1994-1995 presentations subseries
presentations_94_95_c04 = etree.SubElement(presentations_c03, "c04")
presentations_94_95_c04.attrib["level"] = "subseries"
presentations_94_95_did = etree.SubElement(presentations_94_95_c04, "did")
presentations_94_95_physloc = etree.SubElement(presentations_94_95_did, "physloc")
presentations_94_95_physloc.text = "Online"
presentations_94_95_unittitle = etree.SubElement(presentations_94_95_did, "unittitle")
presentations_94_95_unittitle.text = "1994-1995 Presentations"
presentations_94_95_physdesc = etree.SubElement(presentations_94_95_did, "physdesc")
presentations_94_95_physdesc.attrib["altrender"] = "whole"
presentations_94_95_extent = etree.SubElement(presentations_94_95_physdesc, "extent")
presentations_94_95_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_94_95_extent.text = "2 digital files" # <-- will need to be updated

# populate 1994-1995 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1994-1995 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_94_95_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1995-1996 presentations subseries
presentations_95_96_c04 = etree.SubElement(presentations_c03, "c04")
presentations_95_96_c04.attrib["level"] = "subseries"
presentations_95_96_did = etree.SubElement(presentations_95_96_c04, "did")
presentations_95_96_physloc = etree.SubElement(presentations_95_96_did, "physloc")
presentations_95_96_physloc.text = "Online"
presentations_95_96_unittitle = etree.SubElement(presentations_95_96_did, "unittitle")
presentations_95_96_unittitle.text = "1995-1996 Presentations"
presentations_95_96_physdesc = etree.SubElement(presentations_95_96_did, "physdesc")
presentations_95_96_physdesc.attrib["altrender"] = "whole"
presentations_95_96_extent = etree.SubElement(presentations_95_96_physdesc, "extent")
presentations_95_96_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_95_96_extent.text = "3 digital files" # <-- will need to be updated

# populate 1995-1996 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1995-1996 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_95_96_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1996-1997 presentations subseries
presentations_96_97_c04 = etree.SubElement(presentations_c03, "c04")
presentations_96_97_c04.attrib["level"] = "subseries"
presentations_96_97_did = etree.SubElement(presentations_96_97_c04, "did")
presentations_96_97_physloc = etree.SubElement(presentations_96_97_did, "physloc")
presentations_96_97_physloc.text = "Online"
presentations_96_97_unittitle = etree.SubElement(presentations_96_97_did, "unittitle")
presentations_96_97_unittitle.text = "1996-1997 Presentations"
presentations_96_97_physdesc = etree.SubElement(presentations_96_97_did, "physdesc")
presentations_96_97_physdesc.attrib["altrender"] = "whole"
presentations_96_97_extent = etree.SubElement(presentations_96_97_physdesc, "extent")
presentations_96_97_extent.attrib["altrender"] = "materialtype spaceoccupied"
presentations_96_97_extent.text = "11 digital files" # <-- will need to be updated

# populate 1996-1997 presentations subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1996-1997 Presentations"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(presentations_96_97_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out write files series
write_files_c03 = etree.SubElement(umich_presidency_c02, "c03")
write_files_c03.attrib["level"] = "series"
write_files_did = etree.SubElement(write_files_c03, "did")
write_files_unittitle = etree.SubElement(write_files_did, "unittitle")
write_files_unittitle.text = "Write Files" + ", "
write_files_unitdate = etree.SubElement(write_files_unittitle, "unitdate")
write_files_unitdate.text = "1988-1997"
write_files_unitdate.attrib["type"] = "inclusive"
write_files_unitdate.attrib["normal"] = "1988/1997"
write_files_physdesc = etree.SubElement(write_files_did, "physdesc")
write_files_physdesc.attrib["altrender"] = "whole"
write_files_extent = etree.SubElement(write_files_physdesc, "extent")
write_files_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_extent.text = "588 digital files" # <-- will need to be updated
write_files_scopecontent = etree.SubElement(write_files_c03, "scopecontent")
write_files_scopecontent_p = etree.SubElement(write_files_scopecontent, "p")
write_files_scopecontent_p.text = "The Write Files series (588 digital files, 1987-1997) is composed entirely of Microsoft Word text files. Researchers will find a variety of 'traditional' business formats such as correspondence, agendas, and memorandums contained within the Write Files series. However, note that there is often an absence of descriptive information, such as the receiver's name and address, date, and signature line. The absence of this information is a reflection of the distributive work process practiced in President Duderstadt's office--a process afforded by networked computer technology. The correspondence includes letters of recommendation, thank-you's, and communication to persons not only at the University of Michigan but to persons throughout the country including U.S. presidents Gerald Ford and George Bush and Michigan governors James Blanchard and John Engler. It is important to note that Duderstadt often used the recipient's name or initials to name the file. For example, 'Blanchard-1/89' and 'H & V-11/10' are communications to Governor James Blanchard in January 1989 and Harold and Vivian Shapiro on November 10th respectively."

# build out 1988 and earlier write files
write_files_88_earlier_c04 = etree.SubElement(write_files_c03, "c04")
write_files_88_earlier_c04.attrib["level"] = "subseries"
write_files_88_earlier_did = etree.SubElement(write_files_88_earlier_c04, "did")
write_files_88_earlier_physloc = etree.SubElement(write_files_88_earlier_did, "physloc")
write_files_88_earlier_physloc.text = "Online"
write_files_88_earlier_unittitle = etree.SubElement(write_files_88_earlier_did, "unittitle")
write_files_88_earlier_unittitle.text = "1988 and earlier Write Files"
write_files_88_earlier_physdesc = etree.SubElement(write_files_88_earlier_did, "physdesc")
write_files_88_earlier_physdesc.attrib["altrender"] = "whole"
write_files_88_earlier_extent = etree.SubElement(write_files_88_earlier_physdesc, "extent")
write_files_88_earlier_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_88_earlier_extent.text = "19 digital files" # <-- will need to be updated
write_files_88_earlier_accessrestrict = etree.SubElement(write_files_88_earlier_c04, "accessrestrict")
write_files_88_earlier_accessrestrict_p = etree.SubElement(write_files_88_earlier_accessrestrict, "p")
write_files_88_earlier_accessrestrict_p.text = "RESTRICTED until "
write_files_88_earlier_date = etree.SubElement(write_files_88_earlier_accessrestrict_p, "date")
write_files_88_earlier_date.attrib["type"] = "restriction"
write_files_88_earlier_date.attrib["normal"] = "2030-07-01"
write_files_88_earlier_date.text = "July 1, 2030"

# populate 1988 and earlier write subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1988 and earlier 1988 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_88_earlier_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1988-1989 write files subseries
write_files_88_89_c04 = etree.SubElement(write_files_c03, "c04")
write_files_88_89_c04.attrib["level"] = "subseries"
write_files_88_89_did = etree.SubElement(write_files_88_89_c04, "did")
write_files_88_89_physloc = etree.SubElement(write_files_88_89_did, "physloc")
write_files_88_89_physloc.text = "Online"
write_files_88_89_unittitle = etree.SubElement(write_files_88_89_did, "unittitle")
write_files_88_89_unittitle.text = "1988-1989 Write Files"
write_files_88_89_physdesc = etree.SubElement(write_files_88_89_did, "physdesc")
write_files_88_89_physdesc.attrib["altrender"] = "whole"
write_files_88_89_extent = etree.SubElement(write_files_88_89_physdesc, "extent")
write_files_88_89_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_88_89_extent.text = "19 digital files" # <-- will need to be updated
write_files_88_89_accessrestrict = etree.SubElement(write_files_88_89_c04, "accessrestrict")
write_files_88_89_accessrestrict_p = etree.SubElement(write_files_88_89_accessrestrict, "p")
write_files_88_89_accessrestrict_p.text = "RESTRICTED until "
write_files_88_89_date = etree.SubElement(write_files_88_89_accessrestrict_p, "date")
write_files_88_89_date.attrib["type"] = "restriction"
write_files_88_89_date.attrib["normal"] = "2030-07-01"
write_files_88_89_date.text = "July 1, 2030"

# populate 1988-1989 write files subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1988-1989 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_88_89_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1989-1990 write files subseries
write_files_89_90_c04 = etree.SubElement(write_files_c03, "c04")
write_files_89_90_c04.attrib["level"] = "subseries"
write_files_89_90_did = etree.SubElement(write_files_89_90_c04, "did")
write_files_89_90_physloc = etree.SubElement(write_files_89_90_did, "physloc")
write_files_89_90_physloc.text = "Online"
write_files_89_90_unittitle = etree.SubElement(write_files_89_90_did, "unittitle")
write_files_89_90_unittitle.text = "1989-1990 Write Files"
write_files_89_90_physdesc = etree.SubElement(write_files_89_90_did, "physdesc")
write_files_89_90_physdesc.attrib["altrender"] = "whole"
write_files_89_90_extent = etree.SubElement(write_files_89_90_physdesc, "extent")
write_files_89_90_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_89_90_extent.text = "50 digital files" # <-- will need to be updated
write_files_89_90_accessrestrict = etree.SubElement(write_files_89_90_c04, "accessrestrict")
write_files_89_90_accessrestrict_p = etree.SubElement(write_files_89_90_accessrestrict, "p")
write_files_89_90_accessrestrict_p.text = "RESTRICTED until "
write_files_89_90_date = etree.SubElement(write_files_89_90_accessrestrict_p, "date")
write_files_89_90_date.attrib["type"] = "restriction"
write_files_89_90_date.attrib["normal"] = "2030-07-01"
write_files_89_90_date.text = "July 1, 2030"

# populate 1989-1990 write files subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1989-1990 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_89_90_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1990-1991 write files subseries
write_files_90_91_c04 = etree.SubElement(write_files_c03, "c04")
write_files_90_91_c04.attrib["level"] = "subseries"
write_files_90_91_did = etree.SubElement(write_files_90_91_c04, "did")
write_files_90_91_physloc = etree.SubElement(write_files_90_91_did, "physloc")
write_files_90_91_physloc.text = "Online"
write_files_90_91_unittitle = etree.SubElement(write_files_90_91_did, "unittitle")
write_files_90_91_unittitle.text = "1990-1991 Write Files"
write_files_90_91_physdesc = etree.SubElement(write_files_90_91_did, "physdesc")
write_files_90_91_physdesc.attrib["altrender"] = "whole"
write_files_90_91_extent = etree.SubElement(write_files_90_91_physdesc, "extent")
write_files_90_91_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_90_91_extent.text = "74 digital files" # <-- will need to be updated
write_files_90_91_accessrestrict = etree.SubElement(write_files_90_91_c04, "accessrestrict")
write_files_90_91_accessrestrict_p = etree.SubElement(write_files_90_91_accessrestrict, "p")
write_files_90_91_accessrestrict_p.text = "RESTRICTED until "
write_files_90_91_date = etree.SubElement(write_files_90_91_accessrestrict_p, "date")
write_files_90_91_date.attrib["type"] = "restriction"
write_files_90_91_date.attrib["normal"] = "2030-07-01"
write_files_90_91_date.text = "July 1, 2030"

# populate 1990-1991 write files subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1990-1991 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_90_91_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]
            
# build out 1991-1992 write files subseries
write_files_91_92_c04 = etree.SubElement(write_files_c03, "c04")
write_files_91_92_c04.attrib["level"] = "subseries"
write_files_91_92_did = etree.SubElement(write_files_91_92_c04, "did")
write_files_91_92_physloc = etree.SubElement(write_files_91_92_did, "physloc")
write_files_91_92_physloc.text = "Online"
write_files_91_92_unittitle = etree.SubElement(write_files_91_92_did, "unittitle")
write_files_91_92_unittitle.text = "1991-1992 Write Files"
write_files_91_92_physdesc = etree.SubElement(write_files_91_92_did, "physdesc")
write_files_91_92_physdesc.attrib["altrender"] = "whole"
write_files_91_92_extent = etree.SubElement(write_files_91_92_physdesc, "extent")
write_files_91_92_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_91_92_extent.text = "54 digital files" # <-- will need to be updated
write_files_91_92_accessrestrict = etree.SubElement(write_files_91_92_c04, "accessrestrict")
write_files_91_92_accessrestrict_p = etree.SubElement(write_files_91_92_accessrestrict, "p")
write_files_91_92_accessrestrict_p.text = "RESTRICTED until "
write_files_91_92_date = etree.SubElement(write_files_91_92_accessrestrict_p, "date")
write_files_91_92_date.attrib["type"] = "restriction"
write_files_91_92_date.attrib["normal"] = "2030-07-01"
write_files_91_92_date.text = "July 1, 2030"

# populate 1991-1992 write files subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1991-1992 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_91_92_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]
            
# build out 1992-1993 write files subseries
write_files_92_93_c04 = etree.SubElement(write_files_c03, "c04")
write_files_92_93_c04.attrib["level"] = "subseries"
write_files_92_93_did = etree.SubElement(write_files_92_93_c04, "did")
write_files_92_93_physloc = etree.SubElement(write_files_92_93_did, "physloc")
write_files_92_93_physloc.text = "Online"
write_files_92_93_unittitle = etree.SubElement(write_files_92_93_did, "unittitle")
write_files_92_93_unittitle.text = "1992-1993 Write Files"
write_files_92_93_physdesc = etree.SubElement(write_files_92_93_did, "physdesc")
write_files_92_93_physdesc.attrib["altrender"] = "whole"
write_files_92_93_extent = etree.SubElement(write_files_92_93_physdesc, "extent")
write_files_92_93_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_92_93_extent.text = "120 digital files" # <-- will need to be updated
write_files_92_93_accessrestrict = etree.SubElement(write_files_92_93_c04, "accessrestrict")
write_files_92_93_accessrestrict_p = etree.SubElement(write_files_92_93_accessrestrict, "p")
write_files_92_93_accessrestrict_p.text = "RESTRICTED until "
write_files_92_93_date = etree.SubElement(write_files_92_93_accessrestrict_p, "date")
write_files_92_93_date.attrib["type"] = "restriction"
write_files_92_93_date.attrib["normal"] = "2030-07-01"
write_files_92_93_date.text = "July 1, 2030"

# populate 1992-1993 write files subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1992-1993 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_92_93_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1993-1994 write files subseries
write_files_93_94_c04 = etree.SubElement(write_files_c03, "c04")
write_files_93_94_c04.attrib["level"] = "subseries"
write_files_93_94_did = etree.SubElement(write_files_93_94_c04, "did")
write_files_93_94_physloc = etree.SubElement(write_files_93_94_did, "physloc")
write_files_93_94_physloc.text = "Online"
write_files_93_94_unittitle = etree.SubElement(write_files_93_94_did, "unittitle")
write_files_93_94_unittitle.text = "1993-1994 Write Files"
write_files_93_94_physdesc = etree.SubElement(write_files_93_94_did, "physdesc")
write_files_93_94_physdesc.attrib["altrender"] = "whole"
write_files_93_94_extent = etree.SubElement(write_files_93_94_physdesc, "extent")
write_files_93_94_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_93_94_extent.text = "114 digital files" # <-- will need to be updated
write_files_93_94_accessrestrict = etree.SubElement(write_files_93_94_c04, "accessrestrict")
write_files_93_94_accessrestrict_p = etree.SubElement(write_files_93_94_accessrestrict, "p")
write_files_93_94_accessrestrict_p.text = "RESTRICTED until "
write_files_93_94_date = etree.SubElement(write_files_93_94_accessrestrict_p, "date")
write_files_93_94_date.attrib["type"] = "restriction"
write_files_93_94_date.attrib["normal"] = "2030-07-01"
write_files_93_94_date.text = "July 1, 2030"

# populate 1993-1994 write files subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1993-1994 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_93_94_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1994-1995 write files subseries
write_files_94_95_c04 = etree.SubElement(write_files_c03, "c04")
write_files_94_95_c04.attrib["level"] = "subseries"
write_files_94_95_did = etree.SubElement(write_files_94_95_c04, "did")
write_files_94_95_physloc = etree.SubElement(write_files_94_95_did, "physloc")
write_files_94_95_physloc.text = "Online"
write_files_94_95_unittitle = etree.SubElement(write_files_94_95_did, "unittitle")
write_files_94_95_unittitle.text = "1994-1995 Write Files"
write_files_94_95_physdesc = etree.SubElement(write_files_94_95_did, "physdesc")
write_files_94_95_physdesc.attrib["altrender"] = "whole"
write_files_94_95_extent = etree.SubElement(write_files_94_95_physdesc, "extent")
write_files_94_95_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_94_95_extent.text = "55 digital files" # <-- will need to be updated
write_files_94_95_accessrestrict = etree.SubElement(write_files_94_95_c04, "accessrestrict")
write_files_94_95_accessrestrict_p = etree.SubElement(write_files_94_95_accessrestrict, "p")
write_files_94_95_accessrestrict_p.text = "RESTRICTED until "
write_files_94_95_date = etree.SubElement(write_files_94_95_accessrestrict_p, "date")
write_files_94_95_date.attrib["type"] = "restriction"
write_files_94_95_date.attrib["normal"] = "2030-07-01"
write_files_94_95_date.text = "July 1, 2030"

# populate 1994-1995 write files subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1994-1995 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_94_95_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]
            
# build out 1995-1996 write files subseries
write_files_95_96_c04 = etree.SubElement(write_files_c03, "c04")
write_files_95_96_c04.attrib["level"] = "subseries"
write_files_95_96_did = etree.SubElement(write_files_95_96_c04, "did")
write_files_95_96_physloc = etree.SubElement(write_files_95_96_did, "physloc")
write_files_95_96_physloc.text = "Online"
write_files_95_96_unittitle = etree.SubElement(write_files_95_96_did, "unittitle")
write_files_95_96_unittitle.text = "1995-1996 Write Files"
write_files_95_96_physdesc = etree.SubElement(write_files_95_96_did, "physdesc")
write_files_95_96_physdesc.attrib["altrender"] = "whole"
write_files_95_96_extent = etree.SubElement(write_files_95_96_physdesc, "extent")
write_files_95_96_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_95_96_extent.text = "75 digital files" # <-- will need to be updated
write_files_95_96_accessrestrict = etree.SubElement(write_files_95_96_c04, "accessrestrict")
write_files_95_96_accessrestrict_p = etree.SubElement(write_files_95_96_accessrestrict, "p")
write_files_95_96_accessrestrict_p.text = "RESTRICTED until "
write_files_95_96_date = etree.SubElement(write_files_95_96_accessrestrict_p, "date")
write_files_95_96_date.attrib["type"] = "restriction"
write_files_95_96_date.attrib["normal"] = "2030-07-01"
write_files_95_96_date.text = "July 1, 2030"

# populate 1995-1996 write files subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1995-1996 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_95_96_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out 1996-1997 write files subseries
write_files_96_97_c04 = etree.SubElement(write_files_c03, "c04")
write_files_96_97_c04.attrib["level"] = "subseries"
write_files_96_97_did = etree.SubElement(write_files_96_97_c04, "did")
write_files_96_97_physloc = etree.SubElement(write_files_96_97_did, "physloc")
write_files_96_97_physloc.text = "Online"
write_files_96_97_unittitle = etree.SubElement(write_files_96_97_did, "unittitle")
write_files_96_97_unittitle.text = "1996-1997 Write Files"
write_files_96_97_physdesc = etree.SubElement(write_files_96_97_did, "physdesc")
write_files_96_97_physdesc.attrib["altrender"] = "whole"
write_files_96_97_extent = etree.SubElement(write_files_96_97_physdesc, "extent")
write_files_96_97_extent.attrib["altrender"] = "materialtype spaceoccupied"
write_files_96_97_extent.text = "8 digital files" # <-- will need to be updated
write_files_96_97_accessrestrict = etree.SubElement(write_files_96_97_c04, "accessrestrict")
write_files_96_97_accessrestrict_p = etree.SubElement(write_files_96_97_accessrestrict, "p")
write_files_96_97_accessrestrict_p.text = "RESTRICTED until "
write_files_96_97_date = etree.SubElement(write_files_96_97_accessrestrict_p, "date")
write_files_96_97_date.attrib["type"] = "restriction"
write_files_96_97_date.attrib["normal"] = "2030-07-01"
write_files_96_97_date.text = "July 1, 2030"

# populate 1996-1997 write files subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1996-1997 Write Files"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(write_files_96_97_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out legacy series
legacy_c03 = etree.SubElement(umich_presidency_c02, "c03")
legacy_c03.attrib["level"] = "series"
legacy_did = etree.SubElement(legacy_c03, "did")
legacy_unittitle = etree.SubElement(legacy_did, "unittitle")
legacy_unittitle.text = "Legacy" + ", "
legacy_unitdate = etree.SubElement(legacy_unittitle, "unitdate")
legacy_unitdate.text = "circa 1996"
legacy_unitdate.attrib["type"] = "inclusive"
legacy_unitdate.attrib["normal"] = "1996"
legacy_unitdate.attrib["certainty"] = "approximate"
legacy_physdesc = etree.SubElement(legacy_did, "physdesc")
legacy_physdesc.attrib["altrender"] = "whole"
legacy_extent = etree.SubElement(legacy_physdesc, "extent")
legacy_extent.attrib["altrender"] = "materialtype spaceoccupied"
legacy_extent.text = "36 digital files" # <-- will need to be updated
legacy_scopecontent = etree.SubElement(legacy_c03, "scopecontent")
legacy_scopecontent_p = etree.SubElement(legacy_scopecontent, "p")
legacy_scopecontent_p.text = "The Legacy Documents series (36 digital files, ca. 1996) contains the drafts of the digital records that resulted in a number of printed publications written by Duderstadt together entitled 'Legacy Documents.' The files in the 'Sunflower' sub-folder are those files that resulted in the publication entitled 'A Growing Season: A Report from the President . . .The University of Michigan, 1986-1996.' A complete set of printed 'Legacy' documents including 'A Growing Season...' is in the Paper Documents series Publications."

# build out 1996 subseries
legacy_96_c04 = etree.SubElement(presentations_c03, "c04")
legacy_96_c04.attrib["level"] = "subseries"
legacy_96_did = etree.SubElement(legacy_96_c04, "did")
legacy_96_physloc = etree.SubElement(legacy_96_did, "physloc")
legacy_96_physloc.text = "Online"
legacy_96_unittitle = etree.SubElement(legacy_96_did, "unittitle")
legacy_96_unittitle.text = "1996"
legacy_96_physdesc = etree.SubElement(legacy_96_did, "physdesc")
legacy_96_physdesc.attrib["altrender"] = "whole"
legacy_96_extent = etree.SubElement(legacy_96_physdesc, "extent")
legacy_96_extent.attrib["altrender"] = "materialtype spaceoccupied"
legacy_96_extent.text = "36 digital files" # <-- will need to be updated

# populate 1996 subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Legacy" + " - " + "1996"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(legacy_96_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

# build out digital images series
digital_images_c03 = etree.SubElement(umich_presidency_c02, "c03")
digital_images_c03.attrib["level"] = "series"
digital_images_did = etree.SubElement(digital_images_c03, "did")
digital_images_unittitle = etree.SubElement(digital_images_did, "unittitle")
digital_images_unittitle.text = "Digital Images" + ", "
digital_images_unitdate = etree.SubElement(digital_images_unittitle, "unitdate")
digital_images_unitdate.text = "circa 1996"
digital_images_unitdate.attrib["type"] = "inclusive"
digital_images_unitdate.attrib["normal"] = "1996"
digital_images_unitdate.attrib["certainty"] = "approximate"
digital_images_physdesc = etree.SubElement(digital_images_did, "physdesc")
digital_images_physdesc.attrib["altrender"] = "whole"
digital_images_extent = etree.SubElement(digital_images_physdesc, "extent")
digital_images_extent.attrib["altrender"] = "materialtype spaceoccupied"
digital_images_extent.text = "55 digital files" # <-- will need to be updated
digital_images_scopecontent = etree.SubElement(digital_images_c03, "scopecontent")
digital_images_scopecontent_p = etree.SubElement(digital_images_scopecontent, "p")
digital_images_scopecontent_p.text = "The Digital Images series (55 digital files, ca. 1996) provides a look at the many buildings either newly constructed or renovated during Duderstadt's presidential tenure at Michigan. The Ann Arbor campus underwent major changes to the Central, North, Athletic, and Medical campuses. New construction projects include the Media Union, Cancer &amp; Geriatrics Center, Medical Science Research Building, Lurie Engineering Center and Bell Tower, Donald Canham Natatorium, and the Glenn E. Schembechler Hall. Major renovation and improvement projects include Angell Hall, CC Little, Chemistry Building, and Health Service. Included in this series are images of the buildings constructed on the U-M Dearborn and Flint campuses. A complete listing of all construction and renovation projects is highlighted in a special booklet titled 'Rebuilding the University, The University of Michigan 1986-1996.' A copy of this document is in the Paper Documents series Publications."

# build out 1996 subseries
digital_images_96_c04 = etree.SubElement(presentations_c03, "c04")
digital_images_96_c04.attrib["level"] = "subseries"
digital_images_96_did = etree.SubElement(digital_images_96_c04, "did")
digital_images_96_physloc = etree.SubElement(digital_images_96_did, "physloc")
digital_images_96_physloc.text = "Online"
digital_images_96_unittitle = etree.SubElement(digital_images_96_did, "unittitle")
digital_images_96_unittitle.text = "1996"
digital_images_96_physdesc = etree.SubElement(digital_images_96_did, "physdesc")
digital_images_96_physdesc.attrib["altrender"] = "whole"
digital_images_96_extent = etree.SubElement(digital_images_96_physdesc, "extent")
digital_images_96_extent.attrib["altrender"] = "materialtype spaceoccupied"
digital_images_96_extent.text = "36 digital files" # <-- will need to be updated
digital_images_96_accessrestrict = etree.SubElement(digital_images_96_c04, "accessrestrict")
digital_images_96_accessrestrict_p = etree.SubElement(digital_images_96_accessrestrict, "p")
digital_images_96_accessrestrict_p.text = "RESTRICTED until "
digital_images_96_date = etree.SubElement(digital_images_96_accessrestrict_p, "date")
digital_images_96_date.attrib["type"] = "restriction"
digital_images_96_date.attrib["normal"] = "2030-07-01"
digital_images_96_date.text = "July 1, 2030"

# populate 1996 subseries
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Digital Images" + " - " + "1996"):
        
        print "Creating XML for " + sorted_metadatum["unittitle"] + "..."
        
        sorted_metadatum_c05 = etree.SubElement(digital_images_96_c04, "c05")
        sorted_metadatum_c05.attrib["level"] = "file"
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
        sorted_metadatum_dao.attrib["href"] = sorted_metadatum["dao"]
        sorted_metadatum_daodesc = etree.SubElement(sorted_metadatum_dao, "daodesc")
        sorted_metadatum_daodesc_p = etree.SubElement(sorted_metadatum_daodesc, "p")
        sorted_metadatum_daodesc_p.text = "[view item]"
        if "accessrestrict" in sorted_metadatum:
            sorted_metadatum_accessrestrict = etree.SubElement(sorted_metadatum_c03, "accessrestrict")
            sorted_metadatum_accessrestrict_p = etree.SubElement(sorted_metadatum_accessrestrict, "p")
            sorted_metadatum_accessrestrict_p.text = sorted_metadatum["accessrestrict"]

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
    <dao show="new" actuate="onrequest" href="http://hdl.handle.net/2027.42/101933" show="new" actuate="onrequest">
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
for sorted_metadatum in sorted_metadata:

    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997"):
        continue
    
    else:
    
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
        sorted_metadatum_dao.attrib["show"] = "new"
        sorted_metadatum_dao.attrib["actuate"] = "onrequest"
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
