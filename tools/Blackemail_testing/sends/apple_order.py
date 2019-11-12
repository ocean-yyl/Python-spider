from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import parseaddr, formataddr
import smtplib
import time
import os


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 发送邮件函数
def send_email(from_addr, password, to_addr, txt_head, txt_msg):
    # 163网易邮箱服务器地址
    smtp_server = 'smtp.163.com'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header(txt_head, 'utf-8').encode()
    msgRoot['From'] = _format_addr(u'Apple<%s>' % from_addr)  # 设置发送人姓名
    msgRoot['To'] = _format_addr(to_addr)

    # msg text
    msg_text = MIMEText(txt_msg, 'html', 'utf-8')
    msgRoot.attach(msg_text)

    #msg img
    img_file = '../txt_msg/imgs/apple.png'
    img_id = 1
    fp = open(img_file, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<' + str(img_id) + '>')
    msgRoot.attach(msgImage)

    # 发送邮件
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msgRoot.as_string())
    print(to_addr, ":seng ok.")
    server.quit()


def send_msg(to_email='', txt_head='', txt_msg=''):
    # 发件人地址
    from_addr = 'to_Ocean_yyl@163.com'
    # 邮箱密码
    password = 'yyl123456789'
    # 收件人地址
    to_addr = to_email
    # 设置邮件信息
    txt_head = txt_head
    txt_msg = txt_msg
    send_email(from_addr, password, to_addr, txt_head, txt_msg)


def send_emails(e_file, txt_head="", htm_file=""):
    with open(e_file, encoding="utf-8") as e_f:
        elist = e_f.readlines()
    txt_head = txt_head
    with open(htm_file, encoding="utf-8") as f:
        txt_msg = f.read()

    baseurl = "http://39.96.166.6/login/"
    for e_addr in elist:
        # url = "http://127.0.0.1/login/"+e_addr
        url = baseurl + e_addr
        e_addr = e_addr.strip()
        txt_msg_new = txt_msg.replace("Ocean_yyl@163.com", e_addr)  # 更换邮箱
        txt_msg_new = txt_msg_new.replace("http://www.baidu.com", url)  # 更换url地址

        send_msg(to_email=e_addr, txt_head=txt_head, txt_msg=txt_msg_new)

if __name__ == '__main__':
    send_emails(e_file="../e-list", txt_head='Apple 确认订单', htm_file="../txt_msg/apple_order.html")
