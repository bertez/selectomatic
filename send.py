# -*- coding: utf-8 -*-
import config
import time
import csv
from mail import SendMail
from template import CreateTemplate
from random import randint
import sys


def process():
    with open(config.data) as data:
        people = csv.DictReader(data)

        for person in people:

            params = {key: value for key, value
                      in person.items()
                      if not key.startswith('_')}

            template = CreateTemplate(params, person['_template']).get()

            mail = SendMail(template, '{0} <{1}>'.format(person['_full_name'], person['_mail']),
                            'Gracias por te presentares á oferta de traballo da navalla suíza'.format(person['short_name']))
            mail.send()
            print 'Email sent to {0}'.format(person['_full_name'])
            time.sleep(randint(2,5))


if __name__ == '__main__':
    process()
