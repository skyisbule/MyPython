from urllib2 import urlopen
import re
from bs4 import BeautifulSoup
import time
import sys   
sys.setrecursionlimit(10000)

pages = set()
global i
i=1
def run():
   global pages
   f = open("/root/dizhi.txt","r")  
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
	for link in bsObj.findAll('a',href=re.compile('http://aqicn.org/city/+[^\s]*')):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newpage = link.attrs['href']
				if 'jp/' not in newpage:
				 if '/es' not in newpage:
				  if '/ru' not in newpage:
				   if '/fr' not in newpage:
				    if '/de' not in newpage:
				     if '/hk' not in newpage:
				      if '/pl' not in newpage:
				       if '/cn' not in newpage:
				        if '/pt' not in newpage:
				         if '/vn' not in newpage:
					  if '/m' not in newpage:
				           if '/kr' not in newpage:
				    	    print(newpage)
					    global i
					    i=i+1
					    print(str(i))
					    file.write(newpage+"\n")
				    	    pages.add(newpage)
					    if i==100:
					      return
				     	    getLinks(newpage)

run()
file =open("dizhi.txt","a")

getLinks('http://aqicn.org/city/singapore/north/')
file.close()
