import smtplib

sender = 'ppatel011102@gmail.com'
receivers = ['ppatel011102@gmail.com']

message = """From: Pratham Patel <ppatel011102@gmail.com>
To: Pratham Patel <ppatel011102@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    smtpObj.login("ppatel011102@gmail.com", "Prathamrajpatel11")
    print("Successfully sent email")
except smtplib.SMTPException:
    print("Error: unable to send email")
