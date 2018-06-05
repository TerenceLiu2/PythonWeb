#!/usr/bin/python
#coding=utf-8
from MainPage.MainActivity import *

urls = (
    #登录注册
    '/Login','Login',
    '/Regist','Regist',
    #用户
    '/UserInfoUpload','UserInfoUpload',
    '/Img/(.*?)','SingleImg',
    '/UserBasicInfo','UserBasicInfo',
    '/UserActivity','UserActivity',
    '/UserPhoto','UserPhoto',
    #发布
    '/Publish','Publish',
    #主页
    '/MainWait','MainWait',
    '/MainFinish','MainFinish',
    '/TakeActivity','TakeActivity',
    #测试
    '/(.*?)', 'RegistInput'

)
app = web.application(urls, globals())




if __name__ == "__main__":
    SQLTools.InitSql('localhost', 'root', '123', 'GraphGo')
    app.run()
