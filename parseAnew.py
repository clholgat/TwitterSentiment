import csv, couchdb

reader = csv.DictReader(open('anew.csv', 'rb'), delimiter=',')
couch = couchdb.Server()
db = couch['anew']

for line in reader:
	db.save(line)
