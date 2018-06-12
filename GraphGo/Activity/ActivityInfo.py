import web
from sys import path
path.append(r'Tools')
path.append(r'Config')
import Config
import SQLTools, LittleTools


class ActivityInfo:
    def POST(self):
        info=web.input(d={})
        activity_id=info['activity_id']
        try:
            item_list=SQLTools.GetListFromSql("select img_dir from photo where activity_id=%s"%activity_id)
            content=SQLTools.GetOneFromSql("select content from activity where activity_id=%s"%activity_id)
            info_dict={}
            info_dict['content']=content
            info_dict['img_list']=[]
            print item_list
            for item in item_list:
                info_dict['img_list'].append({'img_url':"http://%s/%s#%s" % (Config.Config.ip, item[0],LittleTools.generate_random())})
            print info_dict
            return LittleTools.MakeJson(200,info_dict)
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")