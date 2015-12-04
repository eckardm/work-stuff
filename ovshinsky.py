import csv
import os

metadata_filenames = []

with open("deepBlue_2014092_0002.csv", mode="r") as csv_file:
    reader = csv.reader(csv_file)
    
    next(reader, None)
    
    for row in reader:
        if " | " in row[8]:
            metadata_filenames.append(row[8].split(" | ")[0])
            metadata_filenames.append(row[8].split(" | ")[1])
        else:
            metadata_filenames.append(row[8])
            
print len(metadata_filenames)
            
filenames = [
    "Hko Ecd Groundbreak 9 16 05-1.zip",
    "Stanford Ovshinsky 9-23-11-1.zip",
    "Leading The Way-1.zip",
    "OvshinskyPhotographsforNotreDameBook.zip",
    "OvonicFuelCellAdvertisements.zip",
    "ECDUniSolarOpening.zip",
    "WalkerCislerLecture.zip",
    "ECDFamilyOuting.zip",
    "80thBirthdayReminiscences.zip",
    "AkronRoundtable.zip",
    "OvshinskyAutobiographyFiles.zip",
    "OvshinskyWJR760.zip",
    "OvshinskyBerkeley.zip",
    "AkronPressConference.zip",
    "MachineDivision.zip",
    "Ecd2so-1.zip",
    "Ecd Germany 4 18 06-1.mp4",
    "Ovonics Final2-1.mp4",
    "Ovonics Final2-1.zip",
    "Prius - Phase L Video-1.mp4",
    "Prius - Phase L Video-1.zip",
    "OvonicHydrogenPriusWrapupVideo.mpg",
    "Ecd2so-1.mp4",
    "OvshinskyEcology.zip",
    "OvonicsAtWork.mp4",
    "Sro Presentation-1.mp4",
    "Texaco_Ovonic.mpg",
    "OvonicsAtWork.zip",
    "Texaco_Ovonic.zip",
    "EBWR07.pdf",
    "Sro Presentation-1.zip",
    "Hko Ecd Groundbreak 9 16 05-1.mp4",
    "Ovshinsky-NYIT.mp4",
    "Ovshinsky-NYIT.zip",
    "Stanford Ovshinsky 9-23-11-1.mp4",
    "OvshinskyEcology.mp4",
    "Prius Phase lll VideoTake2.mpg",
    "TexacoECD.zip",
    "ECDClosingBell.mp4",
    "ECDClosingBell.zip",
    "Leading The Way-1.mp4",
    "BergmanFreedomRider.mp4",
    "BergmanFreedomRider.zip",
    "Sro Uni Solar Dvd-1.mp4",
    "Sro Uni Solar Dvd-1.zip",
    "Sro Electrichybrid Dvd 4may09-1.zip",
    "Sro Electrichybrid Dvd 4may09-1.mp4",
    "OvshinskyCORE2004.mp4",
    "OvshinskyCORE2004.zip",
    "Ecd Sro Presentation-1.mp4",
    "Ecd Sro Presentation-1.zip",
    "IrisOvshinskyTribute.zip",
    "IrisOvshinskyTribute.mp4",
    "SROCityforYouth.zip",
    "SROCityforYouth.mp4",
    "SROAdlerLecture.zip",
    "SROAdlerLecture.mp4",
    "GMAutoShowHighlights1998.zip",
    "GMAutoShowHighlights1998.mp4",
    "JapansAmericanGenius.mp4",
    "TexacoECD.mp4",
    "OITS2003.mp4",
    "ECDEnergySolutions.mp4",
    "GMHighlightsIacoccaTour.mp4",
    "RoadtotheSun.mp4",
    "OBC1996.mp4",
    "ECDEnergySolutions.zip",
    "JapansAmericanGenius.zip",
    "FutureIsNow.zip",
    "FutureIsNow.mp4",
    "OITS2003.zip",
    "GMHighlightsIacoccaTour.zip",
    "RoadtotheSun.zip",
    "OBC1996.zip",
    "OvonicSolarSolutions.zip",
    "OvonicSolarSolutions.mp4",
    "TransformingTheFuture.zip",
    "TransformingTheFuture.mp4",
    "UnitedSolarOvonicPressConference.zip",
    "UnitedSolarOvonicPressConference.mp4",
    "OBCNewsRelease.zip",
    "OBCNewsRelease.mp4",
    "Ecd Germany 4 18 06-1.zip"
]

print len(filenames)
for i in filenames:
    if i not in metadata_filenames:
        print i