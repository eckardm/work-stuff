import os
import csv

# make directories in 9811_0003 for others Legacy, Presentation, Speeches
series_list = ["C:\Users\eckardm\work-stuff\duderstadt\9811_0003\Legacy", "C:\Users\eckardm\work-stuff\duderstadt\9811_0003\Presentations", "C:\Users\eckardm\work-stuff\duderstadt\9811_0003\Speeches"]
#for series in series_list:
#os.mkdir(series)

# go through and if DC.TITLE.FILENAME but not DC.TITLE, add to folder based on first part of DC.TITLE.FILENAME
with open("deepBlue_9811_0003.csv", mode="rb") as metadata:
    reader = csv.reader(metadata)
    next(reader, None)
    for row in reader:
        dc_title = row[1]
        dc_title_filename = row[8]
        if dc_title_filename and not dc_title:
            filenames = dc_title_filename.split(" | ")
            for filename in filenames:
                if filename.startswith("Legacy"):
                    os.rename(os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0003", filename), os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0003\Legacy", filename))
                if filename.startswith("Presentations"):
                    os.rename(os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0003", filename), os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0003\Presentations", filename))
                if filename.startswith("Speeches"):
                    os.rename(os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0003", filename), os.path.join("C:\Users\eckardm\work-stuff\duderstadt\9811_0003\Speeches", filename))

# manual zipping and adding of metadata
