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
podcasts_path = 'podcasts.txt'

# where is the output xml
podcasts_xml = 'podcasts.xml'

# create description of subordinate components
dsc = ET.Element('dsc')
dsc.set('type', 'combined')

# go through the txt file
podcasts = open(podcasts_path, 'r')
for line in podcasts:
    if line.startswith('Audio Podcasts') and '(Cont.)' not in line:
        c01 = ET.SubElement(dsc, 'c01')
        c01.set('level', 'series')
        did = ET.SubElement(c01, 'did')
        unittitle = ET.SubElement(did, 'unittitle')
        unittitle.text = line
    elif line.startswith('Podcasts') and '(Cont.)' not in line:
        c02 = ET.SubElement(c01, 'c02')
        c02.set('level', 'subseries')
        did = ET.SubElement(c02, 'did')
        unittitle = ET.SubElement(did, 'unittitle')
        unitdate = ET.SubElement(unittitle, 'unitdate')
        contents_of_parenthesis_matches = re.findall('(?<=\()(.*?)(?=\))', line)
        for contents_of_parenthesis_match in contents_of_parenthesis_matches:
            contents = contents_of_parenthesis_match
        unitdate.text = contents
        unitdate.set('type', 'inclusive')
        if unitdate.text == 'Undated':
            continue
        else:
            normal = unitdate.text
        unitdate.set('normal', normal)
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
        unitdate.text = unit_date
        year_matches = re.findall('\d{4}', unit_date)
        for year_match in year_matches:
            year = year_match
        month_matches = re.findall('^\d\d?', unit_date)
        for month_match in month_matches:
            if len(month_match) == 1:
                month = '0' + str(month_match)
            else:
                month = str(month_match)
        day_matches = re.findall('(?<=\/)(.*?)(?=\/)', unit_date)
        for day_match in day_matches:
            if len(day_match) == 1:
                day = '0' + str(day_match)
            else:
                day = str(day_match)
        if unitdate.text == 'Undated':
            continue
        else:
            normal = str(year) + '-' + month + '-' + str(day)
        unitdate.set('normal', normal)
        physical_facet = cells[3][-4:]
        physdesc = ET.SubElement(did, 'physdesc')
        physfacet = ET.SubElement(physdesc, 'physfacet')
        physfacet.text = '(' + physical_facet + ' file)'
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
with open(podcasts_xml, 'a') as xml_file:
   xml_file.write(xml)