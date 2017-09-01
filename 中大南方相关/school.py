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
	print("success!!!")
    print("是否要记住或改变密码？方便下次链接\n是的话输入yes:")
    passwd = raw_input("code:")
    if passwd=="yes":
      if flag==1:
	user = raw_input("您的账号:")
   	passwd = raw_input("您的密码:")
      f=open("login.txt","w")
      f.write(str(id)+"|"+passwd)
      f.close()
      print("success")
def run(ip):
   info=open("login.txt").read().split("|")
   user=info[0]
   passwd=info[1]
   login(user,passwd,ip,1)
   

if __name__ == '__main__':
   localIP = socket.gethostbyname(socket.gethostname())
   print("欢迎使用校园网连接器")
   if os.path.exists('login.txt'):
        print("1")
	run(localIP)
   f=open('login.txt','a')
   f.close()
   print("您的宿舍ip是:"+localIP)
   print("请输入你的联网账号和密码")
   user = raw_input("您的账号:")
   passwd = raw_input("您的密码:")
   login(user,passwd,localIP,0)
   







