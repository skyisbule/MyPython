#coding:utf-8
import requests
import socket
import os

head={'Accept':'image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*',
'Referer':'http://219.136.125.139/portalReceiveAction.do?wlanuserip=10.12.48.62&wlanacname=nfsysugz2',
'Accept-Language':'zh-cn',
'User-Agent':'Supplicant',
'Content-Type':'application/x-www-form-urlencoded',
'Accept-Encoding':'gzip, deflate',
'Host':'219.136.125.139',
'Content-Length':'124',
'Connection':'Keep-Alive',
'Cache-Control':'no-cache'}


path=r'C:\Users\Public\login.txt'

def login(id,passwd,ip,flag):
    url = 'http://219.136.125.139/portalAuthAction.do'
    data = {
        'userid': '',
        'passwd': '',
        'wlanuserip': '',
        'wlanacname': 'nfsysugz2',
	'auth_type': 'PAP',
        'wlanacIp': '183.6.109.10'
    }
    data['userid']=id
    data['passwd']=passwd
    data['wlanuserip']=ip
    session = requests.Session()
    response = session.post(url, data=data, headers=head)
    if len(response.text)>300:
	print(u"连接成功!!!")
    else:
        print(u"连接失败!!!请检查账号密码\n以下为错误信息")
        print(response.text)
        exit()
    print(u"是否要记住或改变密码？方便下次链接\n是的话输入yes:")
    passwd = raw_input("code:")
    if passwd=="yes":
      if flag==1:
	user = raw_input("usernum:")
   	passwd = raw_input("password:")
      f=open(path,"w")
      f.write(str(id)+"|"+passwd)
      f.close()
      print(u"连接成功")
def run(ip):
   info=open(path).read().split("|")
   user=info[0]
   passwd=info[1]
   login(user,passwd,ip,1)
   exit()

def getip():
    ipList =  socket.gethostbyname_ex(socket.gethostname())[-1]
    for i in ipList:
     if '10.' in i:
      print(u"您的IP是："+i)
      return i
    print(u'检测不到宿舍IP')

def init():
    if os.path.exists(path):
       if open(path).read()=="":
           os.remove(path)
    
   

if __name__ == '__main__':
    
   init()
   localIP = getip()
   print(u"是否手动输入ip:yes/no")
   key = raw_input("code:") 
   if key=='yes':
       localIP = raw_input("ip:")
   if os.path.exists(path):
     if '|' in open(path).read():
        print(u"检测到您有保存账号密码")
	run(localIP)
   f=open(path,'a')
   f.close()
   print("youur ip is:"+localIP)
   print(u"请输入你的联网账号和密码")
   user = raw_input("your num:")
   passwd = raw_input('your password:')
   login(user,passwd,localIP,0)
