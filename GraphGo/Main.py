#!/usr/bin/python
#coding=utf-8
import Config.Config
import Tools.SQLTools, Tools.LittleTools
from LoginRegist.Login import *
from LoginRegist.Regist import *
from MainPage.TakeActivity import *
from Tools.Image import *
from User.UserInfo import *
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
