import os
import csv
import re
import time
import datetime

# write headers for metadata
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

# identify restricted files
restricted_files = []

for root, dirs, files in os.walk("C:\Users\eckardm\work-stuff\duderstadt\duderstadt"):
    for name in files:
        if "restricted" in root:
            restricted_files.append(name)

# identify converted files
converted_files = {}

with open("convertedFiles_9811_0003.csv", mode="rb") as converted_files_csv:
    reader = csv.reader(converted_files_csv)
    for row in reader:
        original_path = row[0].split("; ")[1].replace('"', "").strip()
        converted_path = row[0].split("; ")[2].replace('"', "").strip()
        converted_files[original_path] = converted_path

# get metadata
from metadata import metadata

# write metadata
'''
File Name | Author | Date of Publication or Speech | Title
----------|--------|-------------------------------|------'''

identifier_counter = 1

for root, dirs, files in os.walk("C:\Users\eckardm\work-stuff\duderstadt\9811_0003"):
    for name in files:
        if "_bhl-" not in name:
        
            if identifier_counter <= 99:
                identifier_other = "9811_0003_000" + str(identifier_counter)
            elif identifier_counter <= 999:
                identifier_other = "9811_0003_00" + str(identifier_counter)
            else:
                identifier_other = "9811_0003_0" + str(identifier_counter)
            identifier_counter += 1
            
            href = "../" + root.split("\\")[-2:][0] + "/" + root.split("\\")[-2:][1] + "/" + name
            for iter_var in metadata:
                if href == iter_var["href"]:
                    title = iter_var["title"]
                    date = iter_var["date"]
                    
            dc_title = title
            
            dc_description_abstract = ""
            
            dc_contributor_author = "Duderstadt, James J."
            
            dc_contributor_other = ""
            
            dc_date_issued = "2015"
            
            # does this need to be in YYYY-MM-DD format? i'm going to guess probably. what should get passed to finding aids?
            if "-" in date or date == "undated" or date == "1989":
                dc_date_created = date
            else:
                try:
                    dc_date_created = datetime.datetime.strptime(date, "%m/%d/%y")
                # maybe this is the best thing to do? can't tell how these are typos.
                except:
                    dc_date_created = datetime.datetime.strptime(date, "%d/%m/%y")
                dc_date_created = dc_date_created.strftime("%Y-%m-%d")
            
            dc_coverage_temporal = ""

            for iter_var in converted_files:
                if "\\".join(iter_var.split("\\")[4:]) == "\\".join(root.split("\\")[6:]) + "\\" + name:
                    dc_title_filename = name + " | " + str(converted_files[iter_var].split("\\")[:-1])
                    dc_description_filename = "Access version | Preservation version"
                else:
                    dc_title_filename = name
                    dc_description_filename = ""
            
            dc_type = "Office Documents"
            
            if name in restricted_files:
                dc_rights_access = "Closed for research use."
                dc_date_open = "2030-07-01"
            else:
                dc_rights_access = "Collection is open for research."
                # today's date?
                dc_date_open = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")
            
            dc_rights_copyright = "Copyright has been transferred to the Regents of the University of Michigan."
            
            # i think this is right.
            dc_language_iso = "en_US"
            
            with open("deepBlue_9811_0003.csv", mode="ab") as metadata_csv:
                writer = csv.writer(metadata_csv)
                writer.writerow([identifier_other, dc_title, dc_description_abstract, dc_contributor_author, dc_contributor_other, dc_date_issued, dc_date_created, dc_coverage_temporal, dc_title_filename, dc_description_filename, dc_description_filename, dc_type, dc_rights_access, dc_date_open, dc_rights_copyright, dc_language_iso])
