# 2018.12.18
# maxzjs
# -*- coding:utf-8 -*-
# send_mail.py
# SMTP发送邮件
# 内置了SMTP支持
# 发送一个纯文本协议

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# MIMEText对象，第一个参数是邮件正文，第二个参数是subtype，‘plain’表示纯文本，最后一定要用utf-8编码保证多语言兼容性
# 然后，通过SMTP发出去

# 输入Email地址和口令
from_addr = input('【邮件地址】：')
password = input('【请输入密码】：')
# 输入收件人地址：
to_addr = input('【发送到】：')
# 输入SMTP服务器地址
smtp_server = input('【SMTP服务器地址】：')

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()


