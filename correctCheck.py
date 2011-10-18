import enchant, couchdb, re

d = enchant.Dict("en_US")

couch = couchdb.Server()
db = couch['twitter_train']
corpus = couch['corpus']

correct = 0
incorrect = 0

for id in db:
	doc = db[id]
	keys = doc.keys()
	if 'text' in keys:
		words = re.findall('[a-z]+', doc['text'].lower())
	elif 'retweeted_status' in keys:
		words = re.findall('[a-z]+', doc['retweeted_status']['text'])
	else:
		continue
	
	for word in words:
		if d.check(word):
			if corpus.get(word, default=None) == None:
				corpus[word] = {'seen': 1}
			else:
				seen = corpus[word]
				seen['seen'] += 1
				corpus[word] = seen
			

