import os

deposit_id = raw_input("Deposit ID: ")

source_directory = os.path.join("X:\deepblue", deposit_id)
target_directory = "S:\MLibrary\DeepBlue"

# make working copy
os.putenv("SOURCE_DIRECTORY", source_directory)

os.makedirs(deposit_id)
os.putenv("TARGET_DIRECTORY", "C:\Users\eckardm\work-stuff\prep_deep_blue_deposit")

os.system("copy_with_teracopy.bat")
