#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from datetime import datetime,timedelta

global list
list=['start:']

def add(req):
    if req.method == 'POST':
        if req.META=="":
	    return HttpResponse("不要搞事情")
	ip=req.META['REMOTE_ADDR'] 
	if ip in list:
	   return HttpResponse("提交失败请联系管理员 ErrorCode:102")
	name=req.POST['name']+'|'
	sex=req.POST['sex']+'|'
	tel=req.POST['tel']+'|'
	qq=req.POST['qq']+'|'
	bumen1=req.POST['bumen1']+'|'
	select2=req.POST['select2']+'|'
	induce=req.POST['induce']+'|'
	if name=="|":
	    return HttpResponse("不要搞事情")
	if sex=='人妖|':
	    return HttpResponse("计协不需要人妖")
	if tel=="|":
	    return HttpResponse("不要搞事情")

	strs=open('doc/res.txt').read()
	if induce.encode("utf-8") in strs:
	   return HttpResponse("提交失败请联系管理员 ErrorCode:101")
	if name.encode("utf-8") in strs:
	   f=open("doc/sb.txt",'a')
	   res=name+sex+tel+qq+bumen1+select2+induce
	   f.write(res.encode("utf-8"))
	   f.close()
	   return HttpResponse("你已经报过了,不过没关系，我们仍收到了你的信息")
	f=open("doc/res.txt",'a')
	res=name+sex+tel+qq+bumen1+select2+induce+ip+'<br>\n'
	f.write(res.encode("utf-8"))
	f.close()
	global list
	list.append(ip)
	return HttpResponse("报名成功喽")
    else:
        return render_to_response('index.html',{'uf':'a'},context_instance=RequestContext(req))


def show(req):
   passwd=req.GET['a']
   if passwd=="skyisbule":
    path='doc/res.txt'
    res=open(path).read()
    return HttpResponse(res)
   if passwd=="sb":
    path='doc/sb.txt'
    res=open(path).read()
    return HttpResponse(res)
   if passwd=="clear":
    global list
    list2=list
    list=['start:']
    return HttpResponse(list2)
   return HttpResponse("how you know here ?")

def geren(req):
   path='doc/res.txt'
   res=open(path).read()
   return HttpResponse('<style>p{color:gray}</style>'+res)


