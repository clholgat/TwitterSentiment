
import tweetstream, couchdb

def getDB(DB):
	couch = couchdb.Server()
	db = couch[DB]
	return db
	
def tweetFilter(uname, psswd):
	stream = tweetstream.SampleStream(uname, psswd)
	for tweet in stream:
		if 'user' in tweet.keys() and tweet['user']['lang'] == 'en':
			yield tweet

def parseTweet(tweet):
	if 'user' in tweet.keys() and tweet['user']['lang'] == 'en':
		return tweet
		
if __name__ == "__main__":

	stream = tweetFilter("clholgat", "Jumbothedog12")
	db = getDB('twitter_train')
	for tweet in stream:
		db.save(tweet)


