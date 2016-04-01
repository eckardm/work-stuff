import os
from openpyxl import load_workbook

deposit_id = raw_input("Deposit ID: ")

source_directory = os.path.join("X:\deepblue", deposit_id)
target_directory = "S:\MLibrary\DeepBlue"

'''
# make working copy
os.putenv("SOURCE_DIRECTORY", source_directory)

os.makedirs(deposit_id)
os.putenv("TARGET_DIRECTORY", "C:\Users\eckardm\work-stuff\prep_deep_blue_deposit")

os.system("copy_with_teracopy.bat")

# make simple archive format
# make archive_directory
os.rename(deposit_id, "archive_directory")'''

    
    