import json
from collections import Counter
from pprint import pprint

occupations = []

with open("../womens_voices.json", mode="r") as f:
    alumnae = json.load(f)
    
    for id_alumna_dict in alumnae:
        for id, alumna in id_alumna_dict.iteritems():
            occupations.append(alumna.get("occupation", ""))

# change the argument (currenlty set to 10) to change the number of unique occupations you want on the list
print "Top Ten Occupations\n===================\n", pprint(Counter(occupations).most_common(10))
            