import csv

print "Creating DROID dictionary..."

file_path_and_format_name = {}

with open("DROID_9811_0001.csv", mode="rb") as droid:
    reader = csv.DictReader(droid)
    for row in reader:
        file_path = row["FILE_PATH"]
        format_name = row["FORMAT_NAME"]
        if len(format_name) == 0:
            format_name = "Original version: Original format not identified"
        if format_name != "Original version: Original format not identified":
            format_name = "Original version: " + format_name
        file_path_and_format_name[file_path] = format_name

print "Updating Deep Blue metadata..."

metadata_list = []

with open("deepBlue_9811_0001.csv", mode="rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if "C:\Users\eckardm\work-stuff\duderstadt" + row[8].split(" | ")[0] in file_path_and_format_name:
            if len(row[9]) > 0:
                row[9] = row[9].replace("Original version", file_path_and_format_name["C:\Users\eckardm\work-stuff\duderstadt" + row[8].split(" | ")[0]])
            else:
                row[9] = file_path_and_format_name["C:\Users\eckardm\work-stuff\duderstadt" + row[8].split(" | ")[0]]
        with open("deepBlue_9811_0001-updated.csv", mode="ab") as csvfile_updated:
            writer = csv.writer(csvfile_updated)
            writer.writerow(row)
    
print "Alright, we're done!"
    