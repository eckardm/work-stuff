import beautifulsoup
import json

# parse link to look for lccn id
link = 'http://id.loc.gov/authorities/names/n50001506'
lccn_id = link.rsplit('/')[-1]

# concatenate lccn id to viaf uri just links url
lccn_id_to_viaf_uri_base_url = 'http://www.viaf.org/viaf/lccn/'
json = '/justlinks.json'
lccn_id_to_viaf_uri = lccn_id_to_viaf_uri_base_url + lccn_id
lccn_id_to_viaf_uri_json = lccn_id_to_viaf_uri + json

# find the en.wikipedia link

# if there is one, open and parse the wikipedia url, or just skip

    # grab the first paragraph
    
    # if it's there, grab the image (and credits?)

