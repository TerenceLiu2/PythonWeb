import web
from sys import path
path.append(r'Tools')
path.append(r'Config')
import SQLTools,LittleTools

class TakeActivity:
    def POST(self):
        info=web.input(d={})
        token=info['token'].encode("utf-8")
        activity_id=info['activity_id']
        user_id=LittleTools.certify_token(token)
        if user_id==False:
            return LittleTools.MakeJson(401,"")
        try:
            print "update activity set status=1 where activity_id=%s"%activity_id
            print "update activity set attender_id=%d where activity_id=%s" % (user_id,activity_id)
            SQLTools.UpdateSql("update activity set status=1 where activity_id=%s"%activity_id)
            SQLTools.UpdateSql("update activity set attender_id=%s where activity_id=%s" % (user_id,activity_id))
            return LittleTools.MakeJson(200,"")
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")





