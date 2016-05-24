import os
from tqdm import *
from lxml import etree
from time import strptime, strftime
import shutil

source_directory = os.path.join("reel-to-reel_test")
target_directory = os.path.join("S:", "MLibrary", "DeepBlue", "reel-to-reel_test")

metadata = [filename for filename in os.listdir(source_directory) if filename.endswith(".xml")]
    
for metadatum in tqdm(metadata):

    tree = etree.parse(os.path.join(source_directory, metadatum))
    
    # make collection
    collection = "archive_dir_2027-42_" + tree.xpath("//parent_collection")[0].text.split("/")[1] + "-BentleyStaff"
    
    if collection not in os.listdir(target_directory):
        os.makedirs(os.path.join(target_directory, collection))
    
    # make item
    item = tree.xpath("//dc.identifier.other")[0].text
    os.makedirs(os.path.join(target_directory, collection, item))
    
    # license
    with open(os.path.join(target_directory, collection, item, "license.txt"), mode="w") as f:
        
        f.write("As the designated coordinator for this Deep Blue Collection, I am authorized by the Community members to serve as their representative in all dealings with the Repository. As the designee, I ensure that I have read the Deep Blue policies. Furthermore, I have conveyed to the community the terms and conditions outlined in those policies, including the language of the standard deposit license quoted below and that the community members have granted me the authority to deposit content on their behalf.\n")
        
    # contents
    bitstreams = tree.xpath("//bitstream")
    with open(os.path.join(target_directory, collection, item, "contents"), mode="w") as f:
        f.write("license.txt\n")
        for bitstream in bitstreams:
            filename = bitstream.xpath("dc.title.filename")[0].text
            f.write(filename)
            f.write("\tdescription:" + bitstream.xpath("dc.description.filename")[0].text + ". Access restricted to Bentley staff.")
            f.write("\tpermissions:-r 'BentleyStaff'\n")
            '''
            # copy files
            shutil.copyfile(os.path.join(source_directory, item, filename), os.path.join(target_directory, collection, item, filename))'''
    
    # dublin core
    dublin_core = tree
    
    dublin_core.xpath("//audio_item")[0].tag = "dublin_core"
    
    # this is no longer useful
    parent_collection = dublin_core.xpath("//parent_collection")[0]
    parent_collection.getparent().remove(parent_collection)
    
    # don't need these since they are restricted pretty much indefinitely
    dc_date_open = dublin_core.xpath("//dc.date.open")[0]
    dc_date_open.getparent().remove(dc_date_open)
    
    # needs to be iso format
    dc_date_created = dublin_core.xpath("//dc.date.created")[0]
    dc_date_created.text = strftime("%Y-%m-%d", strptime(dc_date_created.text, "%m/%d/%Y"))
    
    # gets added automatically
    dc_owningcollname = dublin_core.xpath("//dc.owningcollname")[0]
    dc_owningcollname.getparent().remove(dc_owningcollname)
    
    # jim prefers it if handles are added this way
    dc_description = dublin_core.xpath("//dc.description")[0]
    dc_description.text = dc_description.text.replace("http://deepblue.lib.umich.edu/handle/2027.42/108126", "http://hdl.handle.net/2027.42/108126")
    
    videostreams = dublin_core.xpath("//dc.identifier.videostream")
    for videostream in videostreams:
        dc_identifier_videostream = etree.Element("dc.identifier.videostream")
        dc_identifier_videostream.text = videostream.text
        dublin_core.xpath("//dublin_core")[0].append(dc_identifier_videostream)
        
    bitstreams = dublin_core.xpath("//bitstream")
    for bitstream in bitstreams:
        bitstream.getparent().remove(bitstream)
        
    dc_elements = dublin_core.xpath("//dublin_core/*")
    for dc_element in dc_elements:
        dc_element.attrib["element"] = dc_element.tag.split(".")[1]
        
        if dc_element.tag == "dc.abstract":
            dc_element.attrib["element"] = "description"
            dc_element.attrib["qualifier"] = "abstract"
            
        elif len(dc_element.tag.split(".")) == 3:
            dc_element.attrib["qualifier"] = dc_element.tag.split(".")[2]
        else:
            dc_element.attrib["qualifier"] = "none"
        dc_element.tag = "dcvalue"
    
    with open(os.path.join(target_directory, collection, item, "dublin_core.xml"), mode="w") as f:
        f.write(etree.tostring(dublin_core, pretty_print=True, xml_declaration=True, encoding='utf-8', standalone=False))
