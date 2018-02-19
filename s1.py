#-----coding:utf-8----
# !/usr/bin/env python3
# -*- coding: utf-8 -*-



import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.qq.com"  #设置服务器
mail_user="417144633@qq.com"    #用户名
mail_pass="cluvezxjwkkxcajc"   #口令

sender = '417144633@qq.com'
receivers = ['tianzhuizhe2@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

content = '过期教程害死人!'
title = 'Python SMTP Mail Test'  # 邮件主题
message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = title

subject = 'Happy new year!'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL()
    smtpObj.connect(mail_host, 465)  # 465 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")
print("ok")