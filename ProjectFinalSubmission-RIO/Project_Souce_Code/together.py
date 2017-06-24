import numpy
from url import Comments
from tokens import Token
from pos import POS
from lemmatize import Lemmatize
from lesk import Lesk
from synonymy import Synonymy

print "result of all features together:"
comments=Comments()
testlist=comments.testList
tok=Token()
part=POS()
lem=Lemmatize()
l=Lesk()
syn=Synonymy()
num=0
for comment in testlist:
	p=[]
	tokp=tok.probability(comment)
	partp=part.probability(comment)
	lemp=lem.probability(comment)
	lp=l.probability(comment)
	synp=syn.probability(comment)

	p.append(numpy.float128(tokp[0])*partp[0]*lemp[0]*lp[0]*synp[0])
	p.append(numpy.float128(tokp[1])*partp[1]*lemp[1]*lp[1]*synp[1])
	p.append(numpy.float128(tokp[2])*partp[2]*lemp[2]*lp[2]*synp[2])
	p.append(numpy.float128(tokp[3])*partp[3]*lemp[3]*lp[3]*synp[3])
	p.append(numpy.float128(tokp[4])*partp[4]*lemp[4]*lp[4]*synp[4])
	Max=max(p)
	star=p.index(Max)+1
	if int(comment[0])==star:
		num=num+1
	print "original:",star,"\timplement:",comment[0],"\tmax probability:",Max
print "Accuracy:",float(num)/20
print "naive accuracy:",0.45
