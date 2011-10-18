
import tweetstream, couchdb

def getDB():
	couch = couchdb.Server()
	db = couch['twitter_train']
	return db
	
def parseTweet(tweet, db):
	if 'user' in tweet.keys() and tweet['user']['lang'] == 'en':
		db.save(tweet)
		
if __name__ == "__main__":

	stream = tweetstream.SampleStream("clholgat", "Jumbothedog12")
	db = getDB()
	for tweet in stream:
		#print(tweet)
		parseTweet(tweet, db)


