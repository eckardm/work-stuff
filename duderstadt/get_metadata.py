import requests
from bs4 import BeautifulSoup
import time
import re

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
                metadata_dictionary["date"] = "1989-06"
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
            elif folder_anchor.text == "MLK Closing, 1/151/14/90"
                metadata_dictionary["title"] = "MLK Closing"
                metadata_dictionary["date"] = "1990-01-15"
                metadata_dictionary["href"] = folder_anchor["href"]
            elif folder_anchor.text == "MLK Welcome, 1/141/14/90"
                metadata_dictionary["title"] = "MLK Welcome"
                metadata_dictionary["date"] = "1990-01-14"
                metadata_dictionary["href"] = folder_anchor["href"]
            else:
                metadata_dictionary["title"] = re.findall("(.*)(?=\d+\/\d+\/\d+)", folder_anchor.text)[0].strip().rstrip(",")
                metadata_dictionary["date"] = re.findall("\d+\/\d+\/\d+", folder_anchor.text)[0]
                metadata_dictionary["href"] = folder_anchor["href"]
            
            metadata_list.append(metadata_dictionary)

            time.sleep(1)
    
with open("metadata.py", mode="w") as metadata:
    metadata.write("# metadata\n")
    metadata.write("metadata = " + str(metadata_list) + "\n")
    