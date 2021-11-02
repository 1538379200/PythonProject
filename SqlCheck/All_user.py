import pymysql
import time
import sys

try:
    db = pymysql.connect(host='192.168.3.199',user='anying',password='tomcat',database='user0111',port=13306)
    print('数据库连接成功')
except:
    print('数据库连接超时')
    a = input('输入任意字符或回车退出程序：')
    sys.exit()
cursor = db.cursor()

def sql_user():
    cursor.execute("SELECT i.uid,i.amt,i.score,i.status,i.type FROM user_integral_income i WHERE i.`status`='1' and i.type='2' ORDER BY i.uid")
    data = cursor.fetchall()
    s = len(data)
    for i in data:
        uid = i[0]
        amt = i[1]
        score = i[2]
        stype = i[3]


