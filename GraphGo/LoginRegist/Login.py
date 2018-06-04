import web
from sys import path
path.append(r'Tools')
import SQLTools,LittleTools

render = web.template.render("Html")
renderImg = web.template.render("Img")


class Login:
    def POST(self):
        info_dict=web.input(i={})
        username=info_dict['username']
        password=info_dict['password']
        sql="select user_id,password from user where username='%s';"%username
        sql_list= SQLTools.GetListFromSql(sql)
        if sql_list==None:
            return LittleTools.MakeJson(404,"")
        sql_passwd = sql_list[1]
        user_id = sql_list[0]
        token = LittleTools.generate_token(user_id)
        t_dict = {'token': token,'user_id':user_id}
        if sql_passwd!=password:
            return LittleTools.MakeJson(400,"")
        else:
            return LittleTools.MakeJson(200,t_dict)

