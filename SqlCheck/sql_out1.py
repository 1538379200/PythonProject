import xlwt
import pymysql
import time
import sys
#连接数据库


#获取日期
today = time.strftime('%Y-%m-%d')

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
worksheet_1 = workbook.add_sheet('超过1000OGT人数')
worksheet_2 = workbook.add_sheet('邀请人信息')
worksheet_3 = workbook.add_sheet('注册人信息')
worksheet_4 = workbook.add_sheet('挖矿返佣总数')
worksheet_5 = workbook.add_sheet('退出守护计划')
worksheet_6 = workbook.add_sheet('加入守护计划')
worksheet_7 = workbook.add_sheet('成为初级节点人数')
worksheet_8 = workbook.add_sheet('取消初级节点人数')
worksheet_9 = workbook.add_sheet('挖矿收益')
worksheet_10 = workbook.add_sheet('新增超级节点')
worksheet_11 = workbook.add_sheet('取消超级节点用户')
worksheet_12 = workbook.add_sheet('初级节点收益')
worksheet_13 = workbook.add_sheet('超级节点收益')
worksheet_14 = workbook.add_sheet('守护计划收益')
worksheet_15 = workbook.add_sheet('节点加成收益')
worksheet_16 = workbook.add_sheet('用户充值eth总额')
worksheet_17 = workbook.add_sheet('用户兑换token总额')
#设置所有30行列宽为18
all_sheet=[worksheet_1,worksheet_2,worksheet_3,worksheet_4,worksheet_5,worksheet_6,worksheet_7,worksheet_8,worksheet_9,
           worksheet_10,worksheet_11,worksheet_12,worksheet_13,worksheet_14,worksheet_15,worksheet_16,worksheet_17]
for i in all_sheet:
    for f in range (30):
        i.col(f).width = 256*20

class SqlOut():
    def __init__(self,Starttime,Endtime):
        self.Starttime = Starttime
        self.Endtime = Endtime
    #查询超过1000ogt人数：
    def OGT(self):

        worksheet_1.write(0,0,'用户ID',style)
        worksheet_1.write(0,1,'手机号',style)
        worksheet_1.write(0,2,'昵称',style)
        worksheet_1.write(0,3,'积分',style)
        worksheet_1.write(0,4,'锁定积分',style)
        worksheet_1.write(0,5,'扩展积分',style)
        worksheet_1.write(0,6,'冻结积分',style)
        worksheet_1.write(0,7,'积分总数',style)
        cursor.execute("select uid,mobile,nick_name,balance,lock_integral,withdraw_integral,holdlock_integral from user.user_integral u LEFT JOIN useraccount a on a.id =u.uid  where balance+lock_integral+holdlock_integral >=100000 and integral_type=2;")
        data = cursor.fetchall()
        raw = 1
        for i in data:
            uid = i[0]
            mobile = i[1]
            nike_name=i[2]
            balance=i[3]
            lock_integral=i[4]
            withdraw_integral=i[5]
            holdlock_integral=i[6]
            Sum_score = i[3]+i[4]+i[5]+i[6]
            worksheet_1.write(raw,0,uid,style2)
            worksheet_1.write(raw,1,mobile,style2)
            worksheet_1.write(raw,2,nike_name,style2)
            worksheet_1.write(raw,3,balance,style2)
            worksheet_1.write(raw,4,lock_integral,style2)
            worksheet_1.write(raw,5,withdraw_integral,style2)
            worksheet_1.write(raw,6,holdlock_integral,style2)
            worksheet_1.write(raw,7,Sum_score,style2)
            raw+=1

    #查询邀请人信息
    def Yaoqing(self):
        worksheet_2.write(0,0,'用户ID',style)
        worksheet_2.write(0,1,'手机号',style)
        worksheet_2.write(0,2,'昵称',style)
        worksheet_2.write(0,3,'创建时间',style)
        cursor.execute("select  DISTINCT(id),mobile,nick_name,create_time from user.useraccount where id in (select referenceId from useraccount    where create_time>=%r AND create_time<=%r and referenceId is not null);"%(self.Starttime,self.Endtime))
        data_2=cursor.fetchall()
        raw=1
        for i in data_2:
            uid = i[0]
            mobile=i[1]
            nike_name=i[2]
            create_time=str(i[3])
            worksheet_2.write(raw,0,uid,style2)
            worksheet_2.write(raw,1,mobile,style2)
            worksheet_2.write(raw,2,nike_name,style2)
            worksheet_2.write(raw,3,create_time,style2)
            raw+=1

    #查询注册人信息
    def Zhuce(self):
        raw=1
        worksheet_3.write(0,0,'用户ID',style)
        worksheet_3.write(0,1,'用户手机号',style)
        worksheet_3.write(0,2,'昵称',style)
        worksheet_3.write(0,3,'邀请人ID',style)
        worksheet_3.write(0,4,'创建时间',style)
        cursor.execute("SELECT a.id,a.mobile,a.nick_name,a.referenceId,a.create_time FROM user.useraccount a WHERE a.create_time >=%r and  a.create_time <=%r AND a.referenceId IS NOT NULL;"%(self.Starttime,self.Endtime))
        data=cursor.fetchall()
        for i in  data:
            uid = i[0]
            mobile=i[1]
            nike_name=i[2]
            refernceid=i[3]
            create_time=str(i[4])
            worksheet_3.write(raw,0,uid,style2)
            worksheet_3.write(raw,1,mobile,style2)
            worksheet_3.write(raw,2,nike_name,style2)
            worksheet_3.write(raw,3,refernceid,style2)
            worksheet_3.write(raw,4,create_time,style2)
            raw+=1

    #挖矿返佣总数：
    def Wakuang(self):
        worksheet_4.write(0,0,'返佣总数',style)
        cursor.execute("select  sum(score) from user.user_integral_income   u where u.create_time >=%r and  u.create_time <=%r   and u.source ='41';"%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            SumF=i[0]
            worksheet_4.write(1,0,SumF,style2)

    #退出守护计划人数和积分
    def TuiShouhu(self):
        worksheet_5.write(0,0,'积分总数',style)
        worksheet_5.write(0,1,'退出人数',style)
        cursor.execute("select  sum(score),count(id) from user.user_integral_income   u where u.create_time >=%r and  u.create_time <=%r   and u.source ='59';"%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            SumC=i[0]
            Count=i[1]
            worksheet_5.write(1,0,SumC,style2)
            worksheet_5.write(1,1,Count,style2)

    #加入守护计划：
    def JiaruShouhu(self):
        raw=1
        worksheet_6.write(0,0,'用户ID',style)
        worksheet_6.write(0,1,'积分数量',style)
        worksheet_6.write(0,2,'说明',style)
        worksheet_6.write(0,3,'创建时间',style)
        cursor.execute("select  uid,score,description,u.create_time from user.user_integral_out   u where u.create_time >=%r and  u.create_time <=%r   and u.source ='58';"%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            uid = i[0]
            score=i[1]
            des=i[2]
            create_time=str(i[3])
            worksheet_6.write(raw,0,uid,style2)
            worksheet_6.write(raw,0,score,style2)
            worksheet_6.write(raw,0,des,style2)
            worksheet_6.write(raw,0,create_time,style2)
            raw+=1

    #成为初级节点人数
    def BeJiedain(self):
        raw=1
        worksheet_7.write(0,0,'用户ID',style)
        worksheet_7.write(0,1,'手机号',style)
        worksheet_7.write(0,2,'昵称',style)
        worksheet_7.write(0,3,'成为时间',style)
        cursor.execute("SELECT u.uid,a.mobile, a.nick_name,u.node_time FROM user.`user` u,useraccount a WHERE a.id=u.uid AND u.identity='2' AND u.node_time >=%r and  u.node_time <=%r ORDER BY u.node_time;"%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            uid = i[0]
            mobile = i[1]
            nike_name=i[2]
            node_time=str(i[3])
            worksheet_7.write(raw,0,uid,style2)
            worksheet_7.write(raw,1,mobile,style2)
            worksheet_7.write(raw,2,nike_name,style2)
            worksheet_7.write(raw,3,node_time,style2)
            raw+=1

    #取消初级节点人数：
    def CancelChuji(self):
        raw = 1
        worksheet_8.write(0,0,'用户ID',style)
        worksheet_8.write(0,1,'手机号',style)
        worksheet_8.write(0,2,'昵称',style)
        worksheet_8.write(0,3,'身份状态',style)
        worksheet_8.write(0,4,'取消时间',style)
        cursor.execute("SELECT u.uid,a.mobile,a.nick_name,u.identity,u.cancel_time FROM user.`user` u ,user.useraccount a  WHERE u.uid=a.id AND u.identity='2' AND u.cancel_time is NOT NULL ORDER BY u.cancel_time; ")
        data = cursor.fetchall()
        for i in data:
            uid = i[0]
            mobile = i[1]
            nike_name=i[2]
            iden=i[3]
            cancel_time=str(i[4])
            worksheet_8.write(raw,0,uid,style2)
            worksheet_8.write(raw,1,mobile,style2)
            worksheet_8.write(raw,2,nike_name,style2)
            worksheet_8.write(raw,3,iden,style2)
            worksheet_8.write(raw,4,cancel_time,style2)
            raw+=1

    #挖矿收益：
    def WkShouyi(self):
        raw=1
        worksheet_9.write(0,0,'用户ID',style)
        worksheet_9.write(0,1,'分值',style)
        worksheet_9.write(0,2,'状态',style)
        worksheet_9.write(0,3,'创建时间',style)
        cursor.execute("SELECT t.uid,t.score,t.`status`,t.create_time FROM user.user_task t WHERE source_type='40' AND create_time >=%r and create_time <=%r ORDER BY t.create_time;"%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            uid = i[0]
            score=i[1]
            status=i[2]
            create_time=str(i[3])
            worksheet_9.write(raw,0,uid,style2)
            worksheet_9.write(raw,1,score,style2)
            worksheet_9.write(raw,2,status,style2)
            worksheet_9.write(raw,3,create_time,style2)
            raw+=1

    #新增超级节点
    def Superuser(self):
        raw = 1
        worksheet_10.write(0,0,'用户ID',style)
        worksheet_10.write(0,1,'手机号',style)
        worksheet_10.write(0,2,'昵称',style)
        worksheet_10.write(0,3,'身份',style)
        worksheet_10.write(0,4,'成为时间',style)
        cursor.execute("SELECT u.uid,a.mobile,a.nick_name,u.identity,u.node_time FROM user.`user` u,user.useraccount a  WHERE u.uid=a.id AND u.identity='3' AND u.node_time >=%r and  u.node_time <=%r ORDER BY u.node_time;"%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            uid = i[0]
            mobile = i[1]
            nike_name=i[2]
            iden=i[3]
            node_time=str(i[4])
            worksheet_10.write(raw,0,uid,style2)
            worksheet_10.write(raw,1,mobile,style2)
            worksheet_10.write(raw,2,nike_name,style2)
            worksheet_10.write(raw,3,iden,style2)
            worksheet_10.write(raw,4,node_time,style2)
            raw += 1

    #取消超级节点
    def CancelSuperuser(self):
        raw = 1
        worksheet_11.write(0, 0, '用户ID',style)
        worksheet_11.write(0, 1, '手机号',style)
        worksheet_11.write(0, 2, '昵称',style)
        worksheet_11.write(0, 3, '身份状态',style)
        worksheet_11.write(0, 4, '取消时间',style)
        cursor.execute(
            "SELECT u.uid,a.mobile,a.nick_name,u.identity,u.cancel_time FROM user.`user` u ,user.useraccount a  WHERE u.uid=a.id AND u.identity='3' AND u.cancel_time is NOT NULL ORDER BY u.cancel_time; ")
        data = cursor.fetchall()
        for i in data:
            uid = i[0]
            mobile = i[1]
            nike_name = i[2]
            iden = i[3]
            cancel_time = str(i[4])
            worksheet_11.write(raw, 0, uid,style2)
            worksheet_11.write(raw, 1, mobile,style2)
            worksheet_11.write(raw, 2, nike_name,style2)
            worksheet_11.write(raw, 3, iden,style2)
            worksheet_11.write(raw, 4, cancel_time,style2)
            raw += 1

    #初级节点收益
    def ChujiShouyi(self):
        raw = 1
        worksheet_12.write(0,0,'用户ID1',style)
        worksheet_12.write(0,1,'用户ID2',style)
        worksheet_12.write(0,2,'身份',style)
        worksheet_12.write(0,3,'收益类型',style)
        worksheet_12.write(0,4,'分值',style)
        worksheet_12.write(0,5,'创建时间',style)
        worksheet_12.write(0,6,'收益状态',style)
        cursor.execute("SELECT u.uid,t.uid,u.identity,t.source_type,t.score,t.create_time,t.`status` FROM user.`user`u ,user.user_task t WHERE t.uid=u.uid AND t.source_type='50' AND t.create_time>=%r AND t.create_time<=%r AND u.identity='2' ORDER BY t.create_time;"%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            uid1 = i[0]
            uid2 = i[1]
            iden = i[2]
            score_type = i[3]
            score = i[4]
            create_time=str(i[5])
            status = i[6]
            worksheet_12.write(raw,0,uid1,style2)
            worksheet_12.write(raw,1,uid2,style2)
            worksheet_12.write(raw,2,iden,style2)
            worksheet_12.write(raw,3,score_type,style2)
            worksheet_12.write(raw,4,score,style2)
            worksheet_12.write(raw,5,create_time,style2)
            worksheet_12.write(raw,6,status,style2)
            raw+=1

    #超级节点收益
    def SuperShouyi(self):
        raw = 1
        worksheet_13.write(0, 0, '用户ID1',style)
        worksheet_13.write(0, 1, '用户ID2',style)
        worksheet_13.write(0, 2, '身份',style)
        worksheet_13.write(0, 3, '收益类型',style)
        worksheet_13.write(0, 4, '分值',style)
        worksheet_13.write(0, 5, '创建时间',style)
        worksheet_13.write(0, 6, '收益状态',style)
        cursor.execute(
            "SELECT u.uid,t.uid,u.identity,t.source_type,t.score,t.create_time,t.`status` FROM user.`user`u ,user.user_task t WHERE t.uid=u.uid AND t.source_type='50' AND t.create_time>=%r AND t.create_time<=%r AND u.identity='3' ORDER BY t.create_time;" % (
            self.Starttime, self.Endtime))
        data = cursor.fetchall()
        for i in data:
            uid1 = i[0]
            uid2 = i[1]
            iden = i[2]
            score_type = i[3]
            score = i[4]
            create_time = str(i[5])
            status = i[6]
            worksheet_13.write(raw, 0, uid1,style2)
            worksheet_13.write(raw, 1, uid2,style2)
            worksheet_13.write(raw, 2, iden,style2)
            worksheet_13.write(raw, 3, score_type,style2)
            worksheet_13.write(raw, 4, score,style2)
            worksheet_13.write(raw, 5, create_time,style2)
            worksheet_13.write(raw, 6, status,style2)
            raw += 1

    #守护计划收益
    def ShouhuSy(self):
        raw=1
        worksheet_14.write(0,0,'ID',style)
        worksheet_14.write(0,1,'用户ID',style)
        worksheet_14.write(0,2,'收益额度',style)
        worksheet_14.write(0,3,'身份',style)
        worksheet_14.write(0,4,'创建时间',style)
        cursor.execute("SELECT * FROM user.hold_profile p WHERE p.identity='1' AND p.create_time>=%r AND p.create_time<=%r ORDER BY p.create_time;"%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            sql_id=i[0]
            uid=i[1]
            prof=i[2]
            iden=i[3]
            create_time=str(i[4])
            worksheet_14.write(raw,0,sql_id,style2)
            worksheet_14.write(raw,1,uid,style2)
            worksheet_14.write(raw,2,prof,style2)
            worksheet_14.write(raw,3,iden,style2)
            worksheet_14.write(raw,4,create_time,style2)
            raw+=1

    #节点加成收益数据：
    def JiedianSY(self):
        raw = 1
        worksheet_15.write(0, 0, 'ID',style)
        worksheet_15.write(0, 1, '用户ID',style)
        worksheet_15.write(0, 2, '收益额度',style)
        worksheet_15.write(0, 3, '身份',style)
        worksheet_15.write(0, 4, '创建时间',style)
        cursor.execute(
            "SELECT * FROM user.hold_profile p WHERE p.identity in (2,3) AND p.create_time>=%r AND p.create_time<=%r ORDER BY p.create_time;" % (
            self.Starttime, self.Endtime))
        data = cursor.fetchall()
        for i in data:
            sql_id = i[0]
            uid = i[1]
            prof = i[2]
            iden = i[3]
            create_time = str(i[4])
            worksheet_15.write(raw, 0, sql_id,style2)
            worksheet_15.write(raw, 1, uid,style2)
            worksheet_15.write(raw, 2, prof,style2)
            worksheet_15.write(raw, 3, iden,style2)
            worksheet_15.write(raw, 4, create_time,style2)
            raw += 1

    #用户充值总额
    def ETH(self):
        worksheet_16.write(0,0,'充值到账ogt总额',style)
        cursor.execute("SELECT SUM(e.arrive_quantity) FROM user.user_convert_eth e WHERE create_time>=%r AND create_time<=%r AND `status`=2; "%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            SumOGT=i[0]
            worksheet_16.write(1,0,SumOGT,style2)

    #用户兑换token：
    def Token(self):
        worksheet_17.write(0,0,'兑换token总额',style)
        cursor.execute("SELECT SUM(ogt_quantity) FROM user.user_convert_token t WHERE t.`status`=2 AND t.create_time>=%r AND t.create_time<=%r;"%(self.Starttime,self.Endtime))
        data = cursor.fetchall()
        for i in data:
            SumToken=i[0]
            worksheet_17.write(1,0,SumToken,style2)

        # OGT()
        # Yaoqing()
        # Zhuce()
        # Wakuang()
        # TuiShouhu()
        # JiaruShouhu()
        # BeJiedain()
        # CancelChuji()
        # WkShouyi()
        # Superuser()
        # CancelSuperuser()
        # ChujiShouyi()
        # SuperShouyi()
        # ShouhuSy()
        # JiedianSY()
        # ETH()
        # Token()
        # workbook.save('%r导出文件.xls'%today)
        # input('导出成功^_^!输入任意字符或回车可退出程序：')
        # cursor.close()
        # db.close()

