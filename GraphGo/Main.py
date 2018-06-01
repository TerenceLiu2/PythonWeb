#coding=utf-8
import web
from Tools import SQLTools
from LoginRegist.Login import *
from LoginRegist.Regist import *
from User.UserInfo import *
from User.UserHistory import *
from Tools.Image import *
from Publish.Publish import *
from MainPage.MainActivity import *


urls = (
    #登录注册
    '/Login','Login',
    '/Regist','Regist',
    '/LoginProfile','LoginProfile',
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
    #测试
    '/(.*?)', 'RegistInput'

)
app = web.application(urls, globals())




if __name__ == "__main__":
    SQLTools.InitSql('localhost', 'root', '123', 'GraphGo')
    app.run()