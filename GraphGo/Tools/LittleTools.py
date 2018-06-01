#coding=utf-8
import json
import os
import time
import base64
import SQLTools

def generate_token(key, expire=3600):
    r'''
        @Args:
            key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
            expire: int(最大有效时间，单位为s)
        @Return:
            state: str
    '''
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    tk=str(key)+'%'+ts_byte
    b64_tk=base64.urlsafe_b64encode(tk.encode("utf-8"))
    return b64_tk


def certify_token(token):
    r'''
        @Args:
            token: str
        @Returns:
            key
    '''
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    print token_str
    token_list = token_str.split('%')
    if len(token_list) != 2:
        return False
    ts_str = token_list[1]
    if float(ts_str) < time.time():
        # token expired
        return False
    k_str = token_list[0]
    return k_str

def MakeJson(code,msg_dict):
    o_dict={"code":code,"msg":{}}
    o_dict["msg"]=msg_dict
    return json.dumps(o_dict)


def Mkdir(dir_name):
    if os.path.exists(dir_name) is False:
        os.makedirs(dir_name)

def GenerateActivityId(user_id):
    # SQLTools.InitSql('localhost','root','123','GraphGo')
    count=SQLTools.GetOneFromSql("select count(*) from activity where user_id=%d"%user_id)
    activity_id=str(user_id)+"_"+str(count+1)
    print activity_id
    return activity_id