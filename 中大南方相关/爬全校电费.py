#coding:utf-8
import urllib
import urllib2
from urllib2 import urlopen
import requests



head={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'249',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'JSESSIONID=F5BC1101EEA77BAFC2F30D5BD47B862E',
'Host':'dfcx.nfu.edu.cn',
'Origin':'http://dfcx.nfu.edu.cn',
'Referer':'http://dfcx.nfu.edu.cn/webSelect/selectLogin.jsp',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}



def getcookie(roomid):
    url = 'http://dfcx.nfu.edu.cn/webSelect/roomFillLogView.do?method=webSelectLogin'
    data = {
        'buildingId':'5',
	'roomName':roomid,
	'adminRand':'3447',
	'x':'149',
	'y':'24'
}
    data['roomName']=roomid
    session = requests.Session()
    response = session.post(url, data=data, headers=head)

def login(roomid,num):
    getcookie(roomid)
    url = 'http://dfcx.nfu.edu.cn/webSelect/usedQuantityDelEleView.do?method=findUsedQuantityDelEleView'
    data = {
        'ec_i':'ec',
	'ec_eti':'ec',
	'ec_ev':'csv',
	'ec_efn':'UsedEle.txt',
	'ec_crd':'10',
	'ec_p':'1',
	'ec_s_roomName':'',
	'ec_s_usedEle':'',
	'ec_s_dailyUsed':'',
	'ec_s_leftEle':'',
	'ec_s_dateTime':'',
	'ec_a_当日实用电量(度)':'dailyUsed',
	'method':'findUsedQuantityDelEleView',
	'ec_rd':'10',
}
    session = requests.Session()
    response = session.post(url, data=data, headers=head)
    f=open('h5.txt', 'a')
    f.write(str(response.text))

for i in range(1,6):
   for j in range(1,29):
     print(i*100+j)
     login(i*100+j,i*100+j)
     


