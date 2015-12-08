import os
import csv

name_list = []
for root, _, files in os.walk("C:\Users\eckardm\work-stuff\duderstadt\9811_0003"):
    for name in files:
        new_name = "-".join(root.split("\\")[6:]) + "-" + name
        
        # renamedFiles_9811_0003
        os.rename(os.path.join(root, name), os.path.join(root, new_name))
        
        # log
        with open("renamedFiles_9811_0003.csv", "ab") as output:
            writer = csv.writer(output)
            writer.writerow([name + " --> " + new_name])
