from urllib2 import urlopen
import re
from bs4 import BeautifulSoup
import time
import sys   
sys.setrecursionlimit(10000)
global i
i = 0
pages = set()
def run():
   global pages
   f = open("/root/meizi.txt","r")  
   lines = f.readlines()
   for line in lines:
        k=line.strip('\n')
	pages.add(k)
   print("success")
   f.close()
def getLinks(pageurl):
	global pages
	html = urlopen(pageurl)
	bsObj= BeautifulSoup(html)
	print("!")
	for link in bsObj.findAll('a',href=re.compile('http://www.mzitu.com/+[0-9]+[^\s]*')):
	   if 'href' in link.attrs:
		if link.attrs['href'] not in pages:
		   newpage = link.attrs['href']
		   print(newpage)
	           file.write(newpage+"\n")
		   pages.add(newpage)
	    	   global i
		   i=i+1
		   print(str(i))
		   getLinks(newpage)

run()
file =open("meizi.txt","a")

getLinks('http://www.mzitu.com/tag/baoru')
file.close()
