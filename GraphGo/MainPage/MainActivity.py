import web
from sys import path
path.append(r'Tools')
path.append(r'Config')
import Config
import SQLTools, LittleTools


class MainWait:
    def POST(self):
        info=web.input(d={})
        page_num=int(info['page_num'])
        item_num=int(info['item_num'])
        try:
            item_list=SQLTools.GetActivityFromSql(0,page_num,item_num)
            info_dict={}
            info_dict['item_list']=[]
            for item in item_list:
                info_dict['item_list'].append({'user_id':item[0],'username':item[2],'content':item[1],'img_url':"http://%s/Img/%d/profile" % (
                    Config.Config.ip, item[0]),'activity_id':item[3]})
            return LittleTools.MakeJson(200,info_dict)
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")

class MainFinish:
    def POST(self):
        info = web.input(d={})
        page_num = int(info['page_num'])
        item_num = int(info['item_num'])
        try:
            item_list=SQLTools.GetActivityFromSql(1,page_num,item_num)
            info_dict={}
            info_dict['item_list']=[]
            for item in item_list:
                info_dict['item_list'].append({'user_id':item[0],'username':item[2],'content':item[1],'profile_url':"http://%s/Img/%d/profile"% (
                Config.Config.ip, item[0]), 'img_url': "http://%s/Img/%d/%d/0" % (
                Config.Config.ip, item[0], int(item[3])),'activity_id':item[3]})
            print info_dict
            return LittleTools.MakeJson(200,info_dict)
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")






