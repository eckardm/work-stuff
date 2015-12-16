import csv
import cPickle as pickle
import os
import datetime

# write headers for metadata
with open("deepBlue_9811_0001.csv", mode="wb") as metadata_csv:
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
    "RELATIVE_PATH",
    "DC.DESCRIPTION.FILENAME", 
    "DC.TYPE", 
    "DC.RIGHTS.ACCESS", 
    "DC.DATE.OPEN", 
    "DC.RIGHTS.COPYRIGHT", 
    "DC.LANGUAGE.ISO"
])

information_packages = pickle.load(open("information_packages.p", mode="rb"))

counter = 1

for information_package in information_packages:

    base_string = "9811_0001_"
    number = str(counter).zfill(4)
    identifier_other = base_string + number
    counter += 1
    
    if information_package.get("unittitle", ""):
        dc_title = information_package.get("series", "") + " - " + information_package.get("subseries", "") + " - " + information_package.get("unittitle", "")
    else:
        dc_title = ""
    
    dc_description_abstract = ""
    
    dc_contributor_author = "Duderstadt, James J."
        
    dc_contributor_other = ""
        
    dc_date_issued = "2015"
    
    dc_date_created = "2015"
    
    if not information_package.get("unitdate", ""):
        dc_coverage_temporal = "undated"
    
    else:
        if "-" in information_package.get("unitdate", "") or information_package.get("unitdate", "") == "undated" or information_package.get("unitdate", "") == "1989":
            continue
        elif information_package.get("unitdate", "") == "6/89":
            dc_coverage_temporal = "1989-06"
        else:
            try:
                dc_coverage_temporal = datetime.datetime.strptime(information_package.get("unitdate", ""), "%m/%d/%y")
            # maybe this is the best thing to do? can't tell how these are typos.
            except:
                dc_coverage_temporal = datetime.datetime.strptime(information_package.get("unitdate", ""), "%d/%m/%y")
                dc_coverage_temporal = dc_coverage_temporal.strftime("%Y-%m-%d")
                
    # if original and not preservation
    if information_package.get("original", "") != "n/a" and information_package.get("preservation", "") == "n/a":
        dc_title_filename = information_package.get("original", "")
        dc_description_filename = ""
        location = information_package.get("original_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "")
    # if original and preservation and not autopro
    if information_package.get("original", "") != "n/a" and information_package.get("preservation", "") != "n/a" and information_package.get("autopro", "") == "n/a": 
        dc_title_filename = information_package.get("original", "") + " | " + information_package.get("preservation", "")
        dc_description_filename = "Original version | Preservation version"
        location = information_package.get("original_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "") + " | " + information_package.get("preservation_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "")
    # if original and preservation and autopro
    if information_package.get("original", "") != "n/a" and information_package.get("preservation", "") != "n/a" and information_package.get("autopro", "") != "n/a":
        dc_title_filename = information_package.get("original", "") + " | " + information_package.get("preservation", "") + " | " + information_package.get("autopro", "")
        dc_description_filename = "Original version | Preservation version | Subsequent preservation version"
        location = information_package.get("original_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "") + " | " + information_package.get("preservation_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "") +  " | " + information_package.get("autopro_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "")
    # if not original and one preservation and not autopro
    if information_package.get("original", "") == "n/a" and " | " not in information_package.get("preservation", "") and information_package.get("autopro", "") == "n/a":
        dc_title_filename = information_package.get("preservation", "")
        dc_description_filename = "Preservation version"
        location = information_package.get("preservation_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "")
    # if not original and two preservation and not autpro
    if information_package.get("original", "") == "n/a" and " | " in information_package.get("preservation", "") and information_package.get("autopro", "") == "n/a":
        dc_title_filename = information_package.get("preservation", "")
        dc_description_filename = dc_description_filename = "Preservation version 1 | Preservation version 2"
        location = information_package.get("preservation_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "")
    # if not original and one preservation and one autopro
    if information_package.get("original", "") == "n/a" and " | " not in information_package.get("preservation", "") and " | " not in information_package.get("autopro", "") != "n/a":
        dc_title_filename = information_package.get("preservation", "") + " | " + information_package.get("autopro", "")
        dc_description_filename = "Preservation version | Subsequent preservation version"
        location = information_package.get("preservation_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "") +  " | " + information_package.get("autopro_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "")
    # if not original and one preservation and two autopro
    if information_package.get("original", "") == "n/a" and " | " not in information_package.get("preservation", "") and " | " in information_package.get("autopro", "") != "n/a":
        dc_title_filename = information_package.get("preservation", "") + " | " + information_package.get("autopro", "")
        dc_description_filename = "Preservation version | Subsequent preservation version 1 | Subsequent preservation version 2"
        location = information_package.get("preservation_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "") +  " | " + information_package.get("autopro_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "")
    # if not original and two preservation and one autopro
    if information_package.get("original", "") == "n/a" and " | " in information_package.get("preservation", "") and " | " not in information_package.get("autopro", "") != "n/a":
        dc_title_filename = information_package.get("preservation", "") + " | " + information_package.get("autopro", "")
        dc_description_filename = "Preservation version 1 | Preservation version 2 | Subsequent preservation version"
        location = information_package.get("preservation_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "") +  " | " + information_package.get("autopro_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "")
    # if not original and two preservation and two autopro
    if information_package.get("original", "") == "n/a" and " | " in information_package.get("preservation", "") and " | " in information_package.get("autopro", "") != "n/a":
        dc_title_filename = information_package.get("preservation", "") + " | " + information_package.get("autopro", "")
        dc_description_filename = "Preservation version 1 | Preservation version 2 | Subsequent preservation version 1 | Subsequent preservation version 2"
        location = information_package.get("preservation_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "") +  " | " + information_package.get("autopro_location", "").replace("C:\Users\eckardm\work-stuff\duderstadt", "")
                
    if information_package.get("series", "") == "Digital Images":
        dc_type = "Image"
    elif information_package.get("series", "") == "Presentations":
        dc_type = "Presentation"
    else:
        dc_type = "Office Documents"
    
    if information_package.get("accessrestrict") == True:
        dc_rights_access = "[ER Restricted until July 1, 2030]"
        dc_date_open = "2030-07-01"
    else:
        dc_rights_access = "Collection is open for research."
        dc_date_open = "2015-12-15"

    dc_rights_copyright = "Copyright has been transferred to the Regents of the University of Michigan."
    
    dc_language_iso = "en"

    with open("deepBlue_9811_0001.csv", mode="ab") as metadata_csv:
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
            location,
            dc_description_filename, 
            dc_type, 
            dc_rights_access, 
            dc_date_open, 
            dc_rights_copyright, 
            dc_language_iso])
