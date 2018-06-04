import web
from sys import path
path.append(r'Tools')
path.append(r'Config')
import SQLTools,LittleTools

class Publish:
    def POST(self):
        pub_info=web.input(d={})
        token=pub_info['token'].encode("utf-8")
        type=pub_info['type']
        content=pub_info['content']
        user_id=LittleTools.certify_token(token)
        if user_id==False:
            return LittleTools.MakeJson(401,"")
        try:
            activity_id=LittleTools.GenerateActivityId(user_id)
            SQLTools.InsertSql("insert into activity values (%s,%s,'%s',%s,0,null);"%(activity_id,user_id,content,type))
            return LittleTools.MakeJson(200,"")
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")





