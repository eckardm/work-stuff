import os
from bs4 import BeautifulSoup
import re

# get metadata
jjd_closed = "C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\jjd_closed"
jjdhtml = "C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\jjdhtml"

metadata_list = []

for file in os.listdir(jjd_closed):
    if file.endswith(".htm"):
        with open(os.path.join(jjd_closed, file), mode="rb") as html:
            soup = BeautifulSoup(html)

            for anchor in soup("a"):
        
                metadata_dictionary = {}
            
                # skip these
                if "Use of Materials" in anchor.text or "Conditions of Use" in anchor.text or "Copyright" in anchor.text or "Suggested Citation" in anchor.text or "University of Michigan Gateway" in anchor.text or "Subseries" in anchor.text or "Files migrated to PDF/A, interface pages converted to .css" in anchor.text or "University of Michigan" in anchor.text:
                    continue
                elif "#" in anchor["href"] or anchor["href"].endswith(".htm"):
                    continue
                    
                # hardcoding these known errors
                elif "Ed for Change" in anchor.text and '"' in anchor.text and "3/22/87" in anchor.text:
                    metadata_dictionary["title"] = "Ed for Change"
                    metadata_dictionary["date"] = "3/22/87"
                    metadata_dictionary["href"] = anchor["href"]
                elif "Nursing" in anchor.text and '"' in anchor.text and "6/11/87" in anchor.text:
                    metadata_dictionary["title"] = "Nursing"
                    metadata_dictionary["date"] = "6/11/87"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == 'Elements of Campaign"5/16/89':
                    metadata_dictionary["title"] = "Elements of Campaign"
                    metadata_dictionary["date"] = "5/16/89"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Teaching and Research 2.12/14/91":
                    metadata_dictionary["title"] = "Teaching and Research 2.1"
                    metadata_dictionary["date"] = "2/14/91"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "State of Univ 1992 3, .11/6/93":
                    metadata_dictionary["title"] = "State of Univ 1992 3.1"
                    metadata_dictionary["date"] = "1/6/93"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Strategic Initiatives and . , .2/9/95":
                    metadata_dictionary["title"] = "Strategic Initiatives and..."
                    metadata_dictionary["date"] = "2/9/95"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "DC Notes-9/12. 9/12/90":
                    metadata_dictionary["title"] = "DC Notes-9/12"
                    metadata_dictionary["date"] = "9/12/90"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "ITI Followup. 12/20/90":
                    metadata_dictionary["title"] = "ITI Followup"
                    metadata_dictionary["date"] = "12/20/90"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Teeter , (7/10/91)7/10/91":
                    metadata_dictionary["title"] = "Teeter (7/10/91)"
                    metadata_dictionary["date"] = "7/10/91"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Family Community Center":
                    metadata_dictionary["title"] = "Family Community Center"
                    metadata_dictionary["date"] = "undated"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "OUE Memo 7/2, 7/92":
                    metadata_dictionary["title"] = "OUE Memo"
                    metadata_dictionary["date"] = "7/2/92"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Progress Report , 1.211/27/92":
                    metadata_dictionary["title"] = "Progress Report 1.2"
                    metadata_dictionary["date"] = "1/27/92"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "GUIR Presentation8/28/96":
                    metadata_dictionary["title"] = "GUIR Presentation"
                    metadata_dictionary["date"] = "8/28/96"
                    metadata_dictionary["href"] = anchor["href"]
                                
                else:
                    try:
                        metadata_dictionary["title"] = re.findall("(.*)(?=\,\s*\d{1,2}\/\d{1,2}\/\d{1,2})", anchor.text.strip())[0]
                    except:
                        print anchor.text.strip()
                        print anchor["href"]
                        continue
                    metadata_dictionary["date"] = re.findall("(\d{1,2}\/\d{1,2}\/\d{1,2})$", anchor.text.strip())[0]
                    metadata_dictionary["href"] = anchor["href"]
            
                metadata_list.append(metadata_dictionary)

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
                elif anchor.text.strip() == "New Faculty Welcome, 2.08/30/87":
                    metadata_dictionary["title"] = "New Faculty Welcome, 2.0"
                    metadata_dictionary["date"] = "8/30/87"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Football Building Kickoff2, /17/89":
                    metadata_dictionary["title"] = "Football Building Kickoff"
                    metadata_dictionary["date"] = "2/17/89"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Lagatus, 6/89":
                    metadata_dictionary["title"] = "Lagatus"
                    metadata_dictionary["date"] = "6/89"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Rotary5, /9/89":
                    metadata_dictionary["title"] = "Rotary"
                    metadata_dictionary["date"] = "5/9/89"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Alumni Talks--Summer 1989, /20/89":
                    metadata_dictionary["title"] = "Alumni Talks--Summer 1989"
                    metadata_dictionary["date"] = "1989"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Bo 12/13/89":
                    metadata_dictionary["title"] = "Bo"
                    metadata_dictionary["date"] = "12/13/89"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "MLK Closing, 1/151/14/90":
                    metadata_dictionary["title"] = "MLK Closing"
                    metadata_dictionary["date"] = "1/15/90"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "MLK Welcome, 1/141/14/90":
                    metadata_dictionary["title"] = "MLK Welcome"
                    metadata_dictionary["date"] = "1/14/90"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Science Education, 2.13/1/90":
                    metadata_dictionary["title"] = "Science Education, 2.1"
                    metadata_dictionary["date"] = "3/1/90"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "State of Univ. l0/2/89, 3/":
                    metadata_dictionary["title"] = "State of Univ."
                    metadata_dictionary["date"] = "10/2/89"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "a) Introductions 3/11/90":
                    metadata_dictionary["title"] = "a) Introductions"
                    metadata_dictionary["date"] = "3/11/90"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Public Education 4.0 9/8/90":
                    metadata_dictionary["title"] = "Public Education 4.0"
                    metadata_dictionary["date"] = "9/8/90"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Parents Weekend, 3.0 10/27/90":
                    metadata_dictionary["title"] = "Parents Weekend, 3.0"
                    metadata_dictionary["date"] = "10/27/90"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Appro Hearings, 2.0 3/25/91":
                    metadata_dictionary["title"] = "Appro Hearings, 2.0"
                    metadata_dictionary["date"] = "3/25/91"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Appro Hearings 3.0, (Actual) 3/27/91":
                    metadata_dictionary["title"] = "Appro Hearings 3.0, (Actual)"
                    metadata_dictionary["date"] = "3/27/91"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "Fresh Convocation 6.0":
                    metadata_dictionary["title"] = "Fresh Convocation 6.0"
                    metadata_dictionary["date"] = "undated"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "6-1 Table of Color %5/16/96":
                    metadata_dictionary["title"] = "6-1 Table of Color"
                    metadata_dictionary["date"] = "5/16/96"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "3-11 ProfPublics color5/29/96":
                    metadata_dictionary["title"] = "3-11 ProfPublics color"
                    metadata_dictionary["date"] = "5/29/96"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "7-9 WomFaculty color5/31/96":
                    metadata_dictionary["title"] = "7-9 WomFaculty color"
                    metadata_dictionary["date"] = "5/31/96"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "SAC-26/8/96":
                    metadata_dictionary["date"] = "SAC-2"
                    metadata_dictionary["title"] = "6/8/96"
                    metadata_dictionary["href"] = anchor["href"]
                elif anchor.text.strip() == "SAC-16/8/96":
                    metadata_dictionary["title"] = "SAC-1"
                    metadata_dictionary["date"] = "6/8/96"
                    metadata_dictionary["href"] = anchor["href"]
                                
                else:
                    try:
                        metadata_dictionary["title"] = re.findall("(.*)(?=\,\s*\d{1,2}\/\d{1,2}\/\d{1,2})", anchor.text.strip())[0]
                    except:
                        print anchor.text.strip()
                        continue
                    metadata_dictionary["date"] = re.findall("(\d{1,2}\/\d{1,2}\/\d{1,2})$", anchor.text.strip())[0]
                    metadata_dictionary["href"] = anchor["href"]
            
                metadata_list.append(metadata_dictionary)

with open("metadata.py", mode="w") as metadata:
    metadata.write("# metadata\n")
    metadata.write("metadata = " + str(metadata_list) + "\n")
        