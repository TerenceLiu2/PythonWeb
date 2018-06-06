import MySQLdb

def InitSql(hostname,user,password,db):
    global conn,cur
    conn=MySQLdb.Connect(host=hostname,user=user,passwd=password,db=db,charset="utf8")
    cur=conn.cursor()

def InsertSql(sql):
    global cur,conn
    cur.execute(sql)
    conn.commit()

def UpdateSql(sql):
    global cur, conn
    cur.execute(sql)
    conn.commit()

def GetOneFromSql(sql):
    global cur, conn
    cur.execute(sql)
    one=cur.fetchone()
    if one:
        return one[0]
    else:
        return None

def GetListFromSql(sql):
    global cur, conn
    cur.execute(sql)
    one = cur.fetchone()
    if one:
        return one
    else:
        return None


def UpdateUserInfo(user_id,phone_number,email,birthday,introduction):
    global cur, conn
    cur.execute("update user set email='%s',birthday='%s',introduction='%s',phone_number='%s' where user_id=%s"%(email,birthday,introduction,phone_number,user_id))
    conn.commit()

def GetHistoryFromSql(type,page_num,item_num,user_id):
    global cur, conn
    if type==0:
        if page_num==0:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where (status=0 or status=1) and user.user_id=activity.user_id and user.user_id=%s;"%user_id)
            return cur.fetchall()
        else:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where (status=0 or status=1) and user.user_id=activity.user_id and user.user_id=%s limit %d,%d ;"%(user_id,(page_num-1)*item_num,item_num))
            return cur.fetchall()
    elif type==1:
        if page_num==0:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where status=2 and user.user_id=activity.user_id and user.user_id=%s;"%user_id)
            return cur.fetchall()
        else:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where status=2 and user.user_id=activity.user_id and user.user_id=%s limit %d,%d ;"%(user_id,(page_num-1)*item_num,item_num))
            return cur.fetchall()
    elif type==2:
        cur.execute("select img_id,img_dir from photo where user_id=%s"%user_id)
        print "select img_id,img_dir from photo where user_id=%s" % user_id
        return cur.fetchall()




def GetActivityFromSql(type,page_num,item_num):
    '''
    
    :param user_id:  
    :param type: Finish Or Not
    :return: 
    '''

    global cur, conn
    if type==0:
        if page_num==0:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where (status=0 or status=1) and user.user_id=activity.user_id;")
        else:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where (status=0 or status=1) and user.user_id=activity.user_id limit %d,%d ;"%((page_num-1)*item_num,item_num))
        return cur.fetchall()
    else:
        if page_num==0:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where (status=0 or status=1) and user.user_id=activity.user_id;")
        else:
            cur.execute("select activity.user_id,content,username,activity_id from activity,user where status=2 and user.user_id=activity.user_id limit %s,%s ;"%((page_num-1)*item_num,item_num))
        return cur.fetchall()

def GetNoticeFromSql(user_id):
    global cur,conn
    cur.execute("select content,username from notice,activity,user where creater_id=%s and activity.activity_id=notice.activity_id and user.user_id=notice.attender_id;"%user_id)
    notice_list=[]
    for item in cur.fetchall():
        content="'"+item[1]+"'take part in'"+item[0]+"'"
        notice_list.append({'content':content})
    return notice_list