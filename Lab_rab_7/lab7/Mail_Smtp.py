# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os

os.putenv('EMAIL_LOGIN', 'volodya.kumar@yandex.ru')
os.putenv('EMAIL_PASSWORD', '*456*654*')
os.putenv('IMAP_HOST', 'imap.yandex.ru')
os.putenv('IMAP_PORT', '993')
os.putenv('SMTP_HOST', 'smtp.yandex.ru')
os.putenv('SMTP_PORT', '465')
os.putenv('PERIOD_CHECK', '5')


def send_mail_admin(ps, fr, to, sb, ms):
    # create message object instance
    msg = MIMEMultipart()
    message = ms
    # setup the parameters of the message
    password = ps
    msg['From'] = fr
    msg['To'] = to
    msg['Subject'] = str(sb)
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    # create server
    server = smtplib.SMTP("smtp.yandex.ru:465", timeout=5)
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (msg['To']))


def send_mail_client(ps, fr, to, sb):
    # create message object instance
    msg = MIMEMultipart()
    # setup the parameters of the message
    password = ps
    msg['From'] = fr
    msg['To'] = to
    msg['Subject'] = str(sb)
    # create server
    server = smtplib.SMTP(os.getenv("SMTP_HOST"))
    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (msg['To']))
