import requests
from bs4 import BeautifulSoup
from tqdm import *
import os
import urllib
import time

# scrape data
base_url = "http://bentley.umich.edu/elecrec/d/duderstadt-2/"

# i'm a conscientious scraper
headers = {"user-agent": "Duderstadt Scraper: eckardm at umich (dot) com"}
data = requests.get(base_url, headers=headers)
soup = BeautifulSoup(data.text)

os.mkdir("duderstadt-2")

for anchor in tqdm(soup("a")):
    if anchor.text.strip() in ["Legacy/", "Presentations/", "Speeches/"]:
        os.mkdir("duderstadt-2" + "/" + anchor["href"])
        subgroup_data = requests.get(base_url + anchor["href"], headers=headers)
        subgroup_soup = BeautifulSoup(subgroup_data.text)
        
        for subgroup_anchor in subgroup_soup("a"):
            if subgroup_anchor.text.strip() != "Parent Directory":
                os.mkdir("duderstadt-2" + "/" + anchor["href"] + "/" + subgroup_anchor["href"])
                digital_documents_data = requests.get(base_url + anchor["href"] + subgroup_anchor["href"], headers=headers)
                digital_documents_soup = BeautifulSoup(digital_documents_data.text)
                
                for digital_document_anchor in digital_documents_soup("a"):
                    if "restricted" in digital_document_anchor.text:
                        os.mkdir("duderstadt-2" + "/" + anchor["href"] + "/" + subgroup_anchor["href"] + "/" + digital_document_anchor["href"])
                        restricted_digital_documents_data = requests.get(base_url + anchor["href"] + subgroup_anchor["href"] + digital_document_anchor["href"])
                        restricted_digital_documents_soup = BeautifulSoup(restricted_digital_documents_data.text)
                        
                        for restricted_digital_documents_anchor in restricted_digital_documents_soup("a"):
                            if restricted_digital_documents_anchor.text.strip() != "Parent Directory":
                                urllib.urlretrieve(base_url + anchor["href"] + subgroup_anchor["href"] + digital_document_anchor["href"] + restricted_digital_documents_anchor["href"], "duderstadt-2" + "/" + anchor["href"] + "/" + subgroup_anchor["href"] + "/" + digital_document_anchor["href"] + "/" + restricted_digital_documents_anchor["href"])
                                
                    elif digital_document_anchor.text.strip() != "Parent Directory":
                        urllib.urlretrieve(base_url + anchor["href"] + subgroup_anchor["href"] + digital_document_anchor["href"], "duderstadt-2" + "/" + anchor["href"] + "/" + subgroup_anchor["href"] + "/" + digital_document_anchor["href"])
                    
                    # i'm a conscentious scraper
                    time.sleep(1)
