import csv
from pprint import pprint

relative_paths = []

with open("deepBlue_9811_0001-20130323.csv", mode="r") as metadata:
    reader = csv.DictReader(metadata)
    for row in reader: 
        relative_paths += row.get("RELATIVE_PATH", "").split(" | ")
        
import collections
duplicates = [item for item, count in collections.Counter(relative_paths).items() if count > 1]

from collections import defaultdict
duplicate_and_names = defaultdict(list)

 
with open("deepBlue_9811_0001-20130323.csv", mode="r") as metadata:
    reader = csv.DictReader(metadata)
    for row in reader: 
        relative_paths = row.get("RELATIVE_PATH", "").split(" | ")
        for relative_path in relative_paths:
            if relative_path in duplicates:
                duplicate_and_names[relative_path].append(row.get("DC.TITLE", "").replace("Digital Documents - University of Michigan Presidency,", ""))
                
for duplicate, names in duplicate_and_names.iteritems():
    print duplicate
    for name in names:
        print name
    print "\n"

print len(duplicate_and_names)



