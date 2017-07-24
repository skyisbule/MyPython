#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from datetime import datetime,timedelta


global list=['127.0.0.1']

def add(req):
    if req.method == 'POST':
        if req.META=="":
	    return HttpResponse("不要搞事情")
	ip=req.META['REMOTE_ADDR']
	list.append(ip) 
	name=req.POST['name']+'|'
	sex=req.POST['sex']+'|'
	tel=req.POST['tel']+'|'
	qq=req.POST['qq']+'|'
	bumen1=req.POST['bumen1']+'|'
	select2=req.POST['select2']+'|'
	induce=req.POST['induce']+'|<br>\n'
	if name=="|":
	    return HttpResponse("不要搞事情")
	if sex=='人妖|':
	    return HttpResponse("计协不需要人妖")
	if tel=="|":
	    return HttpResponse("不要搞事情")

	if induce.encode("utf-8") in strs:
	   return HttpResponse("提交失败请联系管理员 ErrorCode:101")
	if ip in list:
	   return HttpResponse("提交失败请联系管理员 ErrorCode:102")
	if name.encode("utf-8") in strs:
	   f=open("doc/sb.txt",'a')
	   res=name+sex+tel+qq+bumen1+select2+induce
	   f.write(res.encode("utf-8"))
	   f.close()
	   return HttpResponse("你已经报过了")
	f=open("doc/res.txt",'a')
	res=name+sex+tel+qq+bumen1+select2+induce
	f.write(res.encode("utf-8"))
	f.close()
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
   return HttpResponse("how you know here ?")

def geren(req):
   path='doc/res.txt'
   res=open(path).read()
   return HttpResponse('<style>p{color:gray}</style>'+res)


