import csv, couchdb

reader = csv.DictReader(open('anew.csv', 'rb'), delimiter=',')
couch = couchdb.Server()
db = couch['anew']

for line in reader:
	key = line['description-word']
	print(key)
	db[key] = line
