import tweetstream, enchant, re, math
from pickle import Unpickler
from nltk.stem.wordnet import WordNetLemmatizer
import string

anew = Unpickler(file('anew.pickle','r')).load()
d = enchant.Dict("en_US")
lmtzr = WordNetLemmatizer()

def tweetFilter(uname, psswd):
	stream = tweetstream.SampleStream(uname, psswd)
		
	for tweet in stream:
		if 'user' in tweet.keys() and tweet['user']['lang'] == 'en':
			yield tweet
			
def correctWord(word):
	sug = d.suggest(word)
	if len(sug) <= 0:
		return word
	else:
		return d.suggest(word)[0]
	
def calcSentiment(agg):		
	valence = 0
	valenceNorm = []
	valenceSum = 0
	valenceSD = 0
	arousal = 0
	arousalNorm = []
	arousalSum = 0
	arousalSD = 0
	wordFreq = 0
	for word in agg:
		wordFreq += word['word-freq']
		v = (1/math.sqrt(2*math.pi*math.pow(word['valence-SD'],2)))
		valenceSum += v
		valenceNorm.append((v,word['valence-mean']))
		valenceSD += word['valence-SD']
		a = (1/math.sqrt(2*math.pi*math.pow(word['arousal-SD'],2)))
		arousalSum += a
		arousalNorm.append((a,word['arousal-mean']))
		arousalSD += word['arousal-SD']
	
	for v in valenceNorm:
		valence += (v[0]/valenceSum)*v[1]
	
	for a in arousalNorm:
		arousal += (a[0]/arousalSum)*a[1]
		
	return {'valence':valence, 'valence-SD':valenceSD, 'arousal':arousal, 'arousal-SD':arousalSD, 'word-freq':wordFreq}
			
def normTweet(tweet):
	if 'text' in tweet.keys():
		text = tweet['text']
	else:
		return None
		
	exclude = set(string.punctuation)
	exclude.difference_update(set(['\'', '\"']))
	stripped = ''.join(ch for ch in text if ch not in exclude)	
	
	words = re.findall('[a-z\'\"]+', stripped.lower())
	#words = stripped.lower().split(" ")
	english = 0;
	agg = []
	
	for word in words:	
		if len(word) <= 2:
			continue
			
		if d.check(word):
			english += 1;
			replace = word
		else:
			replace = correctWord(word)
			if d.check(replace):
				text = text.replace(word, replace)
			else:
				continue
	
		stem = lmtzr.lemmatize(replace)
		agg.append(stem)
		
	tweet['text'] = text
	if english >= 2:
		return (tweet, agg)
	else:
		return (None, agg)
				

def getAnewSentiment(tweet):

	tweet, stems = normTweet(tweet)
	
	agg = []
	
	if tweet:
		for stem in stems:
			if stem in anew.keys():
				agg.append(anew[stem])
		if len(agg) >= 2:
			sentiment = calcSentiment(agg)
			return (sentiment, tweet['text'], tweet)
		else:
			return None
	else:
		return None
	
if __name__ == "__main__":
	stream = tweetFilter('SentimentTest', 'passwd')
	for tweet in stream:
		#print(tweet['text'])
		fixed = getAnewSentiment(tweet)
		if fixed:
			print(fixed[0])
