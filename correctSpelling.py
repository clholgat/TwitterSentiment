import couchdb, enchant, re, operator

couch = couchdb.Server()
db = couch['twitter_train']
corpus = couch['corpus']
d = enchant.Dict("en_US")

map_fun = '''function(doc){
	if(doc.corrected == undefined){
		emit(doc._id, null);
	}
}'''

def getCommon(original, suggest):
	order = {}
	for word in suggest:
		if corpus.get(word, default=None):
			order[word] = corpus[word]['seen']
		else:
			order[word] = 0
	
	ret = max(order.iteritems(), key=operator.itemgetter(1))
	if ret[1] == 0:
		return original
	else:
		return ret[0]

for doc in db.query(map_fun):
	tweet = db[doc['id']]
	keys = tweet.keys()
	if 'text' in keys:
		text = tweet['text']
	elif 'retweeted_status' in keys:
		text = tweet['retweeted_status']['text']
	else:
		continue
		
	#print(text)
	words = re.findall('[a-z]+', text.lower())
		
	for word in words:
		if  d.check(word):
			continue
		else:
			suggest = d.suggest(word)
			if len(suggest) == 0:
				continue
			replace = getCommon(word, suggest)
			if d.check(replace):
				text = text.replace(word, replace)
			
	tweet['corrected'] = text
	db[doc['id']] = tweet
			
			
