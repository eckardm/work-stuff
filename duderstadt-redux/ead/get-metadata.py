import csv
from datetime import *
import pickle

'''
<c02 level="file">
  <did>
    <physloc>Online</physloc>
    <unittitle>Camp Shelby (basic training and MP training) <unitdate type="inclusive" normal="2011/2012">2011-2012</unitdate></unittitle>
    <physdesc> <-- OPTIONAL
      <physfacet>.ZIP file</physfacet> <-- OPTIONAL
    </physdesc> <-- OPTIONAL
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

metadata_list = []

with open("DuderestadtFAData.csv", mode="rb") as report:
    reader = csv.DictReader(report)
    for row in reader:
        
        metadata_dictionary = {}
                
        unittitle = ""
        if row.get("IsPartOf", ""):
            unittitle = row.get("IsPartOf", "") + " - " + row.get("Title", "")
        else:
            unittitle = row.get("Title", "")
        metadata_dictionary["unittitle"] = unittitle
        
        unitdate = ""
        if "/" in unitdate:
            unitdate = strptime(row.get("DateIssued", ""), "%m/%d/%Y").strftime("%Y-%m-%d")
        else:
            unitdate = row.get("DateIssued", "")
        print unitdate
        metadata_dictionary["unitdate"] = unitdate
        
        dao = row.get("Uri", "")
        metadata_dictionary["dao"] = dao
        
        accessrestrict = ""
        if row.get("rights", "") and row.get("rights", "") != "This content is open for research.":
            accessrestrict = row.get("rights", "")
        metadata_dictionary["accessrestrict"] = accessrestrict
                
        metadata_list.append(metadata_dictionary)
        
pickle.dump(metadata_list, open("metadata.p", mode="wb"))
