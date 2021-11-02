import xlwt

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
#设置所有30行列宽为设置为18
all_sheet=[worksheet_1,worksheet_2,worksheet_3,worksheet_4,worksheet_5,worksheet_6,worksheet_7,worksheet_8,worksheet_9,
           worksheet_10,worksheet_11,worksheet_12,worksheet_13,worksheet_14,worksheet_15,worksheet_16,worksheet_17]
for i in all_sheet:
    for f in range (30):
        i.col(f).width = 256*20