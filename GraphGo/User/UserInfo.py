import web
from sys import path
path.append(r'Tools')
path.append(r'Config')
import Config
import SQLTools, LittleTools


class UserInfoUpload:
    def POST(self):
        info_dict = web.input(d={})
        token = info_dict['token']
        user_id = LittleTools.certify_token(token.encode("utf-8"))
        if user_id==False:
            return LittleTools.MakeJson(400,"")
        try:
            profile = info_dict['profile']
            phone_number=info_dict['phone_number']
            email=info_dict['email']
            birthday=info_dict['birthday']
            introduction=info_dict['introduction']
            print phone_number,email,birthday,introduction
            SQLTools.UpdateUserInfo(user_id, phone_number, email, birthday, introduction)
            LittleTools.Mkdir("Img/"+str(user_id))
            LittleTools.SaveSmallImg(profile,"Img/"+str(user_id)+"/profile")
            # fwrite=open("Img/"+str(user_id)+"/profile",'w')
            # fwrite.write(profile)
            return LittleTools.MakeJson(200,"")
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")




class UserBasicInfo:
    def POST(self):
        token=web.input()
        print token['token']
        user_id = LittleTools.certify_token(token['token'].encode("utf-8"))
        if user_id==False:
            return LittleTools.MakeJson(400,"")
        try:
            user_name=SQLTools.GetOneFromSql("select username from user where user_id=%s"%user_id)
        except Exception,e:
            print e
            return LittleTools.MakeJson(500,"")
            pass
        if token!=None:
            print "http://"+Config.Config.ip+"/Img/"+str(user_id)+"/profile"
            return LittleTools.MakeJson(200, {"username":user_name,"profile":"http://"+Config.Config.ip+"/Img/"+str(user_id)+"/profile"})
        else:
            return LittleTools.MakeJson(401, "")




