# -*- coding: UTF-8 -*-
import urllib  
import shutil
import os
global k
k=0
def xiazai(url,i):  
  data = urllib.urlopen(url).read()  
  f = file(str(i)+'.jpg',"wb")
  f.write(data)  
  f.close()
  shutil.copy('/root/'+str(i)+'.jpg','/root/桌面/pp')
  os.remove('/root/'+str(i)+'.jpg')
  print('success'+str(i))

f = open("/root/img.txt","r")  
lines = f.readlines()
for line in lines:
	global k
	k=k+1
	xiazai(line,k)


