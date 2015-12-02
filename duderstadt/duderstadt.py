import requests
from bs4 import BeautifulSoup
from tqdm import *
import os
import urllib
import time
import csv

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

# identify converted files

# write metadata
