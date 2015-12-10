import csv
import cPickle as pickle

converted_files = {}

with open("convertedFiles_9811_0003.csv", mode="rb") as converted_files_csv:
    reader = csv.reader(converted_files_csv)
    next(reader, None)
    for row in reader:
        
        original_location = row[0].split("; ")[1]
        converted_location = row[0].split("; ")[2]
        converted_files[original_location] = converted_location

pickle.dump(converted_files, open("converted_files.p", "wb"))
