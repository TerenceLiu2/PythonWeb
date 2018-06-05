import web
from sys import path
path.append(r'Tools')
path.append(r'Config')
import Config
import SQLTools, LittleTools



class UserActivity:
    def POST(self):
        try:
            info_dict=web.input(d={})
            token=info_dict['token'].encode("utf-8")
            page_num=info_dict['page_num']
            item_num=info_dict['item_num']
            user_id=LittleTools.certify_token(token)
            if user_id==False:
                return LittleTools.MakeJson(400,"")
            wait_list = SQLTools.GetHistoryFromSql(0, page_num, item_num)
            finish_list = SQLTools.GetHistoryFromSql(1, page_num, item_num)
            info_dict = {}
            info_dict['wait_list'] = []
            for item in wait_list:
                info_dict['wait_list'].append({'user_id': item[0], 'username': item[2], 'content': item[1],
                                               'profile_url': "http://%s/Img/%d/profile" % (
                                                   Config.Config.ip, item[0]), 'activity_id': item[3],'status':item[4]})
            info_dict['finish_list']=[]
            for item in finish_list:
                info_dict['finish_list'].append({'user_id': item[0], 'username': item[2], 'content': item[1],
                                               'profile_url': "http://%s/Img/%d/profile" % (
                                                   Config.Config.ip, item[0]),'img_url': "http://%s/Img/%d/%d/0" % (
                                                Config.Config.ip, item[0], int(item[3])), 'activity_id': item[3]})
            return LittleTools.MakeJson(200,info_dict)
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")

class UserPhoto:
    def POST(self):
        info_dict = web.input(d={})
        token = info_dict['token'].encode("utf-8")
        page_num = info_dict['page_num']
        item_num = info_dict['item_num']
        user_id = LittleTools.certify_token(token)
        if user_id == False:
            return LittleTools.MakeJson(400, "")
        try:
            photo_list=SQLTools.GetHistoryFromSql(3,page_num,item_num)
            info_dict = {}
            info_dict['photo_list'] = photo_list
            return LittleTools.MakeJson(200,info_dict)
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")
