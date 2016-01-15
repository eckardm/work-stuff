import csv
import requests
from bs4 import BeautifulSoup
import time
import pickle

'''
<c02 level="file">
  <did>
    <physloc>Online</physloc>
    <unittitle>Camp Shelby (basic training and MP training) <unitdate type="inclusive" normal="2011/2012">2011-2012</unitdate></unittitle>
    <physdesc>
      <physfacet>.ZIP file</physfacet>
    </physdesc>
    <dao href="http://hdl.handle.net/2027.42/101933" show="new" actuate="onrequest">
      <daodesc>
        <p>[view item]</p>
      </daodesc>
    </dao>
  </did>
  <accessrestrict>
    <p>[SR RESTRICTED until July 1 <date type="restriction" normal="2056-07-01">2056</date>]</p>
  </accessrestrict>
</c02>'''

headers = {"user-agent": "Duderstadt scraper v.0.1 - please contact eckardm@umich.edu if there are any issues"}

metadata_list = []

count = 1

with open("data.txt", mode="rb") as csvfile:
    reader = csv.DictReader(csvfile, delimiter="\t")
    for row in reader:
        full_item_record = "http://deepblue.lib.umich.edu/handle/" + row["handle"] + "?show=full"
        
        print "(" + str(count).zfill(4) + "/1316) Getting metadata for " + row["handle"] + "..."

        metadata_dictionary = {}
        
        data = requests.get(full_item_record, headers=headers)
        soup = BeautifulSoup(data.text, "lxml")
        
        metadata_dictionary["unittitle"] = soup.find("td", text="dc.title").find_next("td").text.encode("utf-8")
        metadata_dictionary["unitdate"] = soup.find("td", text="dc.date.issued").find_next("td").text
        
        file_extensions = []
        for bitstream_url in soup.find_all("td", text="dc.description.bitstreamurl"):
            file_extensions.append(bitstream_url.find_next("td").text[-4:].upper())
        file_extensions = list(set(file_extensions))
        if len(file_extensions) == 1:
            physfacet = file_extensions[0] + " file"
        else:
            physfacet = ", ".join(file_extensions[0:-1]) + " and " + file_extensions[-1] + " files"
        metadata_dictionary["physfacet"] = physfacet
        
        metadata_dictionary["dao"] = soup.find("td", text="dc.identifier.uri").find_next("td").text
        
        if soup.find("td", text="dc.rights.access"):
            metadata_dictionary["accessrestrict"] = soup.find("td", text="dc.rights.access").find_next("td").text
            
        metadata_list.append(metadata_dictionary)
        
        # from robots.txt
        time.sleep(15)
        count += 1

pickle.dump(metadata_list, open("metadata.p", mode="wb"))
