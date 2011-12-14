from calculation import *
from string import find
import random
import nltk

POS_EMOTICONS = [
    '<3', '8)', '8-)', '8-}', '8]', '8-]', ': )', ';]', ':-}', ':}', '=}', ':)', ';)', 'x)', ':D', ':-)', '^_^', '=)', '=]', ':-]', ':]'
]

NEG_EMOTICONS = [
	':-L', ':L',  '8(', '8-(', '8-[', '8-{', '</3', ':-{', ': (', ':{', '={', 'x(', 'D:', '=[', '=(', ':(', ':-(', ':, (', ':\'(',  ':[', ':-['
]

class BayesSentiment(object):
	def __init__(self):
		self.stream = tweetFilter('SentimentTest', 'passwd')
		self.pos_train = open("posTrain.txt", "a")
		self.neg_train = open("negTrain.txt", "a")
		self.pos_raw_train = open("posRawTrain.txt", "a")
		self.neg_raw_train = open("negRawTrain.txt", "a")
		
	def train(self):
		for tweet in self.stream:
			text = tweet['text']
			norm, stems = normTweet(tweet)
			features = self.extractFeatures(stems)
			for emot in POS_EMOTICONS:
				if find(text, emot) != -1:
					self.pos_train.write(" ".join(stems)+"\n")
					print("pos "+emot+" ".join(stems))
					break
			for emot in NEG_EMOTICONS:
				if find(text, emot) != -1:
					self.neg_train.write(" ".join(stems)+"\n")
					print("neg "+emot+" ".join(stems))
					break		
					
	def extractFeatures(self, stems):
		features = {}
		for stem in stems:
			features["contains(%s)" % stem] = True
		return features
		
	def trainRaw(self):
		for tweet in self.stream:
			text = self.removeNonAscii(tweet['text'])
			for emot in POS_EMOTICONS:
				if find(text, emot) != -1:
					text = text.replace(emot, "")
					self.pos_raw_train.write(text+"\n")
					print("pos "+emot+" "+text)
					break
			for emot in NEG_EMOTICONS:
				if find(text, emot) != -1:
					text = text.replace(emot, "")
					self.neg_raw_train.write(text+"\n")
					print("neg "+emot+" "+text)
					break
					
	def removeNonAscii(self, s): 
		return "".join(i for i in s if ord(i)<128)
	
	def getClassifier(self):
		self.pos_train.close()
		self.neg_train.close()
		self.pos_train = open("posTrain.txt", "r")
		self.neg_train = open("negTrain.txt", "r")
		self.featureset = []
		for line in self.pos_train:
			self.featureset.append((self.extractFeatures(line.split(" ")), "positive"))
		for line in self.neg_train:
			self.featureset.append((self.extractFeatures(line.split(" ")), "negative"))
		self.classifier = nltk.NaiveBayesClassifier.train(self.featureset)
		return self.classifier
	
	def getRawClassifier(self):
		self.pos_raw_train.close()
		self.neg_raw_train.close()
		self.pos_raw_train = open("posRawTrain.txt", "r")
		self.neg_raw_train = open("negRawTrain.txt", "r")
		self.featureset = []
		for line in self.pos_raw_train:
			self.featureset.append((self.extractFeatures(line.split(" ")), "positive"))
		for line in self.neg_raw_train:
			self.featureset.append((self.extractFeatures(line.split(" ")), "negative"))
		self.classifier = nltk.NaiveBayesClassifier.train(self.featureset)
		return self.classifier
	
	def rawClassify(self, tweet):
		text = tweet['text']
		classify = self.getRawClassifier().classify(self.extractFeatures(self.removeNonAscii(text).split(" ")))
		return (classify, tweet['text'], tweet)
	
	def testClassifier(self):
		random.shuffle(self.featureset)
		trainSet, testSet = self.featureset[len(self.featureset)/2:], self.featureset[:len(self.featureset)/2]
		test = nltk.NaiveBayesClassifier.train(trainSet)
		print(nltk.classify.accuracy(test, testSet))
		

if __name__ == "__main__":
	BayesSentiment().train()
			
