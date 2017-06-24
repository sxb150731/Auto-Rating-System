from url import Comments
from tokens import Token
from pos import POS
from lemmatize import Lemmatize
from lesk import Lesk
from synonymy import Synonymy
from dependencyParse import DependencyParse

comments=Comments()
testlist=comments.testList
tok=Token()
part=POS()
lem=Lemmatize()
l=Lesk()
syn=Synonymy()
dep=DependencyParse()
method=dep

num=0
if method==tok:
	print "result of Token:"
elif method==part:
	print "result of POS:"
elif method==lem:
	print "result of Lemmatize:"
elif method==l:
	print "result of Lesk:"
elif method==syn:
	print "result of Synonymy:"
elif method==dep:
	print "result of Dependency Parse:"
"""
dict0={}
method.addDictionary(dict0,testlist[0][1])
print dict0"""
for comment in testlist:
	p=method.probability(comment)
	Max=max(p)
	star=p.index(Max)+1
	if int(comment[0])==star:
		num=num+1
	print "original:",comment[0],"\timplement:",star,"\tmax probability:",Max
print "Accuracy:",float(num)/20
print "naive accuracy:",0.45
