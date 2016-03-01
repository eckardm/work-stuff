import os
from openpyxl import load_workbook

dc_titles = []
dc_descriptions = []

filenames = []
filenames_in_metadata = []

path = r"X:\deepblue\2015061_0001"

for filename in os.listdir(path):
    
    if filename.startswith("deepBlue_"):
        wb = load_workbook(filename=os.path.join(path, filename), read_only=True)
        ws = wb.active
        
        for row in ws.rows:
            for title in row[8].value.split(" | "):
                if title != "DC.TITLE.FILENAME ":
                    filenames_in_metadata.append(title)
        
            dc_titles.append(row[1].value)
            dc_descriptions.append(row[2].value)
        
    else:
        if filename != "Thumbs.db":
            filenames.append(filename)
        
if len(dc_titles) == len(set(dc_titles)):
    print "All titles unique!"
else:
    print "All titles not unique! Write some code to figure that out!"

if len(dc_descriptions) == len(set(dc_descriptions)):
    print "All descriptions unique!"
else:
    print "All descriptions not unique! Write some code to figure that out!"   
    
if len(filenames) == len(filenames_in_metadata):
    print "Number of filenames and number of filenames in metadata match!"
else:
    print "Number of filenames: ", len(filenames)
    print "Number of filenames in metadata: ", len(filenames_in_metadata)
    
filenames_match_check = []

for filename in filenames:
    if filename not in filenames_in_metadata:
        filenames_match_check.append(filename)
        
if len(filenames_match_check) == 0:
    print "All filenames and filenames in metadata match!"
else:
    print "Check on the following filesnames in the metadata: "
    for filename in filenames_match_check:
        print filename
