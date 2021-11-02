import yagmail

yag = yagmail.SMTP(user='hf1538379200qq@163.com',password='CRZAOHUIKKCQDLFA',host='smtp.163.com')

msg = ['正文内容1','正文内容2']

yag.send('1538379200@qq.com','测试消息',contents=msg)