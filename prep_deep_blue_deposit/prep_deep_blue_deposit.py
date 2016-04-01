import os
from openpyxl import load_workbook

deposit_id = raw_input("Deposit ID: ")

source_directory = os.path.join("X:\deepblue", deposit_id)
target_directory = "S:\MLibrary\DeepBlue"

# make working copy
os.putenv("SOURCE_DIRECTORY", source_directory)

os.makedirs(deposit_id)
os.putenv("TARGET_DIRECTORY", "C:\Users\eckardm\work-stuff\prep_deep_blue_deposit")

os.system("copy_with_teracopy.bat")

# make simple archive format
# make archive_directory
os.rename(deposit_id, "archive_directory")

metadata = [filename for filename in os.listdir("archive_directory") if filename.startswith("deepBlue_")][0]

wb = load_workbook(filename=os.path.join("archive_directory", metadata), read_only=True, use_iterators=True)
ws = wb["Sheet1"]

counter = 1

for row in ws.iter_rows(row_offset=1):
    
    # make items
    item = "item_"
    number = str(counter).zfill(3)
    item = item + number
    counter += 1
    os.makedirs(os.path.join("archive_directory", item))
    