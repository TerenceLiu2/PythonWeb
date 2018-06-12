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
            page_num=int(info_dict['page_num'])
            item_num=int(info_dict['item_num'])
            user_id=LittleTools.certify_token(token)
            if user_id==False:
                return LittleTools.MakeJson(400,"")
            wait_list = SQLTools.GetHistoryFromSql(0, page_num, item_num,user_id)
            finish_list = SQLTools.GetHistoryFromSql(1, page_num, item_num,user_id)
            wait_list_more = SQLTools.GetHistoryFromSql(3, page_num, item_num, user_id)
            finish_list_more = SQLTools.GetHistoryFromSql(4, page_num, item_num, user_id)
            info_dict = {}
            info_dict['wait_list'] = []
            info_dict['finish_list'] = []
            for item in wait_list:
                info_dict['wait_list'].append({'user_id': item[0], 'username': item[2], 'content': item[1],
                                               'profile_url': "http://%s/Img/%d/profile#%s" % (
                                                   Config.Config.ip, item[0],LittleTools.generate_random()), 'activity_id': item[3],'status':item[4],'type':item[5]})
            for item in finish_list:
                info_dict['finish_list'].append({'user_id': item[0], 'username': item[2], 'content': item[1],
                                               'profile_url': "http://%s/Img/%d/profile#%s" % (
                                                   Config.Config.ip, item[0],LittleTools.generate_random()),'img_url': "http://%s/Img/%d/%d/0" % (
                                                Config.Config.ip, item[0], int(item[3])), 'activity_id': item[3]})
            for item in wait_list_more:
                info_dict['wait_list'].append({'user_id': item[0], 'username': item[2], 'content': item[1],
                                               'profile_url': "http://%s/Img/%d/profile#%s" % (
                                                   Config.Config.ip, item[0],LittleTools.generate_random()), 'activity_id': item[3],'status':item[4],'type':item[5]})
            for item in finish_list_more:
                info_dict['finish_list'].append({'user_id': item[0], 'username': item[2], 'content': item[1],
                                               'profile_url': "http://%s/Img/%d/profile#%s" % (
                                                   Config.Config.ip, item[0],LittleTools.generate_random()),'img_url': "http://%s/Img/%d/%d/0" % (
                                                Config.Config.ip, item[0], int(item[3])), 'activity_id': item[3]})
            return LittleTools.MakeJson(200,info_dict)
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")

class UserPhoto:
    def POST(self):
        info_dict = web.input(d={})
        token = info_dict['token'].encode("utf-8")
        page_num = int(info_dict['page_num'])
        item_num = int(info_dict['item_num'])
        user_id = LittleTools.certify_token(token)
        if user_id == False:
            return LittleTools.MakeJson(400, "")
        try:
            photo_list=SQLTools.GetHistoryFromSql(2,page_num,item_num,user_id)
            info_dict = {}
            info_dict['img_list']=[]
            for item in photo_list:
                info_dict['img_list'].append({"img_id":item[0],"img_url":"http://"+Config.Config.ip+"/"+item[1]})
            return LittleTools.MakeJson(200,info_dict)
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")
