import os
import csv

headers = [
    "ID", 
    "PARENT_ID", 
    "URI", 
    "FILE_PATH", 
    "NAME", 
    "METHOD", 
    "STATUS", 
    "SIZE", 
    "TYPE", 
    "EXT", 
    "LAST_MODIFIED", 
    "EXTENSION_MISMATCH", 
    "MD5_HASH", 
    "FORMAT_COUNT", 
    "PUID", 
    "MIME_TYPE", 
    "FORMAT_NAME", 
    "FORMAT_VERSION", 
]

results = []

for droid_output in os.listdir("droid_outputs"):
      
    with open(os.path.join("droid_outputs", droid_output), mode="rb") as droid_dai:
        reader = csv.DictReader(droid_dai)
        for row in reader:
        
            result = []
        
            if row.get("TYPE", "") == "Folder" or row.get("TYPE", "") == "Container":
                continue
            if "_bhl-" in row.get("NAME", ""):
                continue
            
            for header in headers:
                result.append(row.get(header, ""))
                
            results.append(result)

with open("droid_sho.csv", mode="wb") as droid_sho:
    writer = csv.writer(droid_sho)
    writer.writerow(headers)
    writer.writerows(results)
