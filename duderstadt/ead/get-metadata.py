import csv
import requests
from bs4 import BeautifulSoup

metadata_list = list()

with open("data.txt", mode="rb") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")
    for row in reader:
        
        metadata_dictionary = dict()
        
        metadata_dictionary["handle"] = row.get("handle", "")
        
        # go to link and get additional metadata
        
        metadata_list.append(metadata_dictionary)
