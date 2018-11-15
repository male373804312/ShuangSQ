# -*- coding:utf-8 -*-
import requests
import re
import random
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
UA = random.choice(user_agent_list)  ##从self.user_agent_list中随机取出一个字符串
headers = {'User-Agent': UA}  ##构造成一个完整的User-Agent （UA代表的是上面随机取出来的字符串哦）

url = "http://kaijiang.500.com/ssq.shtml"



opt = requests.get(url, headers=headers)
time.sleep(5)
# print opt.text

phase = re.findall(r'<font class="cfont2"><strong>(\d+)</strong>', opt.text)
print phase


number = re.findall(r'<li class="ball_red">(\d+)</li>', opt.text)
bulenum = re.findall(r'<li class="ball_blue">(\d+)</li>', opt.text)
print number
print bulenum
# a = ''
# for i in number:
#     a =+ str(i)
#     print a




def email():
    # 构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype
    # 传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    # msg = MIMEText(message, 'html', 'utf-8')  # message为传入的参数,为发送的消息.
    msg = MIMEText('<html><body><h1>Hello</h1>' +
                   '<p>本期红球为:'+ str(number[0]) +','+str(number[1])+','+str(number[2])+','+str(number[3])+','+str(number[4])+','+str(number[5])+'</p>' +
                   '<p>本期蓝球为:'+ str(bulenum[0]) +'</p>'+'</body></html>', 'html', 'utf-8')
    # 标准邮件需要三个头部信息： From, To, 和 Subject。
    msg['From'] = formataddr(["male", '373804312@qq.com'])  # 显示发件人信息
    msg['To'] = formataddr(["大家好", '349622541@qq.com'])  # 显示收件人信息
    msg['Subject'] = str(phase[0])+"期"  # 定义邮件主题
    try:
        # 创建SMTP对象
        server = smtplib.SMTP("smtp.qq.com", 25)
        # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        # server.set_debuglevel(1)
        # login()方法用来登录SMTP服务器
        server.login("373804312@qq.com", "***************")
        # sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
        server.sendmail('373804312@qq.com', ['373804312@qq.com'], msg.as_string())
        print u"邮件发送成功!"

        server.quit()
    except smtplib.SMTPException:
        print u"Error: 无法发送邮件"

 email()
