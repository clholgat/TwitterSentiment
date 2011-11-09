import couchdb, enchant, re
from stemming.porter2 import stem

d = enchant.Dict("en_US")

couch = couchdb.Server()
db = couch['twitter_train']
anew = couch['anew']


for id in db:
	tweet = db[id]
	keys = tweet.keys()
	if 'corrected' in keys:
		words = re.findall('[a-z]+', tweet['corrected'].lower())
	else:
		continue
		
	sentimentWords = {}
	for word in words:
		if d.check(word):
			sentiment = anew.get(word, default=None)
			if sentiment:
				sentimentWords[word] = sentiment
			else:
				stemmed = stem(word)
				for doc in anew:
					 if anew[doc]['descripting'] == stemmed:
					 	sentimentWords[word] = anew[doc]
					 	break
					 else:
					 	continue
			tweet['sentimentWords'] = sentimentWords
			db[id] = tweet
