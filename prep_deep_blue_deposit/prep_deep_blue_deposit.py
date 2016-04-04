import os
from openpyxl import load_workbook
from collections import Counter
from pprint import pprint
from lxml import etree
from time import strftime
import shutil

# preliminaries
def get_deposit_id():
    while True:
        deposit_id = raw_input("Deposit ID: ")
        if deposit_id in os.listdir("X:\deepblue"):
            break
        print "Enter a valid Deposit ID."
    return deposit_id
    
deposit_id = get_deposit_id()

source_directory = os.path.join("X:\deepblue", deposit_id)
temporary_directory = "archive_directory"
target_directory = "S:\MLibrary\DeepBlue"

# basic check on metadata
def get_dc_titles_and_dc_description_abstracts(directory):
    metadata = [filename for filename in os.listdir(directory) if filename.startswith("deepBlue_")][0]

    dc_titles = []
    dc_description_abstracts = []

    wb = load_workbook(filename=os.path.join(directory, metadata), read_only=True, use_iterators=True)
    ws = wb.active

    for row in ws.iter_rows(row_offset=1):
        dc_titles.append(row[1].value)
        dc_description_abstracts.append(row[2].value)
        
    return dc_titles, dc_description_abstracts
    
def get_filenames_and_dc_title_filenames(directory):
    filenames = []
    dc_title_filenames = []

    for filename in os.listdir(directory):
        if filename != "Thumbs.db" and not filename.startswith("deepBlue_"):
            filenames.append(filename)
            
    metadata = [filename for filename in os.listdir(directory) if filename.startswith("deepBlue_")][0]
            
    wb = load_workbook(filename=os.path.join(directory, metadata), read_only=True, use_iterators=True)
    ws = wb.active

    for row in ws.iter_rows(row_offset=1):
        for title in row[8].value.split("|"):
            dc_title_filenames.append(title)
        
    return filenames, dc_title_filenames

# unique title check
def check_that_dc_titles_are_unique(dc_titles):
    if len(dc_titles) != len(set(dc_titles)):
        print "All titles not unique..."
        print pprint(Counter(dc_titles).most_common())
        quit()

# unique description check
def check_that_dc_description_abstracts_are_unique(dc_description_abstracts):
    if len(dc_description_abstracts) != len(set(dc_description_abstracts)):
        print "All descriptions not unique..."   
        print pprint(Counter(dc_description_abstracts).most_common())
        quit()

# filenames and filenames in metadata check
def check_that_filenames_match_dc_title_filenames(filenames, dc_title_filenames):
    filenames_not_in_filenames_in_metadata = []

    for filename in filenames:
        if filename not in dc_title_filenames:
            filenames_not_in_filenames_in_metadata.append(filename)
            
    if len(filenames_not_in_filenames_in_metadata) > 0:
        print "All filenames and filenames in metadata do not match..."
        for filename in filenames_not_in_filenames_in_metadata:
            print filename
        quit()
        
def basic_metadata_check(directory):
    dc_titles, dc_description_abstracts = get_dc_titles_and_dc_description_abstracts(directory)
    check_that_dc_titles_are_unique(dc_titles)
    check_that_dc_description_abstracts_are_unique(dc_description_abstracts)
    
    filenames, dc_title_filenames = get_filenames_and_dc_title_filenames(directory)
    check_that_filenames_match_dc_title_filenames(filenames, dc_title_filenames)
    
basic_metadata_check(source_directory)

# make working copy
os.putenv("SOURCE_DIRECTORY", source_directory)

os.makedirs(deposit_id)
os.putenv("TARGET_DIRECTORY", os.path.dirname(os.path.abspath(__file__)))

os.system("copy_with_teracopy.bat")

# make simple archive format
# make archive directory
os.rename(deposit_id, temporary_directory)

wb = load_workbook(filename=os.path.join(temporary_directory, metadata), read_only=True, use_iterators=True)
ws = wb.active

counter = 1

for row in ws.iter_rows(row_offset=1):
    
    # make items
    item = "item_"
    number = str(counter).zfill(3)
    item = item + number
    counter += 1
    os.makedirs(os.path.join(temporary_directory, item))
    
    # make dublin core
    dublin_core = etree.Element("dublin_core")
    
    identifier_other = row[0].value
    if identifier_other:
        etree.SubElement(dublin_core, "dcvalue", element="identifier", qualifier="other").text = identifier_other
    
    dc_title = row[1].value
    etree.SubElement(dublin_core, "dcvalue", element="title", qualifier="none").text = dc_title
    
    dc_description_abstract = row[2].value
    if dc_description_abstract:
        etree.SubElement(dublin_core, "dcvalue", element="description", qualifier="abstract").text = dc_description_abstract
    
    dc_contributor_authors = row[3].value.split("|")
    for dc_contributor_author in dc_contributor_authors:
        etree.SubElement(dublin_core, "dcvalue", element="contributor", qualifier="author").text = dc_contributor_author
        
    if row[4].value:
        dc_contributor_others = row[4].value.split("|")
        for dc_contributor_other in dc_contributor_authors:
            etree.SubElement(dublin_core, "dcvalue", element="contributor", qualifier="other").text = dc_contributor_other
        
    dc_date_issued = str(row[5].value)
    etree.SubElement(dublin_core, "dcvalue", element="date", qualifier="issued").text = dc_date_issued
    
    dc_date_created = str(row[6].value)
    if dc_date_created:
        etree.SubElement(dublin_core, "dcvalue", element="date", qualifier="created").text = dc_date_created
        
    dc_coverage_temporal = row[7].value
    if dc_coverage_temporal:
        etree.SubElement(dublin_core, "dcvalue", element="coverage", qualifier="temporal").text = dc_coverage_temporal
    
    dc_title_filenames = row[8].value.split("|")
    
    if row[9].value:
        dc_description_filenames = row[9].value.split("|")
    
    if row[10].value:
        dc_types = row[10].value.split("| ")
        for dc_type in dc_types:
            etree.SubElement(dublin_core, "dcvalue", element="type", qualifier="none").text = dc_type

    dc_rights_access = row[11].value
    if dc_rights_access:
        etree.SubElement(dublin_core, "dcvalue", element="rights", qualifier="access").text = dc_rights_access
    
    dc_date_open = row[12].value.strftime("%Y-%m-%d")
    if dc_date_open:
        etree.SubElement(dublin_core, "dcvalue", element="date", qualifier="open").text = dc_date_open
    
    dc_rights_copyright = row[13].value
    if dc_rights_copyright:
        etree.SubElement(dublin_core, "dcvalue", element="rights", qualifier="copyright").text = dc_rights_copyright
    
    dc_language_iso = row[14].value
    if dc_language_iso:
        etree.SubElement(dublin_core, "dcvalue", element="language", qualifier="iso").text = dc_language_iso
    
    dublin_core = etree.tostring(dublin_core, pretty_print=True, xml_declaration=True, encoding="utf-8", standalone=False)
    
    with open(os.path.join(temporary_directory, item, "dublin_core.xml"), mode="w") as f:
        f.write(dublin_core)
        
    wb._archive.close()
    
    # make license
    with open(os.path.join(temporary_directory, item, "license.txt"), mode="w") as f:
        f.write("As the designated coordinator for this Deep Blue Collection, I am authorized by the Community members to serve as their representative in all dealings with the Repository. As the designee, I ensure that I have read the Deep Blue policies. Furthermore, I have conveyed to the community the terms and conditions outlined in those policies, including the language of the standard deposit license quoted below and that the community members have granted me the authority to deposit content on their behalf.")
        f.write("\n")
        
    # make contents
    with open(os.path.join(temporary_directory, item, "contents"), mode="w") as f:
        f.write("license.txt\n")
        for dc_title_filename, dc_description_filename in zip(dc_title_filenames, dc_description_filenames):
            f.write(dc_title_filename + "\tdescription:" + dc_description_filename)
            
            if dc_rights_access.startswith("This content is open for research"):
                f.write("\tpermissions:Anonymous")
            elif dc_rights_access.startswith("Reading room access only"):
                f.write(" Access restricted to Bentley.")
                f.write("\tpermissions:Bentley Only Users")
            else:
                print "Check out the permissions on these... looks like they're complicated."
                print dc_rights_access
                quit()
                
            f.write("\n")
    
    # move objects
    objects = [filename for filename in os.listdir(temporary_directory) if not filename.startswith("deepBlue_") and not filename.startswith("item_")]
    
    for object in objects:
        if object in dc_title_filenames:
            
            os.putenv("SOURCE_DIRECTORY", os.path.join(temporary_directory, object))
            os.putenv("TARGET_DIRECTORY", os.path.join(temporary_directory, item))
            
            os.system("move_with_teracopy.bat")

# delete metadata
os.remove(os.path.join(temporary_directory, metadata))

# move temporary directory to target directory
os.makedirs(os.path.join(target_directory, deposit_id))

os.putenv("SOURCE_DIRECTORY", os.path.join(os.path.dirname(os.path.abspath(__file__)), temporary_directory))
os.putenv("TARGET_DIRECTORY", os.path.join(target_directory, deposit_id))

# delete temporary location
os.system("move_with_teracopy.bat")
shutil.rmtree(temporary_directory)
