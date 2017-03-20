from urllib2 import urlopen
import re
from bs4 import BeautifulSoup
import time
import sys   
sys.setrecursionlimit(10000)

f = open("/root/meizi.txt","r")  
lines = f.readlines()
for line in lines:
   html = urlopen(line)
   bsObj= BeautifulSoup(html)
   print("!")
   for link in bsObj.findAll('img',src=re.compile('http://i.meizitu.net/+[0-9]+[^\s]*')):
	print(link['src'])
	file =open("img.txt","a")
	file.write(link['src']+"\n")
	file.close()
	
