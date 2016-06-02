from bs4 import BeautifulSoup
import csv

metadata = [
    "Q:\Homefolders\eckardm\Desktop\duderstadt-redux\9811_0001\jjdhtml\JJDLE1.htm",
]

results = []

for metadatum in metadata:
    with open(metadatum, mode="r") as html:
        soup = BeautifulSoup(html, "lxml")
        
        list_items = soup("li")

        for list_item in list_items:
        
            title = list_item.a.text.split(", ")[0].strip()
            try:
                date = list_item.a.text.split(", ")[1].strip()
            except:
                continue
                
            href = list_item.a.get("href", "").replace("/", "\\").replace("..", "Q:\Homefolders\eckardm\Desktop\duderstadt-redux\9811_0001")
            
            results.append([title, date, href])

    with open("metadata.csv", mode="wb") as output:
        writer = csv.writer(output)
        writer.writerows(results)
