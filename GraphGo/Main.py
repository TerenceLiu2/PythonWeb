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
from Activity.ActivityInfo import *
from LoginRegist.Regist import *
from Notice.Notice import *
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
    '/ActivityInfo','ActivityInfo',
    #主页
    '/MainWait','MainWait',
    '/MainFinish','MainFinish',
    #消息
    '/UserNotice','UserNotice',
    #测试
    '/(.*?)', 'RegistInput'

)
app = web.application(urls, globals())




if __name__ == "__main__":
    app.run()
