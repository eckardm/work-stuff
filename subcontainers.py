import os
import csv
from lxml import etree

ead_path = r'C:\Users\eckardm\vandura\Real_Masters_all'

eads = [ead for ead in os.listdir(ead_path) if ead.endswith(".xml")]

for ead in eads:
    tree = etree.parse(os.path.join(ead_path, ead))
    containers = tree.xpath('//did/container[3]')
    for container in containers:
        xpath = tree.getpath(container)
        attribute = container.attrib.get('type', "")
        with open('subcontainer3.csv', 'ab') as subcontainer_csv:
            writer = csv.writer(subcontainer_csv)
            writer.writerow([ead, xpath, attribute])
        