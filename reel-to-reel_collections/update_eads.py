# dallas solved it for me... https://gist.github.com/djpillen/a580862bfdae4ca202b1840b9a64a65e

import os
from lxml import etree
 
collitemno_handle = {}
 
for filename in os.listdir("reelmapfiles"):
    with open(os.path.join("reelmapfiles", filename), mode="r") as file:
        for line in file.readlines():
            collitemno = line.strip().split(" ")[0]
            handle = line.strip().split(" ")[1]
            
            collitemno_handle[collitemno] = handle

path_to_eads = os.path.join("C:/", "Users", "eckardm", "vandura-test", "Real_Masters_all")

for filename in os.listdir(path_to_eads):
    tree = etree.parse(os.path.join(path_to_eads, filename))
    unitids = tree.xpath("//unitid")
    
    for unitid in unitids:
        if unitid:
            if "sr" in unitid.text.lower():
                digfilecalc = unitid.text.strip("[] ")
                
                href = ""
                
                while not href and digfilecalc:
                    if digfilecalc in collitemno_handle:
                        href = "http://hdl.handle.net/" + collitemno_handle.get(digfilecalc)
                        del collitemno_handle[digfilecalc]
                    else:
                        digfilecalc = "-".join(digfilecalc.split("-")[:-1])
                     
                if href:
                    print digfilecalc
                
                    parent_component = unitid.getparent().getparent().getparent()
                    
                    dao = etree.Element("dao")
                    dao.attrib["href"] = href
                    dao.attrib["show"] = "new"
                    dao.attrib["actuate"] = "onrequest"
                    
                    daodesc = etree.Element("daodesc")
                    dao.append(daodesc)
                    
                    p = etree.Element("p")
                    p.text = "[view item]"
                    daodesc.append(p)
                    
                    if not parent_component.find("did").find("dao"):
                        parent_component.append(dao)
            
                        # with open(os.path.join(path_to_eads, filename, mode="w") as ead_out:
                            # ead_out.write(etree.tostring(tree, encoding="utf-8", xml_declaration=True))

if collitemno_handle:
    for collitemno in collitemno_handle:
        print collitemno, handle
        
print len(collitemno_handle)
                