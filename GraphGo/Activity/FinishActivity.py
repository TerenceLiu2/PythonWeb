import web
from sys import path
path.append(r'Tools')
path.append(r'Config')
import SQLTools,LittleTools

class FinishActivity:
    def POST(self):
        info=web.input(d={})
        token=info['token'].encode("utf-8")
        activity_id=info['activity_id']
        content=info['content']
        size=int(info['size'])
        user_id=LittleTools.certify_token(token)
        print size,activity_id
        if user_id==False:
            return LittleTools.MakeJson(400,"")
        try:
            for i in range(size):
                LittleTools.Mkdir("Img/%s/%s/"%(user_id,activity_id))
                img_dir="Img/%s/%s/%d"%(user_id,activity_id,i)
                with open(img_dir,"w") as wf:
                    wf.write(info["p"+str(i)])
                    SQLTools.InsertSql("insert into photo (user_id,img_dir,activity_id) value(%s,'%s',%s)"%(user_id,img_dir,activity_id))
            SQLTools.UpdateSql("update activity set status=2 where activity_id=%s" % activity_id)
            SQLTools.UpdateSql("update activity set content='%s' where activity_id=%s" % (content, activity_id))
            return LittleTools.MakeJson(200,"")
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")





