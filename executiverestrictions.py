import lxml
from lxml import etree
import os
from os.path import join
import csv
import re

# where are the eads?
ead_path = 'S:/Curation/Projects/Mellon/ArchivesSpace/ATeam_Migration/EADs/Real_Masters_all'

# where is the output csv
csv_path = 'C:/Users/Public/Documents/executiverestrictions.csv'

with open(csv_path, 'ab') as csv_file:
    writer = csv.writer(csv_file, dialect='excel')
    writer.writerow(['Filename', 'XPath', 'Title', 'Series', 'Component Title', 'Access Restriction', 'ER Restricted Until...'])

eads = re.compile('\.xml$')
exec_restrict = re.compile('^\[?ER')

counter = 0

accessrestrict_xpath = '//accessrestrict/p'

for filename in os.listdir(ead_path):
    if eads.search(filename):
        print 'Processing ' + filename
        ead_tree = etree.parse(join(ead_path, filename))
        accessrestrict = ead_tree.xpath(accessrestrict_xpath)
        for a in accessrestrict:
            try:
                if exec_restrict.search(a.text):
                    exec_restrict_xpath = ead_tree.getpath(a)
                    exec_restrict_text = etree.tostring(a).replace('\n', '')
                    exec_restrict_text = re.sub('<.*?>', '', exec_restrict_text).strip()
                    print 'Processing ' + exec_restrict_text + ' at ' + exec_restrict_xpath
                    counter += 1
                    # get title
                    titleproper_xpath = '//eadheader/filedesc/titlestmt/titleproper'
                    titleproper = ead_tree.xpath(titleproper_xpath)
                    titleproper_text = titleproper[0].text.replace('\n', '')
                    print 'TITLE: ' + titleproper_text
                    # get series
                    series_xpath = "//dsc//*[starts-with(local-name(), 'c0')][@level='series']"
                    series = ead_tree.xpath(series_xpath)
                    for s in series:
                        if ead_tree.getpath(s) in exec_restrict_xpath:
                            unittitle_xpath = ead_tree.getpath(s) + '/did/unittitle'
                            unittitle = ead_tree.xpath(unittitle_xpath)
                            unittitle_text = etree.tostring(unittitle[0]).replace('\n', '')
                            unittitle_text = re.sub('<.*?>', '', unittitle_text).strip()
                            print 'SERIES: ' + str(unittitle_text)
                    # get component title
                    component_title_xpath = exec_restrict_xpath[:-17] + '/did/unittitle'
                    component_title = ead_tree.xpath(component_title_xpath)
                    component_title_text = etree.tostring(component_title[0]).replace('\n', '')
                    component_title_text = re.sub('<.*?>', '', component_title_text).strip()
                    print 'COMPONENT TITLE: ' + component_title_text
                    # get end date
                    exec_restrictions_date_xpath = exec_restrict_xpath + '/date'
                    exec_restrictions_date = ead_tree.xpath(exec_restrictions_date_xpath)
                    normalized_date = exec_restrictions_date[0].attrib
                    normalized_date_text = normalized_date.get('normal')
                    print 'NORMALIZED DATE: ' + normalized_date_text
                    with open(csv_path, 'ab') as csvfile:
                        writer = csv.writer(csvfile, dialect='excel')
                        writer.writerow([filename, exec_restrict_xpath, titleproper_text, str(unittitle_text), component_title_text, exec_restrict_text, normalized_date_text])
            except:
                continue
                
        
print 'Found ' + str(counter) + ' executive restrictions'