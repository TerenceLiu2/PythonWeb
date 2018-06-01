import web

from GraphGo.Tools import SQLTools, LittleTools


class UserActivity:
    def POST(self):
        try:
            info_dict=web.input(d={})
            token=info_dict['token']
            page_num=info_dict['page_num']
            item_num=info_dict['item_num']
            user_id=LittleTools.certify_token(token)
            SQLTools.GetActivityFromSql(3,page_num,item_num)
            return LittleTools.MakeJson(200,"")
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")