#coding:utf-8
from urllib2 import urlopen
import re
import requests
from bs4 import BeautifulSoup
import time
import random

import itchat
from itchat.content import *
itchat.auto_login(hotReload=True)

head={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'_xsrf=2|f85863c5|9568e3384c4d57f80ebce3d4cafcbb51|1492832899; _qqq_uuid_="2|1:0|10:1492832899|10:_qqq_uuid_|56:ZWFhNjJjNDRkOWNlYzY3OWMyNGE0OTdkMDExYzVhNzM1N2Y2YTAyZA==|4eccf0879afb9fabc28993e5468e644e708b060013259d7c23dc9460a9258bc0"; Hm_lvt_2670efbdd59c7e3ed3749b458cafaa37=1492832904; Hm_lpvt_2670efbdd59c7e3ed3749b458cafaa37=1492833976; _ga=GA1.2.1059794749.1492832904; _gat=1',
'Host':'www.qiushibaike.com',
'Referer':'http://www.qiushibaike.com/hot/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2604.400 QQBrowser/9.6.10897.400'
}

def get():
   session=requests.Session()
   url='http://www.qiushibaike.com/text/'
   req=session.get(url,headers=head)
   bsObj= BeautifulSoup(req.text)
   flag=int(random.randint(1,25))
   now=0
   pattern=re.compile('<span>(.*)</span>')
   res=re.findall(pattern,str(bsObj))
   for i in res:
      now=now+1
      if '匿名' in i:
        continue
      if flag<now:
        i=i.replace('<br>','.')
        i=i.replace('<br/>','.')
        return i.decode('utf-8')
        break

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print(msg.text)
    if msg.text==u'笑话':
      msg.user.send('%s: %s' % (msg.type,get()))
    if msg.text==u'帮助':
      msg.user.send(u'我只是一个机器人')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg.text)
   # if msg.isAt:
    if msg.text==u'笑话':
          msg.user.send('%s: %s' % (msg.type,get()))



itchat.auto_login(True)
itchat.run()


