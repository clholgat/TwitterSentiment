import pycurl, json, urllib

class bufferedStream:
	def __init__(self):
		self.buffer = ""
		self.conn = pycurl.Curl()
		self.conn.setopt(pycurl.USERPWD, "clholgat:Jumbothedog12")
		self.conn.setopt(pycurl.URL, "https://stream.twitter.com/1/statuses/filter.json")
		self.conn.setopt(pycurl.POST, 1)
		postOpts = {'track': 'lang:en'}
		self.conn.setopt(pycurl.POSTFIELDS, urllib.urlencode(postOpts))
		self.conn.setopt(pycurl.WRITEFUNCTION, self.on_recieve)
		self.conn.perform()
		
	def on_recieve(self, data):
		self.buffer += data
		if data.endswith("\r\n") and self.buffer.strip():
			print(json.loads(self.buffer))
			self.buffer = ""
			
if __name__ == "__main__":
	stream = bufferedStream()
