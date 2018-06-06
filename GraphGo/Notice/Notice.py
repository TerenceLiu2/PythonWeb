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
            user_name = SQLTools.GetNoticeFromSql(user_id)
        except Exception, e:
            print e
            return LittleTools.MakeJson(500, "")
            pass
        return LittleTools.MakeJson(200, {"username": user_name,
                                              'profile_url': "http://%s/Img/%s/profile" % (Config.Config.ip, user_id)})