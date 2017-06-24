from url import Comments
import re
comments=Comments()
testlist=comments.testList
pattern=re.compile(r'[.,"\?!:-]')
set1=['rediculous','terrible','horrible']
set2=['disappoint','small']
set3=['popular','hot','thankfully']
set4=['good','love','enjoy']
set5=['awsome','gorgeous','delicious']
print "naiave result:"
def getStar(comment):
	words=comment.split(' ')
	for word in words:
		word=re.sub(pattern,'',word)
		if word in set1:
			return 1
			break
		elif word in set2:
			return 2
			break
		elif word in set3:
			return 3
			break
		elif word in set4:
			return 4
			break
		elif word in set5:
			return 5
			break
	return 3
num=0
for comment in testlist:
	star=getStar(comment[1])
	if int(comment[0])==star:
		num=num+1
	print "original:",comment[0],"\tnaive:",star
print "naive accuracy:",float(num)/20
