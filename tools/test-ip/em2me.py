#coding:utf-8
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import datetime

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 发送邮件函数
def send_email(from_addr, password, to_addr, txt_head, txt_msg):
    # 163网易邮箱服务器地址
    smtp_server = 'smtp.163.com'

    msg = MIMEText(txt_msg, 'html', 'utf-8')
    msg['Subject'] = Header(txt_head, 'utf-8').encode()
    msg['From'] = _format_addr(from_addr)
    msg['To'] = _format_addr(to_addr)

    # 发送邮件
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print(datetime.datetime.now(),"发送邮件。")
    server.quit()

def send_1():

        # 发件人地址
        from_addr = 'to_Ocean_yyl@163.com'
        # 邮箱密码
        password = 'yyl123456789'
        # 收件人地址
        to_addr = 'Ocean_yyl@163.com'
        # 设置邮件信息
        txt_head = '网络异常'
        txt_msg = '网络访问异常，查看日志'
        send_email(from_addr, password, to_addr, txt_head, txt_msg)

if __name__ == '__main__':
    send_1()