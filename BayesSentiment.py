from calculation import *
from string import find

POS_EMOTICONS = [
    '<3', '8)', '8-)', '8-}', '8]', '8-]', ': )', ';]', ':-}', ':}', '=}', ':)', ';)', 'x)', ':D', ':-)', '^_^', '=)', '=]', ':-]', ':]'
]

NEG_EMOTICONS = [
	':-L', ':L',  '8(', '8-(', '8-[', '8-{', 'xx', '</3', ':-{', ': (', ':{', '={', 'x(', 'D:', '=[', '=(', ':(', ':-(', ':, (', ':\'(',  ':[', ':-['
]

class BayesSentiment(object):
	def train(self):
		self.stream = tweetFilter('clholgat', 'Jumbothedog12')
		pos_train = open("posTrain.txt", "a")
		neg_train = open("negTrain.txt", "a")
		for tweet in self.stream:
			text = tweet['text']
			norm, stems = normTweet(tweet)
			features = self.extractFeatures(stems)
			for emot in POS_EMOTICONS:
				if find(text, emot) != -1:
					pos_train.write(" ".join(stems)+"\n")
					print("pos "+emot+" ".join(stems))
					break
			for emot in NEG_EMOTICONS:
				if find(text, emot) != -1:
					neg_train.write(" ".join(stems)+"\n")
					print("neg "+emot+" ".join(stems))
					break
		return			
					
	def extractFeatures(self, stems):
		features = {}
		for stem in stems:
			features["contains(%s)" % stem] = True
		return features
		

if __name__ == "__main__":
	BayesSentiment().train()
			
