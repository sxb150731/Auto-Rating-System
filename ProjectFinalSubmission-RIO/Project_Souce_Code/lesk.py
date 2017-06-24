from url import Comments
from nltk.corpus import wordnet
import re
class Lesk:
	comments=Comments()
	trainlist=comments.trainList
	testlist=comments.testList
	dict1={}
	dict2={}
	dict3={}
	dict4={}
	dict5={}
	pattern=re.compile(r'[.,"\?!:-]')

	def computeOverlap(self,signature,context):
		a=0
		s1=signature.split()
		s2=context
		for w1 in s1:
			for w2 in s2:
				if w1==w2:
					a=a+1
		return a

	def simplifiedLesk(self,word, sentence):
		maxOverlap=0
		bestSense=""
		context=sentence.split()
		synsets = wordnet.synsets(word)
		for sense in synsets:
			signature=[]
			overlap=0
			glow=sense.definition()
			overlap=self.computeOverlap(glow,context)
			for example in sense.examples():
					overlap+=self.computeOverlap(example,context)
			if overlap>maxOverlap:
				maxOverlap=overlap
				bestSense=sense
		return bestSense

	def addDictionary(self,dict0,comment):
		pattern1 = u"!.?,"
		sentences = re.compile(u'[^%s]+' % pattern1).findall(comment)
		for sentence in sentences:
			words=sentence.split(' ')
			for word in words:
				word=re.sub(self.pattern,'',word)
				word=self.simplifiedLesk(word,sentence)
				if dict0.has_key(word):
					dict0[word]=dict0[word]+1
				else:
					dict0[word]=1

	def test(self,dict0,comment):
		p=1
		pattern1 = u"!.?,"
		sentences = re.compile(u'[^%s]+' % pattern1).findall(comment)
		for sentence in sentences:
			words=sentence.split(' ')
			for word in words:
				word=re.sub(self.pattern,'',word)
				word=self.simplifiedLesk(word,sentence)
				if dict0.has_key(word):
					n=float(dict0[word])
					s=self.dict1.get(word,0)+self.dict2.get(word,0)+self.dict3.get(word,0)+self.dict4.get(word,0)+self.dict5.get(word,0)			
					if s!=0:
						p=p*(n/s)
		if p==1:
			p=0
		return p
	def training(self,dict1,dict2,dict3,dict4,dict5):
		for comment in self.trainlist:
			if comment[0]=='1':
				self.addDictionary(self.dict1,comment[1])
			elif comment[0]=='2':
				self.addDictionary(self.dict2,comment[1])
			elif comment[0]=='3':
				self.addDictionary(self.dict3,comment[1])
			elif comment[0]=='4':
				self.addDictionary(self.dict4,comment[1])
			elif comment[0]=='5':
				self.addDictionary(self.dict5,comment[1])

	def probability(self,comment):
		self.training(self.dict1,self.dict2,self.dict3,self.dict4,self.dict5)
		p=[]
		p.append(self.test(self.dict1,comment[1]))
		p.append(self.test(self.dict2,comment[1]))
		p.append(self.test(self.dict3,comment[1]))
		p.append(self.test(self.dict4,comment[1]))
		p.append(self.test(self.dict5,comment[1]))
		return p





