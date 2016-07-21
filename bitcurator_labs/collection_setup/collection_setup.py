import os
import pickle
from bs4 import BeautifulSoup

collno_and_collname = {}

if os.path.isfile("collno_and_collname.p"):
    pkl_file = open("collno_and_collname.p", mode="rb")
    collno_and_collname = pickle.load(pkl_file)

new_collno_and_collname = {}

collno = raw_input("Collection Number: ")

collname = ""
if collno in collno_and_collname:
    collname = collno_and_collname.get(collno, "")
    print "Collection Name/Description:", collname
else:
    collname = raw_input("Collection Name/Description: ")
    new_collno_and_collname[collno] = collname
    
barcode = raw_input("Item Barcode: ")

print "The most recent images in the Logitech Webcam folder will be copied and used as media images."

if new_collno_and_collname:
    collno_and_collname.update(new_collno_and_collname)

output = open("collno_and_collname.p", mode="wb")
pickle.dump(collno_and_collname, output)

if len(os.listdir(os.path.join("C:/", "Users", "eckardm", "Pictures", "Logitech Webcam"))) == 0:
    do_you_want_to_continue = raw_input("The webcame directory appears to have no media images. Do you want to continue? ")
    if do_you_want_to_continue == "Yes":
        pass
    else:
        exit()

if os.path.isdir(os.path.join("C:/", "Users", "eckardm", "BHL", "Collections Processing", collno + "-" + collname)) is False:
    os.mkdir(os.path.join("C:/", "Users", "eckardm", "BHL", "Collections Processing", collno + "-" + collname))

os.mkdir(os.path.join("C:/", "Users", "eckardm", "BHL", "Collections Processing", collno + "-" + collname, barcode))
    
os.mkdir(os.path.join("C:/", "Users", "eckardm", "BHL", "Collections Processing", collno + "-" + collname, barcode, "MetaData"))

soup = BeautifulSoup(open("media-removal.html", mode="r"), "lxml")
soup(class_="barcode")[0].contents[0].replace_with("A" + barcode + "A")
soup(class_="codenumber")[0].contents[0].replace_with(barcode)

html = soup.prettify("utf-8")
with open(os.path.join("C:/", "Users", "eckardm", "BHL", "Collections Processing", collno + "-" + collname, barcode, "MetaData", "media-removal.html"), mode="w") as media_removal:
    media_removal.write(html)

with open(os.path.join("C:/", "Users", "eckardm", "BHL", "Collections Processing", collno + "-" + collname, barcode, "MetaData", "notes.txt"), mode="w") as media_removal:
    media_removal.write("This is a simple template to record information about any appraisal and processing decisions made with regards to digital media.\n\n")
    media_removal.write("Collection ID: " + collno + "\n\n")
    media_removal.write("Media Barcode: " + barcode + "\n\n")
    media_removal.write("Media Description: \n\n")
    media_removal.write("Brief summary of contents: \n\n")
    media_removal.write("Archival Hierarchy (i.e., folder where media was found, if applicable): \n\n")
    media_removal.write("Suggested intellectual arrangement (if known): \n\n")
    media_removal.write("Processing notes: \n\n")
    media_removal.write("Files / Directories to exclude: \n\n")

for image in os.listdir(os.path.join("C:/", "Users", "eckardm", "Pictures", "Logitech Webcam")):
    os.system('convert "' + os.path.join("C:/", "Users", "eckardm", "Pictures", "Logitech Webcam", image) + '" -fuzz 25% -trim -modulate 110 "' + os.path.join("C:/", "Users", "eckardm", "BHL", "Collections Processing", collno + "-" + collname, barcode, "MetaData", image) + '"')
    os.remove(os.path.join("C:/", "Users", "eckardm", "Pictures", "Logitech Webcam", image))
