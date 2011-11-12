import csv, couchdb
from pickle import Pickler


def parse(anew):
	reader = csv.DictReader(open(anew, 'rb'), delimiter=',')
	#couch = couchdb.Server()
	#db = couch['anew']
	anewDict = {}
	fp = file('anew.pickle','w+')

	for line in reader:
		key = line['descripting']
		anewDict[key] = {'valence-mean': float(line['valence-mean']),'valence-SD': float(line['valence-SD']),'arousal-mean':float(line['arousal-mean']),'arousal-SD': float(line['arousal-SD']),'dominance-mean':float(line['dominance-mean']),'dominance-SD': float(line['dominance-SD']),'word-freq': float(line['word-freq'])}
	
	Pickler(fp).dump(anewDict)
