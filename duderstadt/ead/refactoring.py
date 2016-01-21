from lxml import etree
import pickle
from operator import itemgetter

parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse("C:\Users\eckardm\work-stuff\duderstadt\ead\duderst.xml", parser=parser)

old_digital_documents = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]")[0]
parent = old_digital_documents.getparent()
parent.remove(old_digital_documents)

def make_c01_subgroup(unittitle_text, extent_text, physfacet_text, scopecontent_p1_text, scopecontent_p2_text):
    c01 = etree.Element("c01")
    c01.attrib["level"] = "subgrp"
    did = etree.SubElement(c01, "did")
    unittitle = etree.SubElement(did, "unittitle")
    unittitle.text = unittitle_text
    physdesc = etree.SubElement(did, "physdesc")
    physdesc.attrib["altrender"] = "whole"
    extent = etree.SubElement(physdesc, "extent")
    extent.attrib["altrender"] = "materialtype spaceoccupied"
    extent.text = extent_text # <-- will need to be updated
    physfacet = etree.SubElement(physdesc, "physfacet")
    physfacet.text = physfacet_text # <-- will need to be updated
    scopecontent = etree.SubElement(c01, "scopecontent")
    p1 = etree.SubElement(scopecontent, "p")
    p1.text = scopecontent_p1_text # <-- will need to be updated
    p2 = etree.SubElement(scopecontent, "p")
    p2.text = scopecontent_p2_text
    
    return c01

def make_c02_series(unittitle_text, unitdate_text, scopecontent_p_text):
    c02 = etree.Element("c02")
    c02.attrib["level"] = "series"
    did = etree.SubElement(c02, "did")
    unittitle = etree.SubElement(did, "unittitle")
    unittitle.text = unittitle_text + ", "
    unitdate = etree.SubElement(unittitle, "unitdate")
    unitdate.text = unitdate_text
    unitdate.attrib["type"] = "inclusive"
    if "-" in unitdate_text:
        unitdate.attrib["normal"] = unitdate_text.replace("-", "/")
    else:
        unitdate.attrib["normal"] = unitdate_text
    scopecontent = etree.SubElement(c02, "scopecontent")
    scopecontent_p = etree.SubElement(scopecontent, "p")
    scopecontent_p.text = scopecontent_p_text
    
    return c02
    
new_digital_documents = make_c01_subgroup("Digital Documents", "5397 digital files", "393 MB", "There are 5397 digital files (393 MB) in the Digital Documents subgroup. At the time of the records accession to the Bentley Historical Library, the Macintosh operating system version 8.0 was in use. The original organization and arrangement of Duderstadt's digital files has been preserved. Duderstadt maintained seven archival directories: Speeches, Idea Files, Strategy, Position Papers, Presentations, Write Files, and Legacy. An additional series, Digital Images, was created when a collection of digital images of university building projects was accessioned to the collection early in 1998.", "The arrangement of files within each directory is chronological by date starting with the 1986-1987 school year. This arrangement was designed and used by Duderstadt in the Speeches, Idea Files, and Write Files series and extended to the remaining series except the Digital Images during the processing phase of the project. The directory naming scheme effectively describes the type of record contained within the directory. File names are also in most cases descriptive of the content, however, researchers should note that Duderstadt used personal last names, initials, abbreviations, and numerous acronyms in naming files. A list of commonly used acronyms and abbreviations used for file naming purposes can be found in the 'Additional Descriptive Data' section of the finding aid. Researcher's Note: The file-naming scheme also reveals the specific version of a particular document. Duderstadt maintained the file name for the record and added a sequence of numbers to the file name to indicate various versions. For example, the record 'Project Athena' progresses from Project Athena .92, Project Athena 1.0, 1.01, 1.2, 2.1, to Project Athena 2.21.")

new_digital_documents.append(make_c02_series("University of Michigan Presidency", "1986-1997", "Digital documents from Duderstadt's tenure as University President."))

new_digital_documents.append(make_c02_series("Faculty Archives", "1968-ongoing", "Includes speeches, presentations, writings and images. Portions of the collection are restricted. This collection represents the 'personal papers' of president Duderstadt."))

dsc = tree.xpath("/ead/archdesc[1]/dsc[1]")[0]
dsc.append(new_digital_documents)

ead_text = etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding="utf-8")

with open("C:\Users\eckardm\work-stuff\duderstadt\ead\duderst-updated.xml", mode="w") as f:
  f.write(ead_text)
  
def make_c03_series(unittitle_text, unitdate_text, extent_text, scopecontent_p1_text, scopecontent_p2_text):
    c03 = etree.Element("c03")
    c03.attrib["level"] = "series"
    did = etree.SubElement(c03, "did")
    unittitle = etree.SubElement(did, "unittitle")
    unittitle.text = unittitle_text + ", "
    unitdate = etree.SubElement(unittitle, "unitdate")
    unitdate.text = unitdate_text
    unitdate.attrib["type"] = "inclusive"
    if "-" in unitdate_text:
        unitdate.attrib["normal"] = unitdate_text.replace("-", "/")
    else:
        unitdate.attrib["normal"] = unitdate_text.replace("circa ", "")
    if unitdate_text.startswith("circa"):
        unitdate.attrib["certainty"] = "approximate"
    physdesc = etree.SubElement(did, "physdesc")
    physdesc.attrib["altrender"] = "whole"
    extent = etree.SubElement(physdesc, "extent")
    extent.attrib["altrender"] = "materialtype spaceoccupied"
    extent.text = extent_text # <-- will need to be updated
    scopecontent = etree.SubElement(c03, "scopecontent")
    scopecontent_p1 = etree.SubElement(scopecontent, "p")
    scopecontent_p1.text = scopecontent_p1_text # <-- will need to be updated
    if len(scopecontent_p2_text) > 0:
        scopecontent_p2 = etree.SubElement(scopecontent, "p")
        scopecontent_p2.text = scopecontent_p2_text
        
    return c03
        
university_of_michigan_presidency = [
    ("Speeches", "1986-1996", "821 digital files", "A main avenue President Duderstadt utilized as a means to communicate his ideas, objectives, and university strategic plan was to get out into the community and talk. During his presidency, Duderstadt frequently made several speeches a day to groups on campus and across the state, thus making the Speeches series (821 files, 1986-1996) the largest series in the Digital Documents subgroup. The early speech files from the years 1986 to 1992 were predominately composed using the MORE 3.1 outline program. However, after 1992 he drafted his speeches using a combination of MORE 3.1 and Microsoft Word 6.0. Major Speeches contained in this series include: The Cranbrook Address, The Challenge of K-12 Education, February, 1990, American Nuclear Society Keynote Address, A Future of Change, April, 1992, State Equity in Education Conference, The Michigan Mandate: A Progress Report, March, 1993, Vision 2017: The Third Century, November, 1993.", "Researchers should note that a list of key speeches by title, year, and location can be found in the digital file titled 'Accomplishments' located in the Strategy series. Also, note that several iterations of particular speeches can be found in the Digital Documents subgroup. Duderstadt's file naming scheme reflects the change in a file by a series of numbers located after the file name."),
    ("Idea Files", "1986-1995", "328 digital files", "The Idea Files series (328 digital files, 1986-1995) is comprised of files created with the MORE 3.1 outline program. Many of the outline files in this series resemble a silhouette of ideas that Duderstadt later developed into strategic planning documents, position papers, and speeches. Other outlines in the series read as talking points Duderstadt used either to prepare for a meeting or an important conversation. Major topics addressed in this series include higher education, teaching and research, information technology, and affirmative action. Yearly progress reports on the status of Duderstadt's agenda and goals can be found within this series in files with titles such as 'Summary 1991-92' or 'The Year Past.' Researchers interested in additional biographical material should consult the digital file 'Biography' in the 1988-1989 Ideas subseries and the Biographical series in the Paper Documents subgroup.", ""),
    ("Strategy", "1986-1997", "63 digital files", "While the other series in the Duderstadt Digital Documents subgroup contain records which cover a variety of topics, the Strategy series (84 files, 1986-1996) is largely focused on issues specifically related to President Duderstadt's vision of higher education in the 21st century. The framework for his position of the future of education can be found in two key documents: 'Vision 2000: The Leaders and Best' and 'Vision 2017: Transforming the University.'", "Duderstadt's espousal of the changing environment and the need for traditional institutions to transform is captured in this series. A researcher interested in his views on organizational change should look at the files containing the word transformation or variants with 'trans' such as, 'Transformation Text 1.6,' 'Trans Team 2.0,' and 'Trans Course 2.1.' For a summary of Duderstadt's major strategic initiatives, priorities for the coming decade, and views of changes needed in education, research, and diversity consult the file 'The Decade Report.' This report outlines major initiatives introduced to the university by Duderstadt such as the Institute for the Humanities, the Media Union, Institute of Molecular Medicine, and the Tauber Manufacturing Institute. The digital file titled 'Accomplishments,' written in the fall of 1995, provides a very informative outline of Duderstadt's priorities for the decade, accomplishments, projects (listed by year), strategic plan (Phases I, II, III), major papers, and selected speeches (listed by year). Lastly, this series contains in the 1996-1997 Strategy subseries the records related to Duderstadt's vision of 'The New University' and 'The Millennium Project.'"),
    ("Position Papers", "1986-1997", "140 digital files", "The Position Papers series (140 digital files, 1986-1997) contains Duderstadt's key addresses, white papers, planning documents, annual reports, and presidential essays. Major papers contained in this series include: 'The Michigan Mandate: A Strategic Linking of Academic Excellence and Social Diversity,' 'The Role of the Research University in Undergraduate Education,' 'Michigan's Challenge: Preparing for an Age of Knowledge,' 'The Michigan Agenda for Women: Toward a Full and Equal Partnership,' 'Intellectual Transformation.' A complete list of major position papers can be found in the digital file titled 'Accomplishments' located in the Strategy series. Researchers will note that several versions of a document are in the Digital Documents subgroup, and that Duderstadt used a numbering scheme to organize versions of an digital document. One example of his file naming scheme is a series of files from the 1991-1996 subseries entitled 'Women 3.2,' 'Women 3.3,' 'Women 3.4.'", ""),
    ("Presentations", "1987-1997", "64 digital files", "The majority of records in the Presentations series (64 digital files, 1987-1996) were created using the software application PowerPoint by Microsoft. This application was designed specifically as a presentation tool. Many of the records in this series seem to be presentations given to Duderstadt's Executive Officers (EOs) and the Regents at retreat meetings (for example, 'Regents Retreat,' 'Tuition Retreat,' 'Leadership Retreat'). Other presentation topics included in this series are The Michigan Mandate, The Mission Plan, and University Resources.", "Researchers will note that in the Digital Documents subgroup contextual and descriptive information such as audience, location, and exact date of the presentation or speech is not always explicit in the digital record."),
    ("Write Files", "1988-1997", "588 digital files", "The Write Files series (588 digital files, 1987-1997) is composed entirely of Microsoft Word text files. Researchers will find a variety of 'traditional' business formats such as correspondence, agendas, and memorandums contained within the Write Files series. However, note that there is often an absence of descriptive information, such as the receiver's name and address, date, and signature line. The absence of this information is a reflection of the distributive work process practiced in President Duderstadt's office--a process afforded by networked computer technology. The correspondence includes letters of recommendation, thank-you's, and communication to persons not only at the University of Michigan but to persons throughout the country including U.S. presidents Gerald Ford and George Bush and Michigan governors James Blanchard and John Engler. It is important to note that Duderstadt often used the recipient's name or initials to name the file. For example, 'Blanchard-1/89' and 'H & V-11/10' are communications to Governor James Blanchard in January 1989 and Harold and Vivian Shapiro on November 10th respectively.", ""),
    ("Legacy", "circa 1996", "36 digital files", "The Legacy Documents series (36 digital files, ca. 1996) contains the drafts of the digital records that resulted in a number of printed publications written by Duderstadt together entitled 'Legacy Documents.' The files in the 'Sunflower' sub-folder are those files that resulted in the publication entitled 'A Growing Season: A Report from the President . . .The University of Michigan, 1986-1996.' A complete set of printed 'Legacy' documents including 'A Growing Season...' is in the Paper Documents series Publications.", ""),
    ("Digital Images", "circa 1996", "55 digital files", "The Digital Images series (55 digital files, ca. 1996) provides a look at the many buildings either newly constructed or renovated during Duderstadt's presidential tenure at Michigan. The Ann Arbor campus underwent major changes to the Central, North, Athletic, and Medical campuses. New construction projects include the Media Union, Cancer &amp; Geriatrics Center, Medical Science Research Building, Lurie Engineering Center and Bell Tower, Donald Canham Natatorium, and the Glenn E. Schembechler Hall. Major renovation and improvement projects include Angell Hall, CC Little, Chemistry Building, and Health Service. Included in this series are images of the buildings constructed on the U-M Dearborn and Flint campuses. A complete listing of all construction and renovation projects is highlighted in a special booklet titled 'Rebuilding the University, The University of Michigan 1986-1996.' A copy of this document is in the Paper Documents series Publications.", "")
]

for unittitle_text, unitdate_text, extent_text, scopecontent_p1_text, scopecontent_p2_text in university_of_michigan_presidency:
    new_university_of_michigan_presidency = make_c03_series(unittitle_text, unitdate_text, extent_text, scopecontent_p1_text, scopecontent_p2_text)
    
    c02 = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]")[0]
    c02.append(new_university_of_michigan_presidency)

ead_text = etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding="utf-8")

with open("C:\Users\eckardm\work-stuff\duderstadt\ead\duderst-updated.xml", mode="w") as f:
    f.write(ead_text)
    
def make_c04_subseries(unittitle_text, extent_text, accessrestrict_bool):
    c04 = etree.Element("c04")
    c04.attrib["level"] = "subseries"
    did = etree.SubElement(c04, "did")
    physloc = etree.SubElement(did, "physloc")
    physloc.text = "Online"
    unittitle = etree.SubElement(did, "unittitle")
    unittitle.text = unittitle_text
    physdesc = etree.SubElement(did, "physdesc")
    physdesc.attrib["altrender"] = "whole"
    extent = etree.SubElement(physdesc, "extent")
    extent.attrib["altrender"] = "materialtype spaceoccupied"
    extent.text = extent_text # <-- will need to be updated'''
    if accessrestrict_bool == True:
        accessrestrict = etree.SubElement(c04, "accessrestrict")
        accessrestrict_p = etree.SubElement(accessrestrict, "p")
        accessrestrict_p.text = "ER RESTRICTED until "
        date = etree.SubElement(accessrestrict_p, "date")
        date.attrib["type"] = "restriction"
        date.attrib["normal"] = "2030-07-01"
        date.text = "July 1, 2030"
        
    return c04

speeches = [
    ("1986-1987 Speeches", "37 files", False), 
    ("1987-1988 Speeches", "54 files", False), 
    ("1988-1989 Speeches", "124 files", False), 
    ("1989-1990 Speeches", "132 files", False), 
    ("1990-1991 Speeches", "214 files", False), 
    ("1991-1992 Speeches", "52 files", False), 
    ("1992-1993 Speeches", "36 files", False), 
    ("1994-1995 Speeches", "27 files", False), 
    ("1995-1996 Speeches", "135 files", False), 
    ("Athletic Talks-Speeches", "12 files", False)
]

for unittitle_text, extent_text, accessrestrict_bool in speeches:
    new_speeches = make_c04_subseries(unittitle_text, extent_text, accessrestrict_bool)

    c02 = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]")[0]
    c02.append(new_speeches)

idea_files = [
    ("1986-1987 Ideas", "36 files", True), 
    ("1987-1988 Ideas", "28 files", True), 
    ("1988-1989 Ideas", "33 files", True), 
    ("1989-1990 Ideas", "47 files", True), 
    ("1990-1991 Ideas", "29 files", True), 
    ("1991-1992 Ideas", "20 files", True), 
    ("1992-1993 Ideas", "30 files", True), 
    ("1993-1994 Ideas", "57 files", True), 
    ("1994-1995 Ideas", "31 files", True)
]

for unittitle_text, extent_text, accessrestrict_bool in idea_files:
    new_idea_files = make_c04_subseries(unittitle_text, extent_text, accessrestrict_bool)

    c02 = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]")[0]
    c02.append(new_idea_files)

new_strategy = make_c04_subseries("1986-1997 Strategy", "63 files", True)

c02 = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[3]")[0]
c02.append(new_strategy)

position_papers = [
    ("1986-1991 Position Papers", "74 files", True), 
    ("1991-1996 Position Papers", "66 files", True), 
    ("1996-1997 Position Papers", "04 files", True)
]

for unittitle_text, extent_text, accessrestrict_bool in position_papers:
    new_position_papers = make_c04_subseries(unittitle_text, extent_text, accessrestrict_bool)

    c02 = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[4]")[0]
    c02.append(new_position_papers)

presentations = [
    ("1987-1988 Presentations", "1 file", False), 
    ("1988-1989 Presentations", "5 files", False), 
    ("1989-1990 Presentations", "8 files", False), 
    ("1990-1991 Presentations", "13 files", False), 
    ("1991-1992 Presentations", "17 files", False), 
    ("1992-1993 Presentations", "3 files", False), 
    ("1993-1994 Presentations", "1 file", False), 
    ("1994-1995 Presentations", "2 files", False), 
    ("1995-1996 Presentations", "3 files", False), 
    ("1996-1997 Presentations", "11 files", False)
]

for unittitle_text, extent_text, accessrestrict_bool in presentations:
    new_presentations = make_c04_subseries(unittitle_text, extent_text, accessrestrict_bool)

    c02 = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]")[0]
    c02.append(new_presentations)

write_files = [
    ("1988 and earlier Write Files", "19 files", True), 
    ("1988-1989 Write Files", "19 files", True), 
    ("1989-1990 Write Files", "50 files", True), 
    ("1990-1991 Write Files", "74 files", True), 
    ("1991-1992 Write Files", "54 files", True), 
    ("1992-1993 Write Files", "120 files", True), 
    ("1993-1994 Write Files", "114 files", True), 
    ("1994-1995 Write Files", "55 files", True), 
    ("1995-1996 Write Files", "75 files", True), 
    ("1996-1997 Write Files", "8 files", True)
]

for unittitle_text, extent_text, accessrestrict_bool in write_files:
    new_write_files = make_c04_subseries(unittitle_text, extent_text, accessrestrict_bool)

    c02 = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]")[0]
    c02.append(new_write_files)

new_legacy = make_c04_subseries(unittitle_text, extent_text, accessrestrict_bool)

c02 = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[7]")[0]
c02.append(new_legacy)

new_digital_images = make_c04_subseries(unittitle_text, extent_text, accessrestrict_bool)

c02 = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[8]")[0]
c02.append(new_digital_images)

ead_text = etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding="utf-8")

with open("C:\Users\eckardm\work-stuff\duderstadt\ead\duderst-updated.xml", mode="w") as f:
    f.write(ead_text)
    
def make_file(unittitle_text, unitdate_text, physfacet_text, dao_href_attrib, accessrestrict_bool):
    if unittitle_text.startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997"):
        c0x = etree.Element("c05")
    else:
        c0x = etree.Element("c03")
    c0x.attrib["level"] = "file"
    did = etree.SubElement(c0x, "did")
    physloc = etree.SubElement(did, "physloc")
    physloc.text = "Online"
    unittitle = etree.SubElement(did, "unittitle")
    unittitle.text = unittitle_text.decode("utf-8") + ", "
    unitdate = etree.SubElement(unittitle, "unitdate")
    unitdate.text = unitdate_text
    unitdate.attrib["type"] = "inclusive"
    unitdate.attrib["normal"] = unitdate_text  
    physdesc = etree.SubElement(did, "physdesc")
    physfacet = etree.SubElement(physdesc, "physfacet")
    physfacet.text = physfacet_text
    dao = etree.SubElement(did, "dao")
    dao.attrib["show"] = "new"
    dao.attrib["actuate"] = "onrequest"
    dao.attrib["href"] = dao_href_attrib
    daodesc = etree.SubElement(dao, "daodesc")
    daodesc_p = etree.SubElement(daodesc, "p")
    daodesc_p.text = "[view item]"
    if accessrestrict_bool == True:
        accessrestrict = etree.SubElement(c04, "accessrestrict")
        accessrestrict_p = etree.SubElement(accessrestrict_bool, "p")
        accessrestrict_p.text = "ER RESTRICTED until "
        date = etree.SubElement(accessrestrict_p, "date")
        date.attrib["type"] = "restriction"
        date.attrib["normal"] = "2030-07-01"
        date.text = "July 1, 2030"

    return c0x
    
metadata = pickle.load(open("metadata.p", mode="rb"))
sorted_metadata = sorted(metadata, key=itemgetter("unitdate"), reverse=False)

for sorted_metadatum in sorted_metadata:

    unittitle_text = sorted_metadatum["unittitle"]
    unitdate_text = sorted_metadatum["unitdate"]
    physfacet_text = sorted_metadatum["physfacet"]
    dao_href_attrib = sorted_metadatum["dao"]
    accessrestrict_bool = False
    if "accessrestrict" in sorted_metadatum:
        accessrestrict_bool = True
        
    new_file = make_file(unittitle_text, unitdate_text, physfacet_text, dao_href_attrib, accessrestrict_bool)
    
    if sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1986-1987 Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[1]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1987-1988 Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[2]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1988-1989 Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[3]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1989-1990 Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[4]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1990-1991 Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[5]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1991-1992 Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[6]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1992-1993 Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[7]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1994-1995 Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[8]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "1995-1996 Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[9]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Speeches" + " - " + "Athletic Talks-Speeches"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[1]/c04[10]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1986-1987 Ideas"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]/c04[1]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1987-1988 Ideas"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]/c04[2]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1988-1989 Ideas"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]/c04[3]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1989-1990 Ideas"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]/c04[4]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1990-1991 Ideas"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]/c04[5]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1991-1992 Ideas"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]/c04[6]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1992-1993 Ideas"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]/c04[7]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1993-1994 Ideas"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]/c04[8]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Idea Files" + " - " + "1994-1995 Ideas"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[2]/c04[9]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Strategy" + " - " + "1986-1997"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[3]/c04[1]")[0]
        
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Position Papers" + " - " + "1986-1991 Position Papers"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[4]/c04[1]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Position Papers" + " - " + "1991-1996 Position Papers"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[4]/c04[2]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Position Papers" + " - " + "1996-1997 Position Papers"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[4]/c04[3]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1987-1988 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[1]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1988-1989 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[2]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1989-1990 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[3]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1990-1991 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[4]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1991-1992 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[5]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1992-1993 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[6]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1993-1994 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[7]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1994-1995 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[8]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1995-1996 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[9]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Presentations" + " - " + "1996-1997 Presentations"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[5]/c04[10]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1988 and earlier 1988 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[1]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1988-1989 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[2]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1989-1990 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[3]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1990-1991 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[4]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1991-1992 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[5]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1992-1993 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[6]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1993-1994 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[7]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1994-1995 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[8]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1995-1996 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[9]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Write Files" + " - " + "1996-1997 Write Files"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[6]/c04[10]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Legacy" + " - " + "1996"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[7]/c04[1]")[0]
    
    elif sorted_metadatum["unittitle"].startswith("Digital Documents" + " - " + "University of Michigan Presidency, 1986-1997" + " - " + "Digital Images" + " - " + "1996"):
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[1]/c03[8]/c04[1]")[0]
    
    else:
        c0x = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[2]")[0]
        
    c0x.append(new_file)
    
ead_text = etree.tostring(tree, pretty_print=True, xml_declaration=True, encoding="utf-8")

with open("C:\Users\eckardm\work-stuff\duderstadt\ead\duderst-updated.xml", mode="w") as f:
    f.write(ead_text)
    