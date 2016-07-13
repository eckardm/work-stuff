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
    mapfile_unitid_handle = {}
    
    with open(os.path.join("reelmapfiles", collno_mapfile.get(collno, ""))) as file:
        for line in file.readlines():
            mapfile_unitid = line.strip().split(" ")[0]
            handle = line.strip().split(" ")[1]
            
            mapfile_unitids.append(mapfile_unitid)
            
            mapfile_unitid_handle[mapfile_unitid] = handle
    
    for mapfile_unitid in mapfile_unitids:
        tree = etree.parse(os.path.join(path_to_eads, collno_ead.get(collno, "")))
        
        ead_unitids = tree.xpath("//unitid")
        
        for ead_unitid in ead_unitids:
            if ead_unitid.text == "[" + mapfile_unitid + "]":
                print mapfile_unitid.text
                print mapfile_unitid_handle.get(mapfile_unitid, "")
                
                parent_component = ead_unitid.getparent().getparent().getparent()
                
                dao = etree.Element("dao")
                dao.attrib["href"] = "http://hdl.handle.net/" + mapfile_unitid_handle.get(mapfile_unitid, "")
                dao.attrib["show"] = "new"
                dao.attrib["actuate"] = "onrequest"
                
                daodesc = etree.Element("daodesc")
                dao.append(daodesc)
                
                p = etree.Element("p")
                p.text = "[view item]"
                daodesc.append(p)
                
                parent_component.find("did").append(dao)
                
                # with open(os.path.join(path_to_eads, collno_ead.get(collno, ""))), mode="w") as ead_out:
                    # ead_out.write(etree.tostring(tree, encoding='utf-8', xml_declaration=True))
                