from lxml import etree
from lxml.builder import E
import os
import re
from operator import itemgetter

tree = etree.parse("duderst.xml")
# tree = etree.parse(os.path.join("C:/", "Users", "eckardm", "vandura", "Real_Masters_all", "duderst.xml"))

faculty_archives_items = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[2]/c03")
faculty_archives_series = tree.xpath("/ead/archdesc[1]/dsc[1]/c01[2]/c02[2]")[0]

reordered_faculty_archives = []

for faculty_archive_item in faculty_archives_items:

    reordered_faculty_archive = {}

    unittitle = faculty_archive_item.xpath("did/unittitle")[0].text.encode("utf-8").rstrip(", ")
    # account for unittitles with extra dates coming out of deep blue
    if re.search(r',\s\d{4}$', unittitle) and unittitle != "Basketball Bust -- March 28, 1989":
        unittitle = ", ".join(unittitle.split(", ")[:-1])
    
    sorted_unittitle = unittitle
    if sorted_unittitle.startswith("A ") or sorted_unittitle.startswith("An ") or sorted_unittitle.startswith("The "):
        sorted_unittitle = " ".join(sorted_unittitle.split(" ")[1:])
    
    reordered_faculty_archive["unittitle"] = unittitle
    reordered_faculty_archive["sorted_unittitle"] = sorted_unittitle
    reordered_faculty_archive["unitdate"] = faculty_archive_item.xpath("did/unittitle/unitdate")[0].text
    reordered_faculty_archive["normal"] = faculty_archive_item.xpath("did/unittitle/unitdate")[0].attrib["normal"]
    reordered_faculty_archive["href"] = faculty_archive_item.xpath("did/dao")[0].attrib["href"]
    
    reordered_faculty_archives.append(reordered_faculty_archive)

reordered_faculty_archives = sorted(reordered_faculty_archives, key=itemgetter("normal", "sorted_unittitle"))

for faculty_archive_item in faculty_archives_items:
    parent = faculty_archive_item.getparent()
    parent.remove(faculty_archive_item)

'''
<c03 level="file">
<did>
  <physloc>Online</physloc>
  <unittitle>Preparing Future Faculty for Future Universities, <unitdate type="inclusive" normal="2001-01-12">1/12/2001</unitdate></unittitle>
  <dao show="new" actuate="onrequest" href="http://hdl.handle.net/2027.42/89146">
    <daodesc>
      <p>[view item]</p>
    </daodesc>
  </dao>
</did>
</c03>'''

for reordered_faculty_archive in reordered_faculty_archives:
    c03 = E.c03(
        E.did(
            E.physloc("Online"),
            E.unittitle(reordered_faculty_archive.get("unittitle", "").decode("utf-8") + ", ", 
                E.unitdate(reordered_faculty_archive.get("unitdate", ""), type="inclusive", normal=reordered_faculty_archive.get("normal", ""))
            ),
            E.dao(
                E.daodesc(
                    E.p("[view item]")
                ),
                show="new", actuate="onrequest", href=reordered_faculty_archive.get("href", "")
            )
        ),
    level="file"
    )
    
    faculty_archives_series.append(c03)
    
with open("duderst-UPDATE.xml", mode='w') as ead_out:
    ead_out.write(etree.tostring(tree, encoding='utf-8', xml_declaration=True, pretty_print=True))