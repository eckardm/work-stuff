import os
import cPickle as pickle
import shutil

os.mkdir("leftovers")

information_packages = pickle.load(open("information_packages.p", mode="rb"))

leftovers = []

copy_errors = []

for root, _, files in os.walk("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\original-records"):
    for name in files:
        for information_package in information_packages:
            if information_package.get("original_location", "") == os.path.join(root, name):
                if information_package.get("preservation", "") == "n/a" and information_package.get("autopro", "") == "n/a": 
                    leftovers.append(information_package.get("original_location", ""))
               
for leftover in leftovers:
    try:
        shutil.copy(leftover, "leftovers")
    except:
        copy_errors.append(leftover)
        
for copy_error in copy_errors:
    with open("leftovers_copy_errors.txt", mode="a") as errors:
        errors.write(copy_error)
        errors.write("\n")
