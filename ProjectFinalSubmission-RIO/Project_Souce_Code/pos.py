from url import Comments
import nltk
import re

class POS:
	comments=Comments()
	trainlist=comments.trainList
	testlist=comments.testList
	dict1={}
	dict2={}
	dict3={}
	dict4={}
	dict5={}

	def addDictionary(self,dict0,comment):
		text = nltk.word_tokenize(comment)
		lists= nltk.pos_tag(text)
		for newlist in lists:
			if newlist[1]=='.':
				continue
			if dict0.has_key(newlist[0]):
				newdict=dict0[newlist[0]]
				if newdict.has_key(newlist[1]):
					newdict[newlist[1]]=newdict[newlist[1]]+1
				else:
					newdict[newlist[1]]=1
			else:
				dict0[newlist[0]]={newlist[1]:1}

	def tagsum(self,dict0,newlist):
		n=0
		if dict0.has_key(newlist[0]):
			newdict=dict0[newlist[0]]
			if newdict.has_key(newlist[1]):
				n=float(newdict[newlist[1]])
		return n

	def test(self,dict0,comment):
		p=1
		text = nltk.word_tokenize(comment)
		lists= nltk.pos_tag(text)
		for newlist in lists:
			if newlist[1]=='.':
				continue
			if dict0.has_key(newlist[0]):
				newdict=dict0[newlist[0]]
				if newdict.has_key(newlist[1]):
					n=float(newdict[newlist[1]])
					s=self.tagsum(self.dict1,newlist)+self.tagsum(self.dict2,newlist)+self.tagsum(self.dict3,newlist)+self.tagsum(self.dict4,newlist)+self.tagsum(self.dict5,newlist)	
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





