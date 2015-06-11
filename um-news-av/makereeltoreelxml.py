'''Here's the draft of the FA attached as well as the original metadata spreadsheets I gave Rob. The series that need to be addressed are:

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
reel_to_reel_path = 'reeltoreel.txt'

# where is the output xml
reel_to_reel_xml = 'reeltoreel.xml'

# create description of subordinate components
dsc = ET.Element('dsc')
dsc.set('type', 'combined')

# dictionary for months
months = {
    'January': '01',
    'Jan': '01',
    'February': '02',
    'Feb': '02',
    'March': '03',
    'Mar': '03',
    'April': '04',
    'Apr': '04',
    'May': '05',
    'June': '06',
    'Jun': '06',
    'July': '07',
    'Jul': '07',
    'August': '08',
    'Aug': '08',
    'September': '09',
    'Sep': '09',
    'October': '10',
    'Oct': '10',
    'November': '11',
    'Nov': '11',
    'December': '12',
    'Dec': '12',
    'january': '01',
    'jan': '01',
    'february': '02',
    'feb': '02',
    'march': '03',
    'mar': '03',
    'april': '04',
    'apr': '04',
    'may': '05',
    'june': '06',
    'jun': '06',
    'july': '07',
    'jul': '07',
    'august': '08',
    'aug': '08',
    'september': '09',
    'sep': '09',
    'october': '10',
    'oct': '10',
    'november': '11',
    'nov': '11',
    'december': '12',
    'dec': '12'
}

# go through the txt file
reel_to_reel = open(reel_to_reel_path, 'r')
for line in reel_to_reel:
    if line.startswith('Audio Reel-to-Reel News Briefs') and '(Cont.)' not in line:
        c02 = ET.SubElement(dsc, 'c02')
        c02.set('level', 'subseries')
        did = ET.SubElement(c02, 'did')
        unittitle = ET.SubElement(did, 'unittitle')
        unittitle.text = line
    elif line.startswith('Box') and '(Cont.)' not in line:
        box_number = str(line[4])
    elif line.startswith('News Briefs'):
        c03 = ET.SubElement(c02, 'c03')
        c03.set('level', 'file')
        did = ET.SubElement(c03, 'did')
        container = ET.SubElement(did, 'container')
        container.set('type', 'box')
        container.set('label', 'Box')
        container.text = box_number
        unittitle = ET.SubElement(did, 'unittitle')
        unitdate = ET.SubElement(unittitle, 'unitdate')
        unitdate.set('type', 'inclusive')
        unitdate_matches = re.findall('(?<=News Briefs )(.*?)(?=:)', line)
        for unitdate_match in unitdate_matches:
            unitdate_text = unitdate_match.replace(' (5 inch reel)', '') # <-- where should this information go?
            if unitdate_text == "Fall 1975": # <-- is this the best way to do this?
                unitdate.set('normal', '1975-09/1975-12')
                unitdate.set('certainty', 'approximate')
            elif '-' in unitdate_text:
                year_begin_matches = re.findall('\d{4}', unitdate_text)
                for year_begin_match in year_begin_matches:
                    year_begin = year_begin_match
                month_begin_matches = re.findall('[A-Za-z]+', unitdate_text)
                for month_begin_match in month_begin_matches:
                    month_begin = months[month_begin_match]
                day_begin_matches = re.findall('\d\d?', unitdate_text)
                for day_begin_match in day_begin_matches:
                    day_begin = day_begin_match
                year_end_matches = re.findall('\d{4}$', unitdate_text)
                for year_end_match in year_end_matches:
                    year_end = year_end_match
                month_end_matches = re.findall('(?<=\-\s\d\s)([A-Za-z]+)', unitdate_text)
                if not month_end_matches:
                    month_end_matches = re.findall('(?<=\-\s\d\d\s)([A-Za-z]+)', unitdate_text)
                    for month_end_match in month_end_matches:
                        month_end = months[month_end_match]
                else:
                    for month_end_match in month_end_matches:
                        month_end = months[month_end_match]
                day_end_matches = re.findall('(?<=\-\s)\d\d?', unitdate_text)
                for day_end_match in day_end_matches:
                    day_end = day_end_match
                normal = str(year_begin) + '-' + month_begin + '-' + str(day_begin) + '/' + str(year_end) + '-' + month_end + '-' + str(day_end)
                unitdate.set('normal', normal)
            else:
                year_matches = re.findall('\d{4}', unitdate_text)
                for year_match in year_matches:
                    year = year_match
                month_matches = re.findall('[A-Za-z]+', unitdate_text)
                for month_match in month_matches:
                    month = months[month_match]
                day_matches = re.findall('\d\d?', unitdate_text)
                for day_match in day_matches:
                    day = day_match
                normal = str(year) + '-' + month + '-' + str(day)
                unitdate.set('normal', normal)
            unitdate.text = unitdate_text
        odd = ET.SubElement(c03, 'odd')
        p = ET. SubElement(odd, 'p')
        p_matches = re.findall('(?<=\:\s)(.*)', line)
        for p_match in p_matches:
            p.text = p_match
            
    
# print the xml
xml = ET.tostring(dsc)  
with open(reel_to_reel_xml, 'a') as xml_file:
   xml_file.write(xml)