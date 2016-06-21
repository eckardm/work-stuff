import os
from lxml import etree

mlibrary_drop = os.path.join("Q:", "Homefolders", "eckardm", "Desktop", "test")
# mlibrary_drop = os.path.join("R:", "MLibrary Drop", "reel-to-reel")

for root, _, files in os.walk(mlibrary_drop):
    for name in files:
        if name == "dublin_core.xml":
            print root, name
            
            tree = etree.parse(os.path.join(root, name))
            videostreams = tree.xpath("//dcvalue[@element='identifier'][@qualifier='videostream']")
            
            count = 1
            for videostream in videostreams:
                entry_id = videostream.text
                player_id = "1455309" + str(count).zfill(3)
                videostream.text = "https://cdnapisec.kaltura.com/p/1758271/sp/175827100/embedIframeJs/uiconf_id/29300931/partner_id/1758271?autoembed=true&entry_id=" + entry_id + "&playerId=kaltura_player_" + player_id + "&cache_st=1455309475&width=400&height=330&flashvars[streamerType]=auto"
                count += 1
                
                with open(os.path.join(root, name), 'w') as f:
                    f.write(etree.tostring(tree, xml_declaration=True, encoding='utf-8', standalone=False))
