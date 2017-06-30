#coding:utf-8
import urllib
import urllib2
from urllib2 import urlopen
import requests
import re
import time

head={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'249',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'',
'Host':'live.bilibili.com',
'Origin':'http://dfcx.nfu.edu.cn',
'Referer':'http://static.hdslb.com/live-static/swf/LivePlayerEx_1.swf?_=1-1-6d8379b',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}



def send(msg):
    url = 'http://live.bilibili.com/msg/send'
    data = {
        'color':'16777215',
	'fontsize':'25',
	'mode':'1',
	'msg':'ghh',
	'rnd':'1498574330',
	'roomid':'68886',
}
    data['msg']=msg
    session = requests.Session()
    response = session.post(url, data=data, headers=head)
    print(response)

send("hahahha")









