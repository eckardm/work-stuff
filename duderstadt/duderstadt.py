import requests
from bs4 import BeautifulSoup
from tqdm import *
import os
import urllib
import time
import csv
import re

'''
# scrape data
base_url = "http://bentley.umich.edu/elecrec/d/duderstadt/"

headers = {"user-agent": "Duderstadt Scraper: eckardm at umich (dot) com"}
data = requests.get(base_url, headers=headers)
soup = BeautifulSoup(data.text)

os.mkdir("duderstadt")

for anchor in tqdm(soup("a")):
    if anchor.text.strip() in ["Legacy/", "Presentations/", "Speeches/"]:
        os.mkdir("duderstadt" + "/" + anchor["href"])
        subgroup_data = requests.get(base_url + anchor["href"], headers=headers)
        subgroup_soup = BeautifulSoup(subgroup_data.text)
        
        for subgroup_anchor in subgroup_soup("a"):
            if subgroup_anchor.text.strip() != "Parent Directory":
                os.mkdir("duderstadt" + "/" + anchor["href"] + "/" + subgroup_anchor["href"])
                digital_documents_data = requests.get(base_url + anchor["href"] + subgroup_anchor["href"], headers=headers)
                digital_documents_soup = BeautifulSoup(digital_documents_data.text)
                
                for digital_document_anchor in digital_documents_soup("a"):
                    if "restricted" in digital_document_anchor.text:
                        os.mkdir("duderstadt" + "/" + anchor["href"] + "/" + subgroup_anchor["href"] + "/" + digital_document_anchor["href"])
                        restricted_digital_documents_data = requests.get(base_url + anchor["href"] + subgroup_anchor["href"] + digital_document_anchor["href"])
                        restricted_digital_documents_soup = BeautifulSoup(restricted_digital_documents_data.text)
                        
                        for restricted_digital_documents_anchor in restricted_digital_documents_soup("a"):
                            if restricted_digital_documents_anchor.text.strip() != "Parent Directory":
                                urllib.urlretrieve(base_url + anchor["href"] + subgroup_anchor["href"] + digital_document_anchor["href"] + restricted_digital_documents_anchor["href"], "duderstadt" + "/" + anchor["href"] + "/" + subgroup_anchor["href"] + "/" + digital_document_anchor["href"] + "/" + restricted_digital_documents_anchor["href"])
                                
                    elif digital_document_anchor.text.strip() != "Parent Directory":
                        urllib.urlretrieve(base_url + anchor["href"] + subgroup_anchor["href"] + digital_document_anchor["href"], "duderstadt" + "/" + anchor["href"] + "/" + subgroup_anchor["href"] + "/" + digital_document_anchor["href"])
                        
                    time.sleep(1)'''

# write headers for metadata
metadata_headers = [
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
]

with open("deepBlue_9811_0003.csv", mode="wb") as metadata:
    writer = csv.writer(metadata)
    for metadata_header in metadata_headers:
        writer.writerow(metadata_header)

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
metadata_list = []

base_url = "http://bentley.umich.edu/elecrec/d/duderstadt/jjdhtml/"

headers = {"user-agent": "Duderstadt Scraper: eckardm at umich (dot) com"}
data = requests.get(base_url, headers=headers)
soup = BeautifulSoup(data.text)

for anchor in soup("a"):
    if anchor.text.endswith(".htm") and anchor.text != "use.htm":
        folder_data = requests.get(base_url + anchor["href"], headers=headers)
        folder_soup = BeautifulSoup(folder_data.text)
        
        for folder_anchor in folder_soup("a"):
        
            metadata_dictionary = {}
        
            # skip these
            if "Use of Materials" in folder_anchor.text or "Conditions of Use" in folder_anchor.text or "Copyright" in folder_anchor.text or "Suggested Citation" in folder_anchor.text or "University of Michigan Gateway" in folder_anchor.text or "Subseries" in folder_anchor.text or "Files migrated to PDF/A, interface pages converted to .css" in folder_anchor.text or "University of Michigan" in folder_anchor.text:
                continue
            elif "#" in folder_anchor["href"] or folder_anchor["href"].endswith(".htm"):
                continue
        
            # hardcoding these known errors
            elif folder_anchor.text == "Football Building Kickoff2, /17/89":
                metadata_dictionary["title"] = "Football Building Kickoff"
                metadata_dictionary["date"] = "2/17/89"
                metadata_dictionary["href"] = folder_anchor["href"]
            elif folder_anchor.text == "Lagatus, 6/89":
                metadata_dictionary["title"] = "Lagatus"
                metadata_dictionary["date"] = "6/89"
                metadata_dictionary["href"] = folder_anchor["href"]
            elif folder_anchor.text == "Rotary5, /9/89":
                metadata_dictionary["title"] = "Rotary"
                metadata_dictionary["date"] = "5/9/89"
                metadata_dictionary["href"] = folder_anchor["href"]
            elif folder_anchor.text == "Alumni Talks--Summer 1989, /20/89":
                metadata_dictionary["title"] = "Alumni Talks--Summer 1989"
                metadata_dictionary["date"] = "1989"
                metadata_dictionary["href"] = folder_anchor["href"]
            elif folder_anchor.text == "Fresh Convocation 6.0":
                metadata_dictionary["title"] = "Fresh Convocation 6.0"
                metadata_dictionary["date"] = "undated"
                metadata_dictionary["href"] = folder_anchor["href"]
                
            else:
                metadata_dictionary["title"] = re.findall("(.*)(?=\d+\/\d+\/\d+)", folder_anchor.text)[0].strip().rstrip(",")
                metadata_dictionary["date"] = re.findall("\d+\/\d+\/\d+", folder_anchor.text)[0]
                metadata_dictionary["href"] = folder_anchor["href"]
            
            metadata_list.append(metadata_dictionary)

    time.sleep(1)

# write metadata
'''
File | Name	| Author | Date of Publication or Speech | Title
-----|------|--------|-------------------------------|------'''
