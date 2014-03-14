import config
import time
import csv
from mail import SendMail
from template import CreateTemplate


def process():
    with open(config.data) as data:
        people = csv.DictReader(data)

        for item in people:
            template = CreateTemplate(item).get()
            mail = SendMail(template, item['mail'], 'Hello, {name}, this is a personal email'.format(name=item['short_name']))
            mail.send()
            print 'Email sent to {0}'.format(item['name'])
            time.sleep(2)


if __name__ == '__main__':
    process()
