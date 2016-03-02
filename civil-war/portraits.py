import requests
from bs4 import BeautifulSoup
import time
import csv
from tqdm import *

headers = {"user-agent": "Name scraper v.0.1 - please contact eckardm@umich.edu if there are any issues"}
data = requests.get("http://bentley.umich.edu/legacy-support/civilwar/civilwar_search.php?sort=portraits", headers=headers)

soup = BeautifulSoup(data.text, "lxml")

anchors = [a for a in soup("a") if a.get("href", "") and "id" in a["href"]]

portraits = []

for portrait in tqdm(anchors):
    
    name = portrait.text.strip()
    
    url = "http://bentley.umich.edu/legacy-support/civilwar/" + portrait["href"]
    
    data = requests.get(url, headers=headers)
       
    soup = BeautifulSoup(data.text, "lxml")
    
    try:
        image = "http://bentley.umich.edu/legacy-support/civilwar/" + soup("img")[0]["src"]
    except:
        image = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Lost_or_Unknown.svg/199px-Lost_or_Unknown.svg.png"
        
    try:
        description = soup("img")[0].find_next("p").text.replace('\n', ' ').replace('\r', '')
    except:
        description = "No description available."
        
    portraits.append([name, description, image, url])
    
    time.sleep(1)

with open("portraits.csv", mode="wb") as f:
    writer = csv.writer(f)
    headers = ["Name", "Description", "Image", "URL"]
    
    writer.writerow(headers)
    writer.writerows(portraits)
    