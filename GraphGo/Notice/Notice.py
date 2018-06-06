import web
from sys import path
path.append(r'Tools')
path.append(r'Config')
import Config
import SQLTools, LittleTools

class UserNotice:
    def POST(self):
        token = web.input()
        user_id = LittleTools.certify_token(token['token'].encode("utf-8"))
        if user_id == False:
            return LittleTools.MakeJson(400, "")
        try:
            notice_list = SQLTools.GetNoticeFromSql(user_id)
        except Exception, e:
            print e
            return LittleTools.MakeJson(500, "")
            pass
        return LittleTools.MakeJson(200, {"notice_list": notice_list})