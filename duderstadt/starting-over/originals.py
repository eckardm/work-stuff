import os
import csv

originals = {}
for root, _, names in os.walk("Y:\unprocessed\9811_0001\data\original-records"):
    for name in names:
        originals[name] = root

filenames_in_metadata = []
with open("deepBlue_9811_0003.csv", mode="rb") as metadata:
    reader = csv.reader(metadata)
    next(reader, None)
    for row in reader:
        dc_filename_title = row[8]
        filenames_in_metadata.append(dc_filename_title)

for original in originals:
    if original not in filenames_in_metadata:
        with open("print.text", mode="a") as output:
            output.write(original + " " + originals[original] + "\n")