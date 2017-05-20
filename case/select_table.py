# coding: utf-8
#获取表数据量
import pymysql

from vo.Indentity import Indentity

# from vo.InGetRelativeTheme import InGetRelativeTheme


def getMysqlConnect():
    global con
    # con = mdb.connect(host='118.144.248.23', port=3307, user='mmysql', passwd='m12345', db="pengCloud",
    #                   charset='utf8')

    con = pymysql.connect(host='118.144.248.23', port=3307, user='mmysql', passwd='m12345',
                           db='pengCloud')


    return con;
# 获得mysql查询的链接对象

# con = getMysqlConnect()

def bulkData():
    cur = con.cursor(cursorclass=Indentity)
    # 执行语句不变
    cur.execute("select id,name from  pengCloud.identity where parent_id =6 and status =1");

    # cursor = conn.cursor(cursorclass=mdb.cursors.DictCursor)

    # 获取数据方法不变
    # rows = cur.fetchall();
    # for row in rows:
    #     id = row["id"];
    #     print(id);
    #     name = row["name"];
    #     print(name)

