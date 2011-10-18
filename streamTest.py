import pycurl, json, urllib

import couchdb

USERPWD = "clholgat:Jumbothedog12"
SAMPLE = "https://stream.twitter.com/1/statuses/sample.json"


def getDB():
	couch = couchdb.Server()
	db = couch['twitter']
	return db

def parseTweet(tweet, db):
	tweet = json.loads(tweet)
	if 'user' in tweet.keys() and tweet['user']['lang'] == 'en':
		db.save(tweet)

class bufferedStreamTwitter:
	def __init__(self, db):
		self.buffer = ""
		self.db = db
		self.conn = pycurl.Curl()
		self.conn.setopt(pycurl.USERPWD, USERPWD)
		self.conn.setopt(pycurl.URL, SAMPLE)
		self.conn.setopt(pycurl.WRITEFUNCTION, self.on_recieve)
		self.conn.setopt(pycurl.CONNECTTIMEOUT, 15)
		self.conn.setopt(pycurl.TIMEOUT, 25)
		
		self.conn.perform()
		
	def on_recieve(self, data):
		print(data)
		self.buffer += data
		if data.endswith("\r\n") and self.buffer.strip():
			parseTweet(self.buffer, self.db)
			self.buffer = ""
			
if __name__ == "__main__":
	db = getDB()

	stream = bufferedStreamTwitter(db)
