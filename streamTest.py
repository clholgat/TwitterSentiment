import pycurl, json

def on_recieve(data):
	print(data)

conn = pycurl.Curl()
conn.setopt(pycurl.USERPWD, "clholgat:Jumbothedog12")
conn.setopt(pycurl.URL, "https://stream.twitter.com/1/statuses/sample.json")
conn.setopt(pycurl.WRITEFUNCTION, on_recieve)
conn.perform()
