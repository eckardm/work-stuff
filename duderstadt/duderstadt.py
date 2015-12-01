import requests
from bs4 import BeautifulSoup
from tqdm import *
import os
import urllib
import time
import csv

'''
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



converted_files = {}
with open("convertedFiles_9811_0003.csv", mode="r") as converted_files_csv:
    reader = csv.reader(converted_files_csv)
    for row in reader:
        input = os.path.split(row[0].split("; ")[1].strip())[1].replace('"', "")
        output = os.path.split(row[0].split("; ")[2].strip())[1].replace('"', "")
        if input in converted_files:
            print input, output, converted_files[input]
        converted_files[input] = output
          

print len(converted_files)
test = []
for root, dirs, files in os.walk("C:\Users\eckardm\work-stuff\duderstadt\duderstadt"):
    for name in files:
        if name in converted_files:
            test.append(name)
print len(test)

for name in converted_files:
    if name not in test:
        print "what?", name


restricted_files = []
'''
        if filename.split(".")[0] + "-bhl_" in os.listdir("path/to/directory"):
            row.append("9811_0003_0001")
            row.append(title)
            row.append("Duderstadt, James J.")
            row.append("")
            row.append("2015-11-25")
            row.append(date)
        if "-bhl_" in filename:
            row.append(filename.split("-bhl_")[0] + filename[-4:] + "|" + filename)
        writer.writerow( title, "", "Duderstadt, James J.", "", "2015-11-25", date, , "Access version | Preservation version", ""])
        
        with open("deepBlue_9811_0003", mode="ab") as metadata:
    writer = csv.writer(metadata)'''
