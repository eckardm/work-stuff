import os
from lxml import etree


path_to_eads = os.path.join("C:/", "Users", "eckardm", "vandura-test", "Real_Masters_all")
eads = [ead for ead in os.listdir(path_to_eads) if ead.endswith(".xml")]

collno_ead = {}

for ead in eads:
    tree = etree.parse(os.path.join(path_to_eads, ead))
    
    eadid = tree.xpath("/ead/eadheader/eadid")[0]
    collno = eadid.text.strip().split("-")[2]
    
    collno_ead[collno] = ead
 
 
mapfiles = [mapfile for mapfile in os.listdir("reelmapfiles")]
 
collnos = []
collno_mapfile = {}
    
for mapfile in mapfiles:
    with open(os.path.join("reelmapfiles", mapfile)) as file:
        collno = file.readlines()[0].strip().split("-")[0]
        
        collnos.append(collno)
        
        collno_mapfile[collno] = mapfile
        

for collno in collnos:
    print collno_ead.get(collno)

    mapfile_unitids = []
    
    with open(os.path.join("reelmapfiles", collno_mapfile.get(collno, ""))) as file:
        for line in file.readlines():
            mapfile_unitid = line.strip().split(" ")[0]
            
            mapfile_unitids.append(mapfile_unitid)
    
    for mapfile_unitid in mapfile_unitids:
        tree = etree.parse(os.path.join(path_to_eads, collno_ead.get(collno, "")))
        
        ead_unitids = tree.xpath("//unitid")
        
        for ead_unitid in ead_unitids:
            if ead_unitid.text == "[" + mapfile_unitid + "]":
                print ead_unitid.text