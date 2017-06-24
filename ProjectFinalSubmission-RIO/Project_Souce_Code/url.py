import urllib
import urllib2
import re

class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD= re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')
    replaceApostrophe = re.compile(r'&#39;')
    replacenbsp = re.compile(u'\xc2')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"",x)
        x = re.sub(self.replaceTD,"",x)
        x = re.sub(self.replacePara,"",x)
        x = re.sub(self.replaceBR,"",x)
        x = re.sub(self.removeExtraTag,"",x)  
        x = re.sub(self.replaceApostrophe," '",x)
        x = re.sub(self.replacenbsp,"",x)    
        return x.strip()
class Yelp:
    def __init__(self,baseUrl):
        self.baseURL = baseUrl
        self.tool = Tool()
    def getPage(self,pageNum):
        try:
            num=20*(pageNum-1)
            url = self.baseURL+'?start='+str(num)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"",e.reason
                return None
class Comments:
    trainList=[]
    testList=[]
    url = 'https://www.yelp.com/biz/shake-shack-dallas'
    yielp=Yelp(url)
    tool=Tool()
    page=[1,2,3,4,5]
    for i in page:
        content=yielp.getPage(i)
        pattern0=re.compile('review-content.*?review-footer',re.S)
        pattern2=re.compile('<p lang="en">.*?</p>')
        pattern1=re.compile('title=.*?rating"')
        reviews=re.findall(pattern0,content)    
        for review in reviews:
            newlist=[]
            star=re.findall(pattern1,review)
            comment=re.findall(pattern2,review)
            star=tool.replace(star[0])
            star=star[7]
            star=star.encode("utf-8")
            comment=tool.replace(comment[0])
            comment=comment.lstrip('title').rstrip('star rating"').strip()
            comment=comment.encode("utf-8")
            uniString = unicode(comment, "UTF-8")
            comment = uniString.replace(u"\u00A0", " ")
            newlist.append(star)
            newlist.append(comment)
            if i==1:
                testList.append(newlist)
            else:
                trainList.append(newlist)