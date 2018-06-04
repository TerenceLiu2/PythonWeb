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
    cur.execute("update user set email='%s',birthday='%s',introduction='%s' where user_id=%s"%(email,birthday,introduction,user_id))
    conn.commit()

def GetActivityFromSql(type,page_num,item_num):
    '''
    
    :param user_id:  
    :param type: Finish Or Not
    :return: 
    '''

    global cur, conn
    if type==0:
        cur.execute("select activity.user_id,content,username,activity_id from activity,user where status=0 and user.user_id=activity.user_id limit %d,%d ;"%((page_num-1)*item_num,item_num))
        return cur.fetchall()
    else:
        cur.execute("select activity.user_id,content,username,activity_id from activity,user where status=1 and user.user_id=activity.user_id limit %s,%s ;"%((page_num-1)*item_num,item_num))
        return cur.fetchall()