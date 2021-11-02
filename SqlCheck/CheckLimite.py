import pymysql
import xlwt
import sys
import time

#连接数据库
use_db = input('输入需要使用的数据库：')
try:
    db = pymysql.connect(host='192.168.3.199',user='anying',password='tomcat',database='%s'%use_db,port=13306)
    print('数据库连接成功')
except:
    print('数据库连接超时')
    a = input('输入任意字符或回车退出程序：')
    sys.exit()
cursor = db.cursor()

# SuserID = input('输入需要查询的用户ID：')

#设置表格样式
font = xlwt.Font()  #字体设置
font.bold = True
font.height = 20*12

pattern = xlwt.Pattern()  #背景颜色设置
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 44

alignment = xlwt.Alignment()  #设置居中对齐
alignment.horz = 0x02
alignment.vert = 0x01

border = xlwt.Borders() #设置边框
border.left=6
border.right=6
border.top=6
border.bottom=6
border.bottom_colour=0x3A

style = xlwt.XFStyle()  #初始化样式
style.font=font
style.pattern=pattern
style.alignment=alignment
style.borders=border

font2 = xlwt.Font()  #样式2的字体
font2.height = 20*11
style2 = xlwt.XFStyle()  #初始化样式2
style2.alignment = alignment
style2.font = font2

#打开表格：
workbook = xlwt.Workbook(encoding='GBK')
sheet = workbook.add_sheet('团队人数')


#设置列宽
all_sheet = [sheet]
for i in all_sheet:
    for f in range (30):
        i.col(f).width = 256*20


user_id = []
a = 1

def getID(id,count):
    if count == 2:
        print('--------------------------------直邀用户-------------------------------------')
    elif count == 3:
        print('--------------------------------间邀用户-------------------------------------')
    elif count == 4:
        print('--------------------------------三代以上用户-------------------------------------')
    data = []
    for i in id:
        for f in i:
            print(f)
            cursor.execute("SELECT a.id FROM useraccount a WHERE a.referenceId =%r;"%f)
            some_id = cursor.fetchall()
            for g in some_id:
                data.append(g)
    user_id.append(data)
    # if len(data)==0:
    if count == 3 or len(data)==0:
        return id
    else:
        count += 1
        return getID(data,count)



def SaveExcle():
    raw = 1
    sheet.write(0,0,'user表id',style)
    sheet.write(0,1,'积分表id',style)
    sheet.write(0,2,'手机号',style)
    sheet.write(0,3,'邀请人ID',style)
    sheet.write(0,4,'balance',style)
    sheet.write(0,5,'free_integral',style)
    sheet.write(0,6,'holdlock_integral',style)
    sheet.write(0,7,'lock_integral',style)
    sheet.write(0,8,'withdraw_integral',style)
    sheet.write(0,9,'积分类型（1起源、2节点）',style)
    sheet.write(0,10,'create_time',style)
    for i in user_id:
        for g in i:
            for z in g:
                cursor.execute("SELECT a.id,i.uid,a.mobile,a.referenceId,i.balance,i.free_integral,i.holdlock_integral,i.lock_integral,i.withdraw_integral,i.integral_type,i.create_time FROM useraccount a LEFT JOIN user_integral i ON a.id=i.uid WHERE a.id=%r;" %z)
                data = cursor.fetchall()
                for i in data:
                    ID = i[0]
                    uid = i[1]
                    mobile = i[2]
                    reID= i[3]
                    balance = i[4]
                    free = i[5]
                    hold = i[6]
                    lock = i[7]
                    wid = i[8]
                    sty = i[9]
                    ctime = i[10]
                    sheet.write(raw,0,ID,style2)
                    sheet.write(raw,1,uid,style2)
                    sheet.write(raw,2,mobile,style2)
                    sheet.write(raw,3,reID,style2)
                    sheet.write(raw,4,balance,style2)
                    sheet.write(raw,5,free,style2)
                    sheet.write(raw,6,hold,style2)
                    sheet.write(raw,7,lock,style2)
                    sheet.write(raw,8,wid,style2)
                    sheet.write(raw,9,sty,style2)
                    sheet.write(raw,10,ctime,style2)
                    raw += 1


if __name__ == '__main__':
    this_id = input('请输入需要查询的用户ID：')
    Inthis = int(this_id)
    print('开始导出用户ID……')
    getID((((Inthis,)),),1)
    time.sleep(2)
    # for i in user_id:
    #     for g in i:
    #         print(g[0])
    print('开始导出用户数据表……')
    SaveExcle()
    workbook.save('导出%r用户团队%r数据.xls'%(this_id,use_db))
    input("数据导出成功，文件在程序目录，按任意键可退出程序：")
    cursor.close()
    db.close()