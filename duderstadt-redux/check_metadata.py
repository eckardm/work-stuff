import csv

with open("9811_0001.csv", mode="r") as metadata:
    reader = csv.DictReader(metadata)
    for row in reader:
        
        path_length = len(row.get("PATH", "").split("|"))
        dc_title_filenames = len(row.get("DC.TITLE.FILENAME", "").split("|"))
        dc_description_filenames = len(row.get("DC.DESCRIPTION.FILENAME", "").split("|"))
        
        if path_length != dc_title_filenames:
            print row.get("IDENTIFIER.OTHER", "")
            
        if path_length != dc_description_filenames:
            print row.get("IDENTIFIER.OTHER", "") 
            print row.get("DC.TITLE.FILENAME", ""), row.get("DC.DESCRIPTION.FILENAME", "")
            
        if "Miscellaneous" in row.get("DC.TITLE", ""):
            print row.get("DC.TITLE", "")
            print row.get("PATH", "")
            print row.get("DC.TITLE.FILENAME", "")
            print row.get("DC.DESCRIPTION.FILENAME", "")
            print "\n"
            
           