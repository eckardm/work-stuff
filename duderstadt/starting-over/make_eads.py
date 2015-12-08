import csv
import requests
from bs4 import BeautifulSoup
import time

import re

# identify elements in csv
'''
{
    'publisher': '', 
    'dates': '2006/04-2015/10', 
    'dateAdded': '2011-12-23T16:51:58Z', 
    'handle': '2027.42/88898', 
    'bitCount': '1', 
    'title': 'AAU Meeting ', 
    'author': 'Duderstadt, James J. '
}'''

'''
        <c02 level="file">
          <did>
            <physloc>Online</physloc>
            <unittitle>Clippings <unitdate type="inclusive" normal="1961/1990" certainty="approximate">circa 1961-1990</unitdate></unittitle>
            <physdesc>
              <physfacet>.ZIP file</physfacet>
            </physdesc>
            <dao href="http://hdl.handle.net/2027.42/109233" show="new" actuate="onrequest">
              <daodesc>
                <p>[download item]</p>
              </daodesc>
            </dao>
          </did>
          <accessrestrict>
            <p>[Download Access Restricted to BHL Reading Room]</p>
          </accessrestrict>
        </c02>'''
        
with open("data.csv", mode="rb") as dspace_stats:
    reader = csv.DictReader(dspace_stats, dialect="excel-tab")
    next(reader, None)
    csv.list_dialects()
    for row in reader:
        level = "file"
        physloc = "Online"
        unittitle = row["title"]
        # default
        unitdate = ""
        # default
        physfacet = ""
        dao = "http://hdl.handle.net/" + row["handle"]
        daodesc = "[download item]"
        # default
        accessrestrict = None
        
        # i'm a conscientious scraper
        headers = {"user-agent": "Duderstadt Scraper: eckardm at umich (dot) com"}
        full_meta = "http://deepblue.lib.umich.edu/handle/" + row["handle"] + "?show=full"
        data = requests.get(full_meta, headers=headers)
        soup = BeautifulSoup(data.text)
        
        meta_tags = soup("meta")
        for meta_tag in meta_tags:
        
            # get date
            if meta_tag.get("name") == "citation_date":
                unitdate = meta_tag.get("content", "")
            
            # get file extension
            if meta_tag.get("name") == "citation_pdf_url":
                physfacet = meta_tag["content"][-4:].upper() + " file"
                
                # account for restricted files
                if "restricted" in meta_tag["content"]:
                    accessrestrict = "[ER Restricted until July 1, 2030]"

            # i'm a conscientious scraper
            time.sleep(1)

        # make xml

        # delete what's there

        # put in the right spot

        # write a new xml
    