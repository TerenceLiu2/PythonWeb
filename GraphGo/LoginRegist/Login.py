import web
# from sys import path
# path.append(r'Tools')

# import SQLTools,LittleTools

render = web.template.render("Html")
renderImg = web.template.render("Img")

class LoginProfile:
    def POST(self):
        username = web.input()
        user_id = SQLTools.GetOneFromSql("select user_id from user where username='%s'" % username)
        if user_id != None:
            return LittleTools.MakeJson(200, {"img_url": "http://%s/Img/%d/profile" % (GraphGo.Config.ip, user_id)})
        else:
            return LittleTools.MakeJson(400, {"img_url": "http://%s/Img/default/profile" % GraphGo.Config.ip})



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

