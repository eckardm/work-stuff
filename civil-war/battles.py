import requests
from bs4 import BeautifulSoup
import time
import csv
from tqdm import *

headers = {"user-agent": "Battle scraper v.0.1 - please contact eckardm@umich.edu if there are any issues"}
data = requests.get("http://bentley.umich.edu/legacy-support/civilwar/civilwar_search.php?sort=battles", headers=headers)

soup = BeautifulSoup(data.text, "lxml")

locations = {
	"Fort Fisher, N.C.": "Kure Beach, NC", 
    "Fort Donelson, Tenn.": "Dover, TN", 
	"Chattanooga, Tenn.": "Chattanooga, TN", 
	"Fort Blakely, Ala.": "Spanish Fort, AL", 
    "Shiloh, Tenn.": "Shiloh, TN", 
    "Pea Ridge, Ark.": "Pea Ridge, AR", 
    "Champion Hill, Miss.": "Corinth, MS", 
    "Jonesborough, Ga.": "Jonesboro, GA", 
    "Glorieta Pass, N.M.": "Glorieta, NM", 
    "Vicksburg, Miss.": "Vicksburg, MS", 
	"Fort Stedman, Va.": "Petersburg, VA", 
    "Franklin, Tenn.": "Franklin, TN", 
    "Forts Jackson and St. Phillip, La.": "Buras-Triumph, LA", 
    "Bentonville, N.C.": "Bentonville, NC", 
    "Corinth, Miss.": "Corinth, MS", 
    "Stones River, Tenn.": "Murfreesboro, TN", 
    "Nashville, Tenn.": "Nashville, TN", 
    "Spotsylvania Court House, Va.": "Spotsylvania Courthouse, VA", 
    "Mobile Bay, Ala.": "Mobile Bay, AL", 
    "Fort Sumter, S.C.": "Charleston, SC", 
    "Cedar Creek, Va.": "Cedar Creek, Virginia", 
    "Crater, Va.": "Crater, Virginia", 
}

normal = {
    "Sept. 16-Sept. 18, 1862": "1862-09-16/1862-09-18", 
    "Apr. 9, 1865": "1865-04-09/1865-04-09", 
    "Mar. 19-Mar. 21, 1865": "1865-03-19/1865-03-21", 
    "Oct. 19, 1864": "1864-10-19/1864-10-19", 
    "May 16, 1863": "1863-05-16/1863-05-16", 
    "Apr. 30-May 6, 1863": "1863-04-30/1863-05-06", 
    "Nov. 23-Nov. 25, 1863": "1863-11-23/1863-11-25", 
    "Sept. 18-Sept. 20, 1863": "1863-09-18/1863-09-20", 
    "May 31-June 12, 1864": "1864-05-31/1864-06-12", 
    "Oct. 3-Oct. 4, 1862": "1862-10-03/1862-10-04", 
    "July 30, 1864": "1864-07-30/1864-07-30", 
    "Apr. 1, 1865": "1865-04-01/1865-04-01/1", 
    "Apr. 2-Apr. 9, 1865": "1865-04-02/1865-04-09", 
    "Feb. 11-Feb. 16, 1862": "1862-02-11/1862-02-16", 
    "Jan. 13-Jan. 15, 1865": "1865-01-13/1865-01-15", 
    "Mar. 25, 1865": "1865-03-25/1865-03-25", 
    "Apr. 12-Apr. 14, 1861": "1861-04-12/1861-04-14", 
    "Apr. 16-Apr.28, 1862": "1862-04-16/1862-04-28", 
    "Nov. 30, 1864": "1864-11-30/1864-11-30", 
    "Dec. 11-Dec. 15, 1862": "1862-12-11/1862-12-15", 
    "June 27, 1862": "1862-06-27/1862-06-27", 
    "July 1-July 3, 1863": "1863-07-01/1863-07-03", 
    "Mar. 26-Mar. 28, 1862": "1862-03-26/1862-03-28", 
    "Aug. 31-Sept. 1, 1864": "1864-08-31/1864-09-01", 
    "July 1, 1862": "1862-07-01/1862-07-01", 
    "July 21, 1861": "1861-07-21/1861-07-21", 
    "Aug. 28-Aug. 30, 1862": "1862-08-28/1862-08-30", 
    "Apr. 8, 1864": "1864-04-08/1864-04-08", 
    "Aug. 12-Aug. 22, 1864": "1864-08-12/1864-08-22", 
    "Dec. 15-Dec. 16, 1864": "1864-12-15/1864-12-16", 
    "Feb. 28-Apr. 8, 1862": "1862-02-28/1862-04-08", 
    "Sept. 19, 1864": "1864-09-19/1864-09-19", 
    "Mar. 6-Mar. 8, 1862": "1862-03-06/1862-03-08", 
    "Oct. 8, 1862": "1862-10-08/1862-10-08", 
    "June 15-June 18, 1864": "1864-06-15/1864-06-18", 
    "Apr. 2, 1865": "1865-04-02/1865-04-02", 
    "May 21-July 9, 1863": "1863-05-21/1863-07-09", 
    "Apr. 6-Apr. 7, 1862": "1862-04-06/1862-04-07", 
    "May 8-May 21, 1864": "1864-04-08/1864-04-21", 
    "Dec. 31, 1862-Jan. 2, 1863": "1862-12-31/1863-01-02", 
    "May 18-July 4, 1863": "1863-05-18/1863-07-04", 
    "Oct. 23, 1864": "1864-10-23/1864-10-23", 
    "May 5-May 7, 1864": "1864-05-05/1864-05-07", 
    "Aug. 10, 1861": "1861-08-10/1861-08-10", 
    "May 25, 1862": "1862-05-25/1862-05-25", 
}

table_rows = soup("tr")
table_rows.pop(0)

battles = []

for table_row in tqdm(table_rows):
    table_data = table_row("td")
    
    battle = table_data[0].text.replace("(First)", "").replace("(Second)", "").strip()
    
    location = table_data[0].text.replace("(First)", "").replace("(Second)", "").strip()
    if location in locations:
        location = locations[location]
    
    date = table_data[1].text.strip()
    begin = normal[date].split("/")[0]
    end = normal[date].split("/")[1]
    
    collections = "http://bentley.umich.edu/legacy-support/civilwar/" + table_data[2]("a")[0]["href"]
    
    battle_id = int(table_data[2]("a")[0]["href"].split("=")[1])
    
    # main eastern theater battle_id=1-21
    # main western theater battle_id=22-35
    # lower seaboard and gulf approaches battle_id=36-40
    # trans-mississippi theaters battle_id=41-45
    
    if battle_id > 0 and battle_id <= 21:
        theater = "Main Eastern Theater"
    elif battle_id <= 35:
        theater = "Main Western Theater"
    elif battle_id <= 40:
        theater = "Lower Seaboard Theater and Gulf Approaches"
    else:
        theater = "Trans-Mississippi Theater"
    
    battles.append([location, battle, theater, date, begin, end, collections])
        
    time.sleep(1)

with open("battles.csv", mode="wb") as f:
    writer = csv.writer(f)
    headers = ["Location", "Battle", "Theater", "Date", "Begin", "End", "Collections"]
    
    writer.writerow(headers)
    writer.writerows(battles)
    