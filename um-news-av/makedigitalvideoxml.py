'''
Here's the draft of the FA attached as well as the original metadata spreadsheets I gave Rob. The series that need to be addressed are:

  * Sound Materials - Audio Reel-to-Reel News Briefs (1975-1994)
  * Audio Podcasts (2006 - 2010)
  * Digital Video

For the podcasts and video, we want to keep:

  * Unit title
  * Unit date
  * Note field
  * Physical facet--file extension(s)

Let me know if you have any questions--thanks!

MIke'''

# import what we need
from lxml import etree as ET
import re

# where is the reel to reel text file?
digitalvideo_path = 'podcasts.txt'

# where is the output xml
digitalvideo_xml = 'digitalvideo.xml'

# create description of subordinate components
dsc = ET.Element('dsc')
dsc.set('type', 'combined')

# set up the c01
digitalvideo = open(digitalvideo_path, 'r')
c01 = ET.SubElement(dsc, 'c01')
c01.set('level', 'series')
did = ET.SubElement(c01, 'did')
unittitle = ET.SubElement(did, 'unittitle')
unittitle.text = 'Digital Video'

# go through the txt file
for line in digitalvideo:
    if '(' in line and ';' not in line and '(Cont.)' not in line:
        c02 = ET.SubElement(c01, 'co2')
        c02.set('level', 'subseries')
        did = ET.SubElement(c02, 'did')
        unittitle = ET.SubElement(did, 'unittitle')
        unittitle.text = line
    elif ';' in line:
        c03 = ET.SubElement(c02, 'c03')
        c03.set('level', 'file')
        did = ET.SubElement(c03, 'did')
        physloc = ET.SubElement(did, 'physloc')
        physloc.set('label', 'Box')
        physloc.text = 'Online'
        cells = line.split(';')
        unit_title = cells[0].strip()
        unittitle = ET.SubElement(did, 'unittitle')
        unittitle.text = unit_title
        unitdate = ET.SubElement(unittitle, 'unitdate')
        unitdate.set('type', 'inclusive')
        unit_date = cells[1].strip()
        unitdate.set('normal', unit_date)
        unitdate.text = unit_date
        physical_facet = cells[3][-4:]
        physdesc = ET.SubElement(did, 'physdesc')
        physfacet = ET.SubElement(physdesc, 'physfacet')
        physfacet.text = physical_facet
        handle = cells[6].strip()
        dao = ET.SubElement(did, 'dao')
        dao.set('href', handle)
        dao.set('show', 'new')
        dao.set('actuate', 'onrequest')
        daodesc = ET.SubElement(dao, 'daodesc')
        p = ET.SubElement(daodesc, 'p')
        p.text = '[view item]'
        note_field = cells[2].strip()
        odd = ET.SubElement(c03, 'odd')
        p = ET.SubElement(odd, 'p')
        p.text = note_field

xml = ET.tostring(dsc)  
with open(digitalvideo_xml, 'a') as xml_file:
   xml_file.write(xml)