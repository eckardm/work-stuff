import os
import csv
import re
import time
import datetime
from fuzzywuzzy import fuzz, process

# write headers for metadata
with open("deepBlue_9811_0003-TEMP.csv", mode="wb") as metadata_csv:
    writer = csv.writer(metadata_csv)
    writer.writerow([
    "IDENTIFIER.OTHER", 
    "DC.TITLE", 
    "DC.DESCRIPTION.ABSTRACT", 
    "DC.CONTRIBUTOR.AUTHOR", 
    "DC.CONTRIBUTOR.OTHER", 
    "DC.DATE.ISSUED", 
    "DC.DATE.CREATED", 
    "DC.COVERAGE.TEMPORAL", 
    "DC.TITLE.FILENAME ", 
    "DC.DESCRIPTION.FILENAME", 
    "DC.TYPE", 
    "DC.RIGHTS.ACCESS", 
    "DC.DATE.OPEN", 
    "DC.RIGHTS.COPYRIGHT", 
    "DC.LANGUAGE.ISO"
])

with open("deepBlue_9811_0003.csv", mode="wb") as metadata_csv:
    writer = csv.writer(metadata_csv)
    writer.writerow([
    "IDENTIFIER.OTHER", 
    "DC.TITLE", 
    "DC.DESCRIPTION.ABSTRACT", 
    "DC.CONTRIBUTOR.AUTHOR", 
    "DC.CONTRIBUTOR.OTHER", 
    "DC.DATE.ISSUED", 
    "DC.DATE.CREATED", 
    "DC.COVERAGE.TEMPORAL", 
    "DC.TITLE.FILENAME ", 
    "DC.DESCRIPTION.FILENAME", 
    "DC.TYPE", 
    "DC.RIGHTS.ACCESS", 
    "DC.DATE.OPEN", 
    "DC.RIGHTS.COPYRIGHT", 
    "DC.LANGUAGE.ISO"
])

# identify converted files
converted_files = {}

with open("convertedFiles_9811_0003.csv", mode="rb") as converted_files_csv:
    reader = csv.reader(converted_files_csv)
    for row in reader:
        split_data = row[0].split("; ")
        
        original_path = split_data[1].strip('" ')
        converted_path = split_data[2].strip('" ')
        
        converted_files[original_path] = converted_path

# get metadata
from metadata import metadata

# write metadata
identifier_counter = 1

for _, _, files in os.walk("C:\Users\eckardm\work-stuff\duderstadt\9811_0003"):
    for name in files:
        if "_bhl-" in name:
            continue
        
        base_string = "9811_0003_"
        number = str(identifier_counter).zfill(4)
        identifier_other = base_string + number
        identifier_counter += 1
        
        dc_title = ""
        
        dc_date_created = ""
        
        href = "../" + "/".join(name.split("-"))
        for dct in metadata:
            if dct["href"] == href:
                dc_title = dct["title"]
                dc_date_created = dct["date"]
        
                # does this need to be in YYYY-MM-DD format? i'm going to guess probably. what should get passed to finding aids?
                if not dc_date_created:
                    continue
                if "-" in dc_date_created or dc_date_created == "undated" or dc_date_created == "1989":
                    continue
                try:
                    dc_date_created = datetime.datetime.strptime(dc_date_created, "%m/%d/%y")
                # maybe this is the best thing to do? can't tell how these are typos.
                except:
                    dc_date_created = datetime.datetime.strptime(dc_date_created, "%d/%m/%y")
                dc_date_created = dc_date_created.strftime("%Y-%m-%d")
                
                
        dc_description_abstract = ""
        
        dc_contributor_author = "Duderstadt, James J."
        
        dc_contributor_other = ""
        
        dc_date_issued = "2015"
        
        dc_coverage_temporal = ""
        
        dc_title_filename = name
        
        dc_description_filename = ""
        
        for original_path in converted_files:
            converted_file_sub_path = "\\".join(original_path.split("\\")[4:])
            current_sub_path = "\\".join(name.split("-"))
            if converted_file_sub_path == current_sub_path:
                dc_title_filename = name + " | " + "-".join(converted_files[original_path].split("\\")[4:])
                dc_description_filename = "Access version | Preservation version"
        
        dc_type = "Office Documents"
        
        # identify restricted files
        if "restricted" in name:
            dc_rights_access = "[ER Restricted until July 1, 2030]"
            dc_date_open = "2030-07-01"
        else:
            dc_rights_access = "Collection is open for research."
            # today's date?
            dc_date_open = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
        
        dc_rights_copyright = "Copyright has been transferred to the Regents of the University of Michigan."
        
        # i think this is right.
        dc_language_iso = "en_US"
        
        with open("deepBlue_9811_0003-TEMP.csv", mode="ab") as metadata_csv:
            writer = csv.writer(metadata_csv)
            writer.writerow([
                identifier_other, 
                dc_title, 
                dc_description_abstract, 
                dc_contributor_author, 
                dc_contributor_other, 
                dc_date_issued, 
                dc_date_created, 
                dc_coverage_temporal, 
                dc_title_filename, 
                dc_description_filename, 
                dc_type, 
                dc_rights_access, 
                dc_date_open, 
                dc_rights_copyright, 
                dc_language_iso])