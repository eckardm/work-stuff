import cPickle as pickle
import os
from tqdm import *
from fuzzywuzzy import fuzz
from collections import defaultdict

metadata = pickle.load(open("metadata.p", mode="rb"))
converted_files = pickle.load(open("converted_files.p", mode="rb"))

information_packages = []

print "Creating initial information packages..."

for root, _, files in tqdm(os.walk("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\original-records")):
 
    information_package = {}

    names = [name for name in files if name != "Archivist Note"]
    
    for name in tqdm(names, desc="\\" + "\\".join(root.split("\\")[7:])):

        information_package = {}
        
        if "Speeches" in root:
            information_package["series"] = "Speeches"
            
            if "1986-1987 Speeches" in root:
                information_package["subseries"] = "1986-1987 Speeches"
            if "1987-1988 Speeches" in root:
                information_package["subseries"] = "1987-1988 Speeches"
            if "1988-1989 Speeches" in root:
                information_package["subseries"] = "1988-1989 Speeches"
            if "1989-1990 Speeches" in root:
                information_package["subseries"] = "1989-1990 Speeches"
            if "1990-1991 Speeches" in root:
                information_package["subseries"] = "1990-1991 Speeches"
            if "1991-92" in root:
                information_package["subseries"] = "1991-1992 Speeches"
            if "1992-1993 Speeches" in root:
                information_package["subseries"] = "1992-1993 Speeches"
            if "1994-1995 Speeches" in root:
                information_package["subseries"] = "1994-1995 Speeches"
            if "1995-1996 Speeches" in root: # don't appear to be in original-records
                information_package["subseries"] = "1995-1996 Speeches"
            if "Athletics Talks" in root:
                information_package["subseries"] = "Athletic Talks-Speeches"
                
            information_package["accessrestrict"] = False
                
        if "Idea Files" in root:
            information_package["series"] = "Idea Files"
            
            if "1986-1987 Ideas" in root:
                information_package["subseries"] = "1986-1987 Ideas"
            if "1987-1988 Ideas" in root:
                information_package["subseries"] = "1987-1988 Ideas"
            if "1988-1989 Ideas" in root:
                information_package["subseries"] = "1988-1989 Ideas"
            if "1989-1990 Ideas" in root:
                information_package["subseries"] = "1989-1990 Ideas"
            if "1990-1991 Ideas" in root:
                information_package["subseries"] = "1990-1991 Ideas"
            if "1991-1992 Ideas" in root:
                information_package["subseries"] = "1991-1992 Ideas"
            if "1992-1993 Ideas" in root:
                information_package["subseries"] = "1992-1993 Ideas"
            if "1993-1994 Ideas" in root:
                information_package["subseries"] = "1993-1994 Ideas"
            if "1994-1995 Ideas" in root:
                information_package["subseries"] = "1994-1995 Ideas"
                
            information_package["accessrestrict"] = True
            
        if "Strategy" in root:
            information_package["series"] = "Strategy"
            information_package["subseries"] = "1986-1997"
            information_package["accessrestrict"] = True
            
        if "Position Papers" in root:
            information_package["series"] = "Position Papers"
            
            if "1986-1987 Position Papers" in root or "1987-1988 Position Papers" in root or "1988-1989 Position Papers" in root or "1989-1990 Position Papers" in root or "1990-1991 Position Papers" in root:
                information_package["subseries"] = "1986-1991 Position Papers"
            elif "1991-1992 Position Papers" in root or "1992-1993 Position Papers" in root or "1993-1994 Position Papers" in root or "1994-1995 Position Papers" in root or "1995-1996 Position Papers" in root:
                information_package["subseries"] = "1991-1996 Position Papers"
            elif "1996-1997 Position Papers" in root:
                information_package["subseries"] = "1996-1997 Position Papers"
            
            information_package["accessrestrict"] = True
            
        if "Presentations" in root:
            information_package["series"] = "Presentations"
            
            if "1987-1988 Presentations" in root:
                information_package["subseries"] = "1987-1988 Presentations"
            if "1988-1989 Presentations" in root:
                information_package["subseries"] = "1988-1989 Presentations"
            if "1989-1990 Presentations" in root:
                information_package["subseries"] = "1989-1990 Presentations"
            if "1990-1991 Presentations" in root:
                information_package["subseries"] = "1990-1991 Presentations"
            if "1991-1992 Presentations" in root:
                information_package["subseries"] = "1991-1992 Presentations"
            if "1992-1993 Presentations" in root:
                information_package["subseries"] = "1992-1993 Presentations"
            if "1993-1994 Presentations" in root:
                information_package["subseries"] = "1993-1994 Presentations"
            if "1994-1995 Presentations" in root:
                information_package["subseries"] = "1994-1995 Presentations"
            if "1995-1996 Presentations" in root:
                information_package["subseries"] = "1995-1996 Presentations"
            if "1996-1997 Presentations" in root:
                information_package["subseries"] = "1996-1997 Presentations"

            information_package["accessrestrict"] = False
            
        if "Write Files" in root:
            information_package["series"] = "Write Files"
            
            if "1988 and earlier Write" in root:
                information_package["subseries"] = "1988 and earlier Write Files"
            if "1988-1989 Write Files" in root:
                information_package["subseries"] = "1988-1989 Write Files"
            if "1989-1990 Write Files" in root:
                information_package["subseries"] = "1989-1990 Write Files"
            if "1990-1991 Write Files" in root:
                information_package["subseries"] = "1990-1991 Write Files"
            if "1991-1992 Write Files" in root:
                information_package["subseries"] = "1991-1992 Write Files"
            if "1992-1993 Write Files" in root:
                information_package["subseries"] = "1992-1993 Write Files"
            if "1993-1994 Write Files" in root:
                information_package["subseries"] = "1993-1994 Write Files"
            if "1994-1995 Write Files" in root:
                information_package["subseries"] = "1994-1995 Write Files"
            if "1995-1996 Write Files" in root:
                information_package["subseries"] = "1995-1996 Write Files"
            if "1996-1997 Write Files" in root:
                information_package["subseries"] = "1996-1997 Write Files"

            information_package["accessrestrict"] = True
            
        if "Legacy" in root:
            information_package["series"] = "Legacy"
            information_package["subseries"] = "1996"
            information_package["accessrestrict"] = True
            
        if "Digital Images" in root:
            information_package["series"] = "Digital Images"
            information_package["subseries"] = "1996"
            information_package["accessrestrict"] = False
            
        information_package["unittitle"] = name
        
        information_package["original"] = name
        information_package["original_location"] = os.path.join(root, name)
        
        information_package["unitdate"] = ""
        information_package["preservation"] = "n/a"
        information_package["preservation_location"] = "n/a"
        
        for metadata_dictionary in metadata:
            if fuzz.token_sort_ratio(metadata_dictionary.get("title", ""), name) > 95:
                
                information_package["unitdate"] = metadata_dictionary.get("date", "")
                information_package["preservation"] = metadata_dictionary.get("href", "").split("/")[-1]
                information_package["preservation_location"] = metadata_dictionary.get("href", "").replace("..", "C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data").replace("/", "\\")
                
        information_packages.append(information_package)
        
# autopro'd files
print "Accounting for converted files..."
        
for information_package in tqdm(information_packages):

    shortened_preservation_location = "\\".join(information_package.get("preservation_location", "").split("\\")[7:])
    
    autopro = "n/a"
    autopro_location = "n/a"
    
    for converted_file in converted_files:
        shortened_original_location = "\\".join(converted_file.split("\\")[4:]).replace('"', "")
        if shortened_original_location == shortened_preservation_location:
            autopro = converted_files.get(converted_file, "").split("\\")[-1].replace('"', "")
            autopro_location = "C:\Users\eckardm\work-stuff\duderstadt\converted_files" + "\\" + "-".join(converted_files.get(converted_file, "").split("\\")[4:]).replace('"', "")
            
    information_package["autopro"] = autopro
    information_package["autopro_location"] = autopro_location

print "Accounting for restricted files..."

for information_package in tqdm(information_packages):

    if "restricted" in information_package.get("preservation_location", ""):
        information_package["accessrestrict"] = True
        
# 1995-1996 Speeches
print "Accounting for known errors..."
speeches_that_go_together = defaultdict(list)

for root, _, files in os.walk("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches"):
    for name in tqdm(files):
        if "JJDS9a" in root or "JJDS9b" in root:
        
            filename = name[:-4]
            
            if name not in speeches_that_go_together[filename]:
                speeches_that_go_together[filename].append(name)

speeches = []

for key, value in speeches_that_go_together.iteritems():
    
    speech = {}
    
    speech["series"] = "Speeches"
    speech["subseries"] = "1995-1996 Speeches"
    speech["accessrestrict"] = False
    speech["original"] = "n/a"
    speech["original_location"] = "n/a"
    speech["autopro"] = "n/a"
    speech["autopro_location"] = "n/a"
    
    if len(value) == 1:
        speech["preservation"] = value[0]
        if os.path.isfile(os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a", value[0])) == True:
            speech["preservation_location"] = os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a", value[0])
        elif os.path.isfile(os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a\S9restricted", value[0])) == True:
            speech["preservation_location"] = os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a\S9restricted", value[0])
        else:
            speech["preservation_location"] = os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9b", value[0])
        for filename in os.listdir("C:\Users\eckardm\work-stuff\duderstadt\converted_files"):
            if filename.startswith("Speeches-JJD9a-" + key + "_bhl-") and value[0][:-3] in filename:
                speech["autopro"] = filename
                speech["autopro_location"] = os.path.join("C:\Users\eckardm\work-stuff\duderstadt\converted_files", filename)
    
    else:
        speech["preservation"] = value[0] + " | " + value[1]
        if os.path.isfile(os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a", value[0])) == True:
            speech["preservation_location"] = os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a", value[0]) + " | " + os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a", value[1])
        elif os.path.isfile(os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a\S9restricted", value[0])) == True:
            speech["preservation_location"] = os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a\S9restricted", value[0]) + " | " + os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9a\S9restricted", value[1])
        else:
            speech["preservation_location"] = os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9b", value[0]) + " | " + os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\Speeches\JJDS9b", value[1])

    speech["unittitle"] = ""
    speech["unitdate"] = ""
    
    for metadata_dictionary in metadata:

        if metadata_dictionary.get("href", "").split("/")[-1][:-4] == key:
            speech["unittitle"] = metadata_dictionary.get("title", "")
            speech["unitdate"] = metadata_dictionary.get("date", "")

    speeches.append(speech)

autoprod_speeches_that_go_together = defaultdict(list)    
    
for filename in os.listdir("C:\Users\eckardm\work-stuff\duderstadt\converted_files"):
    if "JJDS9a" in filename or "JJDS9b" in filename:
        
        root = filename.split("_bhl-")[0]
        
        autoprod_speeches_that_go_together[root].append(filename)
    
for key, value in autoprod_speeches_that_go_together.iteritems():

    if len(value) == 1:
        autopro = value[0]
        autopro_location = os.path.join("C:\Users\eckardm\work-stuff\duderstadt\converted_files", value[0])
        
    else:
        autopro = value[0] + " | " + value[1]
        autopro_location = os.path.join("C:\Users\eckardm\work-stuff\duderstadt\converted_files", value[0]) + " | " + os.path.join("C:\Users\eckardm\work-stuff\duderstadt\converted_files", value[1])
        
    for speech in speeches:
        if "-".join(speech.get("preservation_location").split(" | ")[0].split("\\")[7:]).split(".")[0] == key:
            speech["autopro"] = autopro
            speech["autopro_location"] = autopro_location
        
for speech in speeches:
    information_packages.append(speech)
        
# temp
import csv
with open("temp.csv", mode="wb") as temp:
        writer = csv.writer(temp)
        writer.writerow([
            "series", 
            "subseries", 
            "accessrestrict", 
            "unittitle", 
            "original", 
            "original_location", 
            "unitdate", 
            "preservation", 
            "preservation_location",
            "autopro",
            "autopro_location"
        ])

for information_package in information_packages:
    with open("temp.csv", mode="ab") as temp:
        writer = csv.writer(temp)
        writer.writerow([
            information_package.get("series"), 
            information_package.get("subseries"), 
            information_package.get("accessrestrict"), 
            information_package.get("unittitle"), 
            information_package.get("original"), 
            information_package.get("original_location"), 
            information_package.get("unitdate"), 
            information_package.get("preservation"), 
            information_package.get("preservation_location"),
            information_package.get("autopro"),
            information_package.get("autopro_location")
        ])
        
pickle.dump(information_packages, open("information_packages.p", "wb"))

print "Alright, we're done!"
