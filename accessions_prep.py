import csv

in_fname = 'accessions-20150710-original.csv'
out_fname = 'accessions-20150710-processed.csv'

# open input csv for reading
input = open(in_fname, 'rb')

# create output csv for writing
output = open(in_fname, 'wb')

# header list
headers = [AccDescription, AccessionDate, AccessionID, Acknowledged, CollectionID, Digital, DigitalSize, DigitalSizeType, DonorBoxList, DonorNumberID, DonorType, FileLink, GivenThrough, HasFile, LinearFeet, MHCType, StaffReceived, ThankYouNote, Unit, UnprocessedLocation, FirstName, LastName, MiddleName, OrganizationOrUnit, Suffix, Title, DonorNumber, Copyright, Notes, Status, Difficulty, PercentageToRetain, PriorityLevel, ProcessNote, Processor, Status, Note, Type, Description, DestructionDate, Location, ReturnDate, Type, Volume, BoxRange, DiskSite, FullPath, ShelfRange, Site, TempLocNote)

writer = csv.writer(output)

for header in headers:
    writer.writerow(header)

for row in csv.reader(input)
    if row:
            writer.writerow(row)

input.close()
output.close()