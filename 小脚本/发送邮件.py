from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_the_mail(content, sub):
	mail_host = 'smtp.126.com'
	mail_user = 'aaaaa'
	mail_pass = 'xxxxxxxxxxx'
	sender = 'aaaaa@126.com'
	receivers = 'aaaaa@outlook.com'
	message = MIMEText(content,'plain','utf-8')
	message['From'] = _format_addr('Python邮件库功能 <%s>' % sender)
	message['To'] = _format_addr(receivers)
	message['Subject'] = Header(sub, 'utf-8').encode()
	try:
		smtpObj = smtplib.SMTP()
		smtpObj.connect(mail_host, 25)
		smtpObj.login(mail_user, mail_pass)
		smtpObj.sendmail(sender, [receivers], message.as_string())
		smtpObj.quit()
		print('success')
	except smtplib.SMTPException as e:
		print('error', e)


def main():
	content = 'https://www.notebooksbilliger.de/nvidia+geforce+rtx+3060+ti+founders+edition'
	sub = '请注意,有原价显卡出现'
	send_the_mail(content, sub)

if __name__ == '__main__':
	main()