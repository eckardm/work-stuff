import os
from openpyxl import load_workbook
from lxml import etree

'''
deposit_id = raw_input("Deposit ID: ")

source_directory = os.path.join("X:\deepblue", deposit_id)'''
target_directory = "S:\MLibrary\DeepBlue"
'''
# make working copy
os.putenv("SOURCE_DIRECTORY", source_directory)

os.makedirs(deposit_id)
os.putenv("TARGET_DIRECTORY", "C:\Users\eckardm\work-stuff\prep_deep_blue_deposit")

os.system("copy_with_teracopy.bat")

# make simple archive format
# make archive directory
os.rename(deposit_id, "archive_directory")'''

metadata = [filename for filename in os.listdir("archive_directory") if filename.startswith("deepBlue_")][0]

wb = load_workbook(filename=os.path.join("archive_directory", metadata), read_only=True, use_iterators=True)
ws = wb["Sheet1"]

counter = 1

for row in ws.iter_rows(row_offset=1):
    
    # make items
    item = "item_"
    number = str(counter).zfill(3)
    item = item + number
    counter += 1
    # os.makedirs(os.path.join("archive_directory", item))
    
    # make dublin core
    identifier_other = row[0].value
    dc_title = row[1].value
    dc_description_abstract = row[2].value
    dc_contributor_author = row[3].value
    dc_contributor_other = row[4].value
    dc_date_issued = str(row[5].value)
    dc_date_created = str(row[6].value)
    dc_coverage_temporal = row[7].value
    dc_title_filenames = row[8].value.split("|")
    dc_description_filenames = row[9].value.split("|")
    dc_type = row[10].value
    dc_rights_access = row[11].value
    dc_date_open = str(row[12].value)
    dc_rights_copyright = row[13].value
    dc_language_iso = row[14].value
    
    dublin_core = etree.Element("dublin_core")
    
    if identifier_other:
        etree.SubElement(dublin_core, "dcvalue", element="identifier", qualifier="other").text = identifier_other
    etree.SubElement(dublin_core, "dcvalue", element="title", qualifier="none").text = dc_title
    if dc_description_abstract:
        etree.SubElement(dublin_core, "dcvalue", element="description", qualifier="abstract").text = dc_description_abstract
    etree.SubElement(dublin_core, "dcvalue", element="contributor", qualifier="author").text = dc_contributor_author
    if dc_contributor_other:
        etree.SubElement(dublin_core, "dcvalue", element="contributor", qualifier="other").text = dc_contributor_other
    etree.SubElement(dublin_core, "dcvalue", element="date", qualifier="issued").text = dc_date_issued
    if dc_date_created:
        etree.SubElement(dublin_core, "dcvalue", element="date", qualifier="created").text = dc_date_created
    if dc_coverage_temporal:
        etree.SubElement(dublin_core, "dcvalue", element="coverage", qualifier="temporal").text = dc_coverage_temporal
    if dc_type:
        etree.SubElement(dublin_core, "dcvalue", element="type", qualifier="none").text = dc_type
    if dc_rights_access:
        etree.SubElement(dublin_core, "dcvalue", element="rights", qualifier="access").text = dc_rights_access
    if dc_date_open:
        etree.SubElement(dublin_core, "dcvalue", element="date", qualifier="open").text = dc_date_open
    if dc_rights_copyright:
        etree.SubElement(dublin_core, "dcvalue", element="rights", qualifier="copyright").text = dc_rights_copyright
    if dc_language_iso:
        etree.SubElement(dublin_core, "dcvalue", element="language", qualifier="iso").text = dc_language_iso
    
    dublin_core = etree.tostring(dublin_core, pretty_print=True, xml_declaration=True, encoding="utf-8", standalone=False)
    
    with open(os.path.join("archive_directory", item, "dublin_core.xml"), mode="w") as f:
        f.write(dublin_core)
        
    wb._archive.close()
    
    # make license
    with open(os.path.join("archive_directory", item, "license.txt"), mode="w") as f:
        f.write("As the designated coordinator for this Deep Blue Collection, I am authorized by the Community members to serve as their representative in all dealings with the Repository. As the designee, I ensure that I have read the Deep Blue policies. Furthermore, I have conveyed to the community the terms and conditions outlined in those policies, including the language of the standard deposit license quoted below and that the community members have granted me the authority to deposit content on their behalf.")
        
    # make contents
    with open(os.path.join("archive_directory", item, "contents"), mode="w") as f:
        f.write("license.txt\n")
        for dc_title_filename, dc_description_filename in zip(dc_title_filenames, dc_description_filenames):
            f.write(dc_title_filename + "\tdescription:" + dc_description_filename)
            if dc_rights_access.startswith("Reading room access only"):
                f.write("  Access restricted to Bentley.")
            f.write("\n")
    '''
    # move objects
    objects = [filename for filename in os.listdir("archive_directory") if not filename.startswith("deepBlue_") and not filename.startswith("item_")]
    
    for object in objects:
        if object in dc_title_filenames:
            
            os.putenv("SOURCE_DIRECTORY", os.path.join("archive_directory", object))
            os.putenv("TARGET_DIRECTORY", os.path.join("archive_directory", item))
            
            os.system("move_with_teracopy.bat")'''

# delete metadata
os.remove(os.path.join("archive_directory", metadata))
            