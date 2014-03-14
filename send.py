import config
import time
import csv
from mail import SendMail
from template import CreateTemplate


def process():
    with open(config.data) as data:
        people = csv.DictReader(data)

        for person in people:
            params = {key: value for key, value
                      in person.items()
                      if not key.startswith('_')}

            template = CreateTemplate(params, person['_template']).get()

            mail = SendMail(template, person['_mail'],
                            'Hello, {0}, this is a personal \ email'.format(person['short_name']))
            mail.send()
            print 'Email sent to {0}'.format(person['_full_name'])
            time.sleep(2)


if __name__ == '__main__':
    process()
