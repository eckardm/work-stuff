import csv

users = []

with open(r'C:\Users\Public\Documents\server-logs\bhlead_201509_semi_anon_parsed-noBHL.csv', 'rb') as csv_file:
	reader = csv.reader(csv_file)
	for row in reader:
		next(reader, None)
		user = row[0]
		if user not in users:
			users.append(user)

print len(users)

totals = 0
collections = 0

for i in users:
	total = 0
	collection = 0
	with open(r'C:\Users\Public\Documents\server-logs\bhlead_201509_semi_anon_parsed-noBHL.csv', 'rb') as csv_file:
		reader = csv.reader(csv_file)
		for row in reader:
			next(reader, None)
			if row[0] == i:
				if 'GET' in row[2]:
					if 'didno' in row[2].split(' ')[1]:
						total += 1
						if ';' not in row[2].split('didno')[1]:
							collection += 1
	totals += total
	collections += collection
	print i
	print 'total: ', total
	print 'collection: ', collection

print totals
print collections

print 'average total', totals / len(users)
print 'average times they went to collection', collections / len(users)



