# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/28 15:40

import smtplib
import traceback

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

from application.configure import setting


def send_mail(subject, text, to=[], files=None):
    msg = MIMEMultipart()

    email_from = u'刘开增<liukaizeng1111@126.com>'.encode('utf-8')

    msg['From'] = email_from
    msg['Subject'] = subject
    msg['to'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg.attach(MIMEText(text, 'html', _charset='utf-8'))

    try:
        server = smtplib.SMTP(setting.EMAIL_HOST, setting.EMAIL_PORT)
        server.login(setting.EMAIL_HOST_USER, setting.EMAIL_HOST_PASSWORD)
        server.sendmail(email_from, to, msg.as_string())
        server.quit()
    except Exception as e:
        print traceback.format_exc(e)


if __name__ == '__main__':
    send_mail('sdfsd', 'sdfsdf', ['1051299241@qq.com'])