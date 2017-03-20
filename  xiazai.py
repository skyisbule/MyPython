from urllib2 import urlopen
import re
from bs4 import BeautifulSoup

html = urlopen('http://www.henan.gov.cn/jrhn/system/2017/02/05/010705869.shtml')
bsObj= BeautifulSoup(html)
print("!")
for link in bsObj.findAll('title'):
	#print(link['src'])
	print(link)
	#print(link)
	#file =open("img.txt","a")
	#file.write(link['src']+"\n")
	#file.close()
	
