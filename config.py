# -*- coding: utf-8 -*-
sender_name = ''
sender = ''
password = ''
smtp = 'smtp.gmail.com:587'
data = 'data/candidates.csv'

try:
    from real_config import *
except ImportError:
    pass
