import csv
from datetime import datetime
import os
from tqdm import *

executive_board_metadata = r"T:\Rackham_2\ExecutiveBoard\Rackham_Executive_Board.csv"
program_files_metadata = r"T:\Rackham_2\ProgramFiles\Program_Files.csv"

cut_off_date = "2014-11"

def check_created_and_modified(metadata):
    
    with open(metadata, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Created'] != row['Modified'] and datetime.strptime(row['Created'].split()[0], "%m/%d/%Y") < datetime.strptime(cut_off_date, "%Y-%m") and datetime.strptime(row['Modified'].split()[0], "%m/%d/%Y") > datetime.strptime(cut_off_date, "%Y-%m"):
                print 'Check:', metadata, row['Name'], row['Created'], row['Modified']
                exit()

check_created_and_modified(executive_board_metadata)
check_created_and_modified(program_files_metadata)

executive_board_directory = r"T:\Rackham_2\ExecutiveBoard"
program_files_directory = r"T:\Rackham_2\ProgramFiles"

def remove_redundant_files(metadata, directory):
    
    files_to_remove = []
    
    with open(metadata, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if datetime.strptime(row['Created'].split()[0], "%m/%d/%Y") < datetime.strptime(cut_off_date, "%Y-%m"):
                files_to_remove.append(row['Name'])
    
    for root, dirs, files in tqdm(os.walk(directory)):
        for file in files:
            if file in files_to_remove:
                os.remove(os.path.join(root, file))

remove_redundant_files(executive_board_metadata, executive_board_directory)
remove_redundant_files(program_files_metadata, program_files_directory)
