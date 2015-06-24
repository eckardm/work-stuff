import lxml
from lxml import etree as ET

def getunitdates(filename):
    unitdate_xpath = '//unitdate'
    tree = ET.parse(filename)
    unitdates = tree.xpath(unitdate_xpath)
    for i in unitdates:
        with open('dates.txt', 'a') as textfile:
            textfile.write(ET.tostring(i))
            
getunitdates('podcasts.xml')
getunitdates('reeltoreel.xml')
getunitdates('digitalvideo.xml')