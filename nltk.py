import os

for dirpath, dirnames, filenames in os.walk(r'C:\Users\Public\Documents\ES-Test-Files'):
    for filename in filenames:
        print os.path.join(dirpath, filename)