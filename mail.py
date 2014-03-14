import smtplib
from email.mime.text import MIMEText
import config


class SendMail(object):
    def __init__(self, content, to, subject, sender=config.sender):
        self.to = to
        self.sender = sender
        self.content = MIMEText(content, _charset='utf-8')
        self.content['To'] = self.to
        self.content['From'] = '{name} <{mail}>'.format(name=config.sender_name, mail=config.sender)
        self.content['Subject'] = subject

    def send(self):
        server = smtplib.SMTP(config.smtp)
        server.starttls()
        server.login(config.sender, config.password)
        server.sendmail(config.sender, self.to, self.content.as_string())
        server.quit()