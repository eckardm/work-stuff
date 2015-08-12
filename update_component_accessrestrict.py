import os
from os.path import join
from lxml import etree
from tqdm import *
import copy

ead_path = 'C:/Users/Public/Documents/Real_Masters_all'
# ead_path = 'C:/Users/eckardm/GitHub/vandura/Real_Masters_all'

accessrestrict_xpath = '/ead/archdesc/dsc//accessrestrict'

for filename in tqdm(os.listdir(ead_path)):
    if filename.endswith('.xml'):
        ead = filename
        print ead
        tree = etree.parse(join(ead_path, ead))
        for accessrestrict in tree.xpath(accessrestrict_xpath):
            
            
            
            
            
            access_restriction_xpath = tree.getpath(accessrestrict)
            component_xpath = access_restriction_xpath[:-15]
            container_xpath = access_restriction_xpath[:-14] + 'did/container'
            physloc_xpath = access_restriction_xpath[:-14] + 'did/physloc'
            if not tree.xpath(container_xpath) and not tree.xpath(physloc_xpath):
                for child in tree.xpath(component_xpath)[0].iter():
                    if child.tag.startswith('c0') and 'accessrestrict' not in child.getchildren():
                        print ead
                        print 'FOUND ONE'
                                # with open(os.path.join(ead_path, ead), mode="w") as f:
                                    # f.write(etree.tostring(tree, xml_declaration=True, encoding='utf-8', pretty_print=True))
    
                # if children.tag.startswith('c0') and not tree.xpath(container) and not tree.xpath(physloc):
                    # print children.tag, children.text
                 #   children.append(access_restriction)
                   # print tree.getpath(children)
                    #print 'wokred?'
                    # with open(os.path.join(ead_path, ead), mode="w") as f:
                        # f.write(etree.tostring(tree, xml_declaration=True, encoding='utf-8', pretty_print=True))
                    