import MySQLdb

def InitSql(hostname,user,password,db):
    global conn,cur
    conn=MySQLdb.Connect(host=hostname,user=user,passwd=password,db=db,charset="utf8")
    cur=conn.cursor()

def InsertSql(sql):
    global cur,conn
    InitSql('localhost', 'root', '123', 'GraphGo')
    cur.execute(sql)
    conn.commit()
    conn.close()

def UpdateSql(sql):
    global cur, conn
    InitSql('localhost', 'root', '123', 'GraphGo')
    cur.execute(sql)
    conn.commit()
    conn.close()

def GetOneFromSql(sql):
    global cur, conn
    InitSql('localhost', 'root', '123', 'GraphGo')
    cur.execute(sql)
    one=cur.fetchone()
    if one:
        conn.close()
        return one[0]
    else:
        conn.close()
        return None


def GetListFromSql(sql):
    global cur, conn
    InitSql('localhost', 'root', '123', 'GraphGo')
    cur.execute(sql)
    one = cur.fetchall()
    if one:
        conn.close()
        return one
    else:
        conn.close()
        return None


def UpdateUserInfo(user_id,phone_number,email,birthday,introduction):
    global cur, conn
    InitSql('localhost', 'root', '123', 'GraphGo')
    cur.execute("update user set email='%s',birthday='%s',introduction='%s',phone_number='%s' where user_id=%s"%(email,birthday,introduction,phone_number,user_id))
    conn.commit()
    conn.close()

def GetHistoryFromSql(type,page_num,item_num,user_id):
    global cur, conn
    InitSql('localhost', 'root', '123', 'GraphGo')
    if type==0:
        if page_num==0:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where (status=0 or status=1) and user.user_id=activity.user_id and user.user_id=%s;"%user_id)
            a_list=cur.fetchall()
            conn.close()
            return a_list
        else:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where (status=0 or status=1) and user.user_id=activity.user_id and user.user_id=%s limit %d,%d ;"%(user_id,(page_num-1)*item_num,item_num))
            a_list = cur.fetchall()
            conn.close()
            return a_list
    elif type==1:
        if page_num==0:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where status=2 and user.user_id=activity.user_id and user.user_id=%s;"%user_id)
            a_list = cur.fetchall()
            conn.close()
            return a_list
        else:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where status=2 and user.user_id=activity.user_id and user.user_id=%s limit %d,%d ;"%(user_id,(page_num-1)*item_num,item_num))
            a_list = cur.fetchall()
            conn.close()
            return a_list
    elif type==2:
        cur.execute("select img_id,img_dir from photo where user_id=%s"%user_id)
        print "select img_id,img_dir from photo where user_id=%s" % user_id
        a_list = cur.fetchall()
        conn.close()
        return a_list
    elif type==4:
        cur.execute(
            "select activity.user_id,content,username,activity_id,status from activity,user where status=2 and user.user_id=activity.user_id and attender_id=%s ;" % (
                user_id))
        a_list=cur.fetchall()
        conn.close()
        return a_list
    elif type == 3:
        cur.execute(
            "select activity.user_id,content,username,activity_id,status from activity,user where (status=1 or status=0) and user.user_id=activity.user_id and attender_id=%s ;" % (
                user_id))
        a_list = cur.fetchall()
        conn.close()
        return a_list

def GenerateNotice(type,creater,attender,activity):
    global cur, conn
    InitSql('localhost', 'root', '123', 'GraphGo')
    cur.execute("insert into notice (activity_id,creater_id,attender_id,type) value(%s,%s,%s,%s)"%(activity,creater,attender,type))
    conn.commit()
    conn.close()




def GetActivityFromSql(type,page_num,item_num):
    '''
    
    :param user_id:  
    :param type: Finish Or Not
    :return: 
    '''

    global cur, conn
    InitSql('localhost', 'root', '123', 'GraphGo')
    if type==0:
        if page_num==0:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where (status=0 or status=1) and user.user_id=activity.user_id;")
        else:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where (status=0 or status=1) and user.user_id=activity.user_id limit %d,%d ;"%((page_num-1)*item_num,item_num))
        list=cur.fetchall()
        conn.close()
        return list
    else:
        if page_num==0:
            cur.execute("select activity.user_id,content,username,activity_id,status from activity,user where status=2 and user.user_id=activity.user_id;")
        else:
            cur.execute("select activity.user_id,content,username,activity_id from activity,user where status=2 and user.user_id=activity.user_id limit %s,%s ;"%((page_num-1)*item_num,item_num))
        list = cur.fetchall()
        conn.close()
        return list

def GetNoticeFromSql(user_id,type):
    global cur,conn
    InitSql('localhost', 'root', '123', 'GraphGo')
    if type==0:
        cur.execute("select content,username,notice.type from notice,activity,user where creater_id=%s and activity.activity_id=notice.activity_id and user.user_id=notice.attender_id and notice.type=0;"%user_id)
        notice_list=[]
        for item in cur.fetchall():
            content="'"+item[1]+"'take part in'"+item[0]+"'"
            notice_list.append({'content':content})
        conn.close()
        return notice_list
    elif type==1:
        cur.execute("select content,username,notice.type from notice,activity,user where notice.attender_id=%s and activity.activity_id=notice.activity_id and user.user_id=notice.attender_id and notice.type=1;"%user_id)
        notice_list=[]
        for item in cur.fetchall():
            content=item[0]+" is end"
            notice_list.append({'content':content})
        conn.close()
        return notice_list