import web

from GraphGo.Tools import LittleTools,SQLTools


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
            print sql
            SQLTools.InsertSql(sql)
            return LittleTools.MakeJson(200,"")
        else:
            return LittleTools.MakeJson(400,"")

