import web
from GraphGo.Tools import SQLTools,LittleTools

class TakeActivity:
    def POST(self):
        info=web.input(d={})
        token=info['token']
        activity_id=info['activity_id']
        user_id=LittleTools.certify_token(token)
        if user_id==False:
            return LittleTools.MakeJson(401,"")
        try:
            SQLTools.UpdateSql("update activity set status=1 where activity_id=%d"%activity_id)
            SQLTools.UpdateSql("update activity set attender_id=%d where activity_id=%d" % (user_id,activity_id))
            return LittleTools.MakeJson(200,"")
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")





