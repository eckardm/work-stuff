import csv
import os
import cPickle as pickle

droid_list = []

with open("droid.csv", mode="rb") as csv_file:
    reader = csv.DictReader(csv_file)
    
    droid_dictionary = {}
    
    for row in reader:
        droid_dictionary["file_path"] = row.get("FILE_PATH", "")
        droid_dictionary["name"] = row.get("NAME", "")
        droid_dictionary["puid"] = row.get("PUID", "")
        droid_dictionary["mime_type"] = row.get("MIME_TYPE", "")
        droid_dictionary["format_name"] = row.get("FORMAT_NAME", "")
        droid_dictionary["format_version"] = row.get("FORMAT_VERSION", "")
        
    droid_list.append(droid_dictionary)
        
information_packages = pickle.load(open("information_packages.p", mode="rb"))

leftovers = []

for root, _, files in os.walk("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\original-records"):
    for name in files:
        for information_package in information_packages:
            if information_package.get("original_location", "") == os.path.join(root, name):
                if information_package.get("preservation", "") == "n/a" and information_package.get("autopro", "") == "n/a": 
                   
                    leftover = {}
                    
                    leftover["original_location"] = information_package.get("original_location", "")
                  
                    leftover["mime_type"] = "n/a"
                    for droid_dictionary in droid_list:
                        print information_package.get("original_location", "")
                        print droid_dictionary.get("file_path")
                        
                        if droid_dictionary.get("file_path") == information_package.get("original_location", ""):
                            leftover["mime_type"] = droid_dictionary["mime_type"] = reader.get("MIME_TYPE", "")
                            
                    leftovers.append(leftover)
               
for leftover in leftovers:
    if leftover.get("mime_type", "") != "n/a":
        print leftover
