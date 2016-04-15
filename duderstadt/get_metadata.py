import os

paths = ["C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\jjd_closed", "C:\Users\eckardm\work-stuff\duderstadt\9811_0001\data\jjdhtml"]

# skip these
skip_list = [
    "Use of Materials",
    "Conditions of Use",
    "Copyright",
    "Suggested Citation",
    "University of Michigan",
    "Subseries",
    "Files migrated to PDF/A",
]

# hardcode these
known_errors = [
    ('Elements of Campaign"5/16/89', "Elements of Campaign", "5/16/89"),
    ("Teaching and Research 2.12/14/91", "Teaching and Research 2.1", "2/14/91"),
    ("State of Univ 1992 3, .11/6/93", "State of Univ 1992 3.1", "1/6/93"),
    ("Strategic Initiatives and . , .2/9/95", "Strategic Initiatives and...", "2/9/95"),
    ("DC Notes-9/12. 9/12/90", "DC Notes-9/12", "9/12/90"),
    ("ITI Followup. 12/20/90", "ITI Followup", "12/20/90"),
    ("Teeter , (7/10/91)7/10/91", "Teeter (7/10/91)", "7/10/91"),
    ("Family Community Center", "Family Community Center", "undated"),
    ("OUE Memo 7/2, 7/92", "OUE Memo", "7/2/92"),
    ("Progress Report , 1.211/27/92", "Progress Report 1.2", "1/27/92"),
    ("GUIR Presentation8/28/96", "GUIR Presentation", "8/28/96"),
    ("New Faculty Welcome, 2.08/30/87", "New Faculty Welcome, 2.0", "8/30/87"),
    ("Football Building Kickoff2, /17/89", "Football Building Kickoff", "2/17/89"),
    ("Lagatus, 6/89", "Lagatus", "6/89"),
    ("Rotary5, /9/89", "Rotary", "5/9/89"),
    ("Alumni Talks--Summer 1989, /20/89", "Alumni Talks--Summer 1989", "1989"),
    ("Bo 12/13/89", "Bo", "12/13/89"),
    ("MLK Closing, 1/151/14/90", "MLK Closing", "1/15/90"),
    ("MLK Welcome, 1/141/14/90", "MLK Welcome", "1/14/90"),
    ("Science Education, 2.13/1/90", "Science Education, 2.1", "3/1/90"),
    ("State of Univ. l0/2/89, 3/", "State of Univ.", "10/2/89"),
    ("a) Introductions 3/11/90", "a) Introductions", "3/11/90"),
    ("Public Education 4.0 9/8/90", "Public Education 4.0", "9/8/90"),
    ("Parents Weekend, 3.0 10/27/90", "Parents Weekend, 3.0", "10/27/90"),
    ("Appro Hearings, 2.0 3/25/91", "Appro Hearings, 2.0", "3/25/91"),
    ("Appro Hearings 3.0, (Actual) 3/27/91", "Appro Hearings 3.0, (Actual)", "3/27/91"),
    ("Fresh Convocation 6.0", "Fresh Convocation 6.0", "undated"),
    ("6-1 Table of Color %5/16/96", "6-1 Table of Color", "5/16/96"),
    ("3-11 ProfPublics color5/29/96", "3-11 ProfPublics color", "5/29/96"),
    ("7-9 WomFaculty color5/31/96", "7-9 WomFaculty color", "5/31/96"),
    ("SAC-26/8/96", "SAC-2", "6/8/96"),
    ("SAC-16/8/96", "SAC-1", "6/8/96"),
]

def fix_known_errors(original, title, date, anchor):
    known_error_metadata_dictionary = {}
    known_error_metadata_dictionary["title"] = title
    known_error_metadata_dictionary["date"] = date
    known_error_metadata_dictionary["href"] = anchor["href"]
    
    return known_error_metadata_dictionary

metadata_list = []

for path in paths:
    filenames = [filename for filename in os.listdir(path) if filename.endswith(".htm")]
    for filename in filenames:
        with open(os.path.join(path, filename), mode="rb") as html:
            soup = BeautifulSoup(html)
            
            # see "skip these" above
            anchors = [anchor for anchor in soup("a") if not any(skip_item in anchor.text for skip_item in skip_list)] 
            
            for anchor in anchors:
            
                metadata_dictionary = {}
                
                # skip these too
                if "#" in anchor.get("href", "") or anchor.get("href", "").endswith(".htm"):
                    continue
                
                # see "hardcode these" above
                else:
                    for original, title, date in known_errors:
                        if anchor.text.strip() == original:
                            metadata_dictionary = fix_known_errors(original, title, date, anchor)
                
                # hardcode these too
                if "Ed for Change" in anchor.text and '"' in anchor.text and "3/22/87" in anchor.text:
                    metadata_dictionary["title"] = "Ed for Change"
                    metadata_dictionary["date"] = "3/22/87"
                    metadata_dictionary["href"] = anchor["href"]
                elif "Nursing" in anchor.text and '"' in anchor.text and "6/11/87" in anchor.text:
                    metadata_dictionary["title"] = "Nursing"
                    metadata_dictionary["date"] = "6/11/87"
                    metadata_dictionary["href"] = anchor["href"]
                            
                if not metadata_dictionary:
                    metadata_dictionary["title"] = re.findall("(.*)(?=\,\s*\d{1,2}\/\d{1,2}\/\d{1,2})", anchor.text.strip())[0]
                    metadata_dictionary["date"] = re.findall("(\d{1,2}\/\d{1,2}\/\d{1,2})$", anchor.text.strip())[0]
                    metadata_dictionary["href"] = anchor["href"]
                                    
                metadata_list.append(metadata_dictionary)

pickle.dump(metadata_list, open("metadata.p", "wb"))
