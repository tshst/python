#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

def getPersonName(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        nameList = bsObj.findAll("span", {"class":"green"})
        for name in nameList:
            return name.get_text()

    except AttributeError as e:
        return None

def getChild(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        for child in bsObj.find("table",{"id":"giftList"}).children:
            return child
    except AttributeError as e:
        return None

def getBrother(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        for brother in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
            print(brother)
    except AttributeError as e:
        return None

def getLinks(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html)
        for link in bsObj.findAll("a"):
            if 'href' in link.attrs:
                print(link.attrs['href'])
    except AttributeError as e:
        return None



#res = getTitle("http://www.pythonscraping.com/pages/page1.html")
#res = getPersonName("http://www.pythonscraping.com/pages/warandpeace.html")
#res = getChild("http://www.pythonscraping.com/pages/page3.html")
res = getBrother("http://www.pythonscraping.com/pages/page3.html")
#res = getLinks("http://en.wikipedia.org/wiki/Kevin_Bacon")

if res == None:
    print("name could not be found")
else:
    print(res)




#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html)
for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])

#%%
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)


#%%
## PythonによるWebスクレイピングの3.1まで完了
## webスクレイピングを学ぶ前にHTMLとCSSの知識をもっと学んだほうが良いと感じた