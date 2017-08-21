from urllib2 import urlopen
import re
from bs4 import BeautifulSoup
import time
import sys   
sys.setrecursionlimit(10000)

'''
a simple demo:
get all <a> from a website
2016.11.2
'''

pages = set()
def getLinks(pageurl):
	global pages
	html = urlopen(pageurl)
	bsObj= BeautifulSoup(html)
	for link in bsObj.findAll('a',href=re.compile('http://heartqiu.cn+[^\s]*')):
	 if 'href' in link.attrs:
	  if link.attrs['href'] not in pages:
	    newpage = link.attrs['href']
	    print(newpage)
	    pages.add(newpage)
	    if 'jpg' not in newpage:
	       getLinks(newpage)			
getLinks('http://heartqiu.cn')

