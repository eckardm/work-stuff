import os
from bs4 import BeautifulSoup
import re

# get metadata
jjdhtml = "C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\jjdhtml"

metadata_list = []

for file in os.listdir(jjdhtml):
    if file.endswith(".htm"):
        with open(os.path.join(jjdhtml, file), mode="rb") as html:
            soup = BeautifulSoup(html)

            for anchor in soup("a"):
        
                metadata_dictionary = {}
            
                # skip these
                if "Use of Materials" in anchor.text or "Conditions of Use" in anchor.text or "Copyright" in anchor.text or "Suggested Citation" in anchor.text or "University of Michigan Gateway" in anchor.text or "Subseries" in anchor.text or "Files migrated to PDF/A, interface pages converted to .css" in anchor.text or "University of Michigan" in anchor.text:
                    continue
                elif "#" in anchor["href"] or anchor["href"].endswith(".htm"):
                    continue
            
                # hardcoding these known errors
                elif anchor.text == "Football Building Kickoff2, /17/89":
                    metadata_dictionary["title"] = "Football Building Kickoff"
                    metadata_dictionary["date"] = "2/17/89"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text == "Lagatus, 6/89":
                    metadata_dictionary["title"] = "Lagatus"
                    metadata_dictionary["date"] = "1989-06"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text == "Rotary5, /9/89":
                    metadata_dictionary["title"] = "Rotary"
                    metadata_dictionary["date"] = "5/9/89"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text == "Alumni Talks--Summer 1989, /20/89":
                    metadata_dictionary["title"] = "Alumni Talks--Summer 1989"
                    metadata_dictionary["date"] = "1989"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text == "Fresh Convocation 6.0":
                    metadata_dictionary["title"] = "Fresh Convocation 6.0"
                    metadata_dictionary["date"] = "undated"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text == "MLK Closing, 1/151/14/90":
                    metadata_dictionary["title"] = "MLK Closing"
                    metadata_dictionary["date"] = "1990-01-15"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text == "MLK Welcome, 1/141/14/90":
                    metadata_dictionary["title"] = "MLK Welcome"
                    metadata_dictionary["date"] = "1990-01-14"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text == "State of Univ. l0/2/89, 3/":
                    metadata_dictionary["title"] = "State of Univ"
                    metadata_dictionary["date"] = "1989-10-02"
                    metadata_dictionary["href"] = anchor["href"]
                else:
                    metadata_dictionary["title"] = re.findall("(.*)(?=\d+\/\d+\/\d+)", anchor.text)[0].rstrip(", ")
                    metadata_dictionary["date"] = re.findall("\d+\/\d+\/\d+", anchor.text)[0]
                    metadata_dictionary["href"] = anchor["href"]
                
                metadata_list.append(metadata_dictionary)
        
with open("metadata.py", mode="w") as metadata:
    metadata.write("# metadata\n")
    metadata.write("metadata = " + str(metadata_list) + "\n")
        