import os
import csv

information_packages = []

for root, _, files in os.walk("C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\original-records"):
 
    information_package = {}

    for name in files:
    
        if name == "Archivist Note":
            continue
    
        information_package = {}
        
        if "Speeches" in root:
            information_package["series"] = "Speeches"
            
            if "1986-1987 Speeches" in root:
                information_package["subseries"] = "1986-1987 Speeches"
            if "1987-1988 Speeches" in root:
                information_package["subseries"] = "1987-1988 Speeches"
            if "1988-1989 Speeches" in root:
                information_package["subseries"] = "1988-1989 Speeches"
            if "1989-1990 Speeches" in root:
                information_package["subseries"] = "1989-1990 Speeches"
            if "1990-1991 Speeches" in root:
                information_package["subseries"] = "1990-1991 Speeches"
            if "1991-92" in root:
                information_package["subseries"] = "1991-92"
            if "1992-1993 Speeches" in root:
                information_package["subseries"] = "1992-1993 Speeches"
            if "1994-1995 Speeches" in root:
                information_package["subseries"] = "1994-1995 Speeches"
            if "1995-1996 Speeches" in root: # don't appear to be in original-records
                information_package["subseries"] = "1995-1996 Speeches"
            if "Athletics Talks" in root:
                information_package["subseries"] = "Athletic Talks-Speeches"
                
            information_package["accessrestrict"] = False
                
        if "Idea Files" in root:
            information_package["series"] = "Idea Files"
            
            if "1986-1987 Ideas" in root:
                information_package["subseries"] = "1986-1987 Ideas"
            if "1987-1988 Ideas" in root:
                information_package["subseries"] = "1987-1988 Ideas"
            if "1988-1989 Ideas" in root:
                information_package["subseries"] = "1988-1989 Ideas"
            if "1989-1990 Ideas" in root:
                information_package["subseries"] = "1989-1990 Ideas"
            if "1990-1991 Ideas" in root:
                information_package["subseries"] = "1990-1991 Ideas"
            if "1991-1992 Ideas" in root:
                information_package["subseries"] = "1991-1992 Ideas"
            if "1992-1993 Ideas" in root:
                information_package["subseries"] = "1992-1993 Ideas"
            if "1993-1994 Ideas" in root:
                information_package["subseries"] = "1993-1994 Ideas"
            if "1994-1995 Ideas" in root:
                information_package["subseries"] = "1994-1995 Ideas"
                
            information_package["accessrestrict"] = True
            
        if "Strategy" in root:
            information_package["series"] = "Strategy"
            information_package["subseries"] = "1986-1997"
            information_package["accessrestrict"] = True
            
        if "Position Papers" in root:
            information_package["series"] = "Position Papers"
            
            if "1986-1987 Position Papers" in root or "1987-1988 Position Papers" in root or "1988-1989 Position Papers" in root or "1989-1990 Position Papers" in root or "1990-1991 Position Papers" in root:
                information_package["subseries"] = "1986-1991 Position Papers"
            elif "1991-1992 Position Papers" in root or "1992-1993 Position Papers" in root or "1993-1994 Position Papers" in root or "1994-1995 Position Papers" in root or "1995-1996 Position Papers" in root:
                information_package["subseries"] = "1991-1996 Position Papers" # what about 1996-1997 Position Papers?
            
            information_package["accessrestrict"] = True
            
        if "Presentations" in root:
            information_package["series"] = "Presentations"
            
            if "1987-1988 Presentations" in root:
                information_package["subseries"] = "1987-1988 Presentations"
            if "1988-1989 Presentations" in root:
                information_package["subseries"] = "1988-1989 Presentations"
            if "1989-1990 Presentations" in root:
                information_package["subseries"] = "1989-1990 Presentations"
            if "1990-1991 Presentations" in root:
                information_package["subseries"] = "1990-1991 Presentations"
            if "1991-1992 Presentations" in root:
                information_package["subseries"] = "1991-1992 Presentations"
            if "1992-1993 Presentations" in root:
                information_package["subseries"] = "1992-1993 Presentations"
            if "1993-1994 Presentations" in root:
                information_package["subseries"] = "1993-1994 Presentations"
            if "1994-1995 Presentations" in root:
                information_package["subseries"] = "1994-1995 Presentations"
            if "1995-1996 Presentations" in root:
                information_package["subseries"] = "1995-1996 Presentations"
            if "1996-1997 Presentations" in root:
                information_package["subseries"] = "1996-1997 Presentations"

            information_package["accessrestrict"] = False
            
        if "Write Files" in root:
            information_package["series"] = "Write Files"
            
            if "1988 and earlier Write" in root:
                information_package["subseries"] = "1988 and earlier Write Files"
            if "1988-1989 Write Files" in root:
                information_package["subseries"] = "1988-1989 Write Files"
            if "1989-1990 Write Files" in root:
                information_package["subseries"] = "1989-1990 Write Files"
            if "1990-1991 Write Files" in root:
                information_package["subseries"] = "1990-1991 Write Files"
            if "1991-1992 Write Files" in root:
                information_package["subseries"] = "1991-1992 Write Files"
            if "1992-1993 Write Files" in root:
                information_package["subseries"] = "1992-1993 Write Files"
            if "1993-1994 Write Files" in root:
                information_package["subseries"] = "1993-1994 Write Files"
            if "1994-1995 Write Files" in root:
                information_package["subseries"] = "1994-1995 Write Files"
            if "1995-1996 Write Files" in root:
                information_package["subseries"] = "1995-1996 Write Files"
            if "1996-1997 Write Files" in root:
                information_package["subseries"] = "1996-1997 Write Files"

            information_package["accessrestrict"] = True
            
        if "Legacy" in root:
            information_package["series"] = "Legacy"
            information_package["subseries"] = "1996"
            information_package["accessrestrict"] = True
            
        if "Digital Images" in root:
            information_package["series"] = "Digital Images"
            information_package["subseries"] = "1996"
            information_package["accessrestrict"] = False
            
        information_package["unittitle"] = name
        
        information_package["original"] = name
        information_package["original_location"] = os.path.join(root, name)
        
        information_packages.append(information_package)
