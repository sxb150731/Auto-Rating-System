from url import Comments
import re
from nltk.parse.stanford import StanfordDependencyParser
class DependencyParse:
	comments=Comments()
	trainlist=comments.trainList
	testlist=comments.testList
	dict1={}
	dict2={}
	dict3={}
	dict4={}
	dict5={}
	path_to_jar = 'stanford-parser-full-2015-12-09/stanford-parser.jar'
	path_to_models_jar = 'stanford-parser-full-2015-12-09/stanford-parser-3.6.0-models.jar'
	dependency_parser = StanfordDependencyParser(path_to_jar=path_to_jar, path_to_models_jar=path_to_models_jar)

	def addDictionary(self,dict0,comment):
		pattern1 = u"!.?,"
		sentences = re.compile(u'[^%s]+' % pattern1).findall(comment)
		for sentence in sentences:
			result = self.dependency_parser.raw_parse(sentence)
			dep = result.next()
			lists=list(dep.triples())
			for newlist in lists:
				string=newlist[0][0].encode('utf-8')+" "+newlist[1].encode('utf-8')+" "+newlist[2][0].encode('utf-8')			
				if dict0.has_key(string):
					dict0[string]=dict0[string]+1
				else:
					dict0[string]=1

	def test(self,dict0,comment):
		p=1
		pattern1 = u"!.?,"
		sentences = re.compile(u'[^%s]+' % pattern1).findall(comment)
		for sentence in sentences:
			result = self.dependency_parser.raw_parse(sentence)
			dep = result.next()
			lists=list(dep.triples())
			for newlist in lists:
				string=newlist[0][0].encode('utf-8')+" "+newlist[1].encode('utf-8')+" "+newlist[2][0].encode('utf-8')
				if dict0.has_key(string):
					n=float(dict0[string])
					s=self.dict1.get(string,0)+self.dict2.get(string,0)+self.dict3.get(string,0)+self.dict4.get(string,0)+self.dict5.get(string,0)			
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





