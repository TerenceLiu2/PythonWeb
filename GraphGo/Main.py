#!/usr/bin/python
#coding=utf-8
import Config.Config
import Tools.SQLTools,Tools.LittleTools
from Activity.Publish import *
from Activity.TakeActivity import *
from Tools.Image import *
from LoginRegist.Login import *
from User.UserInfo import *
from User.UserHistory import *
from Activity.FinishActivity import *
from LoginRegist.Regist import *
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
    #活动
    '/Publish','Publish',
    '/TakeActivity','TakeActivity',
    '/FinishActivity','FinishActivity',
    #主页
    '/MainWait','MainWait',
    '/MainFinish','MainFinish',

    #测试
    '/(.*?)', 'RegistInput'

)
app = web.application(urls, globals())




if __name__ == "__main__":
    SQLTools.InitSql('localhost', 'root', '123', 'GraphGo')
    app.run()
