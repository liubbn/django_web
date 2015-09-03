#coding=utf-8
'''
Created on 2015年8月26日

@author: LIUBO

功能 ：Kindeditor文件上传。

//成功时
{
        "error" : 0,
        "url" : "http://www.example.com/path/to/file.ext"
}
//失败时
{
        "error" : 1,
        "message" : "错误信息"
}
'''
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from django.conf import settings
import os
import uuid
from datetime import datetime as dt

@csrf_exempt
def upload_img(request,dir_name):
    result = {"error":1,"message":"上传文件错误"}
    files = request.FILES.get('imgFile',None)
    
    if files :
        result = save_img(files,dir_name)     # 上传处理
    
    return HttpResponse(json.dumps(result),content_type = "application/json")

#生成上传绝对路径,返回文件相对路径
def creat_uploaddir(dir_name):
    today = dt.today()
    dir_name = dir_name + '/%d/%d/' % (today.year,today.month)
    dir_path = os.path.join(settings.MEDIA_ROOT,dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_name

#上传处理
def save_img(files,dir_name):
    #允许文件上传类型
    allow_type = ['jpg','png','jpeg','gif','bmp']
    
    file_type =files.name.split('.')[-1]
    
    if file_type not in allow_type :
        return {"error":1,"message":"上传文件类型错误"}
    
    dir_name = creat_uploaddir(dir_name)
    file_name = str(uuid.uuid1())+'.'+file_type
    
    file_path = os.path.join(settings.MEDIA_ROOT,dir_name,file_name)
    
    file_url = settings.MEDIA_URL+dir_name+file_name
    
    with open(file_path,'wb') as f:
        f.write(files.file.read())
    
    return {
        "error" : 0,
        "url" : file_url
    }
    
    
    
    
    
    
    