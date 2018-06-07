import web
from sys import path
import shutil
path.append(r'Tools')
path.append(r'Config')
import LittleTools,SQLTools


render = web.template.render("Html")

class RegistInput:
    def GET(self,name):
        return render.Regist()


class Regist:
    def POST(self):
        info_dict=web.input(i={})
        username=info_dict['username']
        password=info_dict['password']
        re_password=info_dict['re_password']
        if password==re_password:
            sql = "insert into user (username,password) value ('%s','%s')" % (username, password)
            SQLTools.InsertSql(sql)
            sql = "select user_id from user where username='%s';"%username
            user_id=SQLTools.GetOneFromSql(sql)
            LittleTools.Mkdir("Img/%s/"%user_id)
            shutil.copyfile("Img/default/profile","Img/%s/profile"%user_id)
            return LittleTools.MakeJson(200,"")
        else:
            return LittleTools.MakeJson(400,"")

