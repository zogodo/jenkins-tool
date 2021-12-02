#!/bin/env python
# _*_ coding: UTF-8 _*_

import os
import sys
import re
import json
import requests

from urllib import urlencode
from urllib import quote
from urllib import unquote

from requests.sessions import session

# Suport Jenkins-2.249.1

myHeaders = {
    'Content-Type': 'application/x-www-form-urlencode',
}
seesion = requests.session()
server = '127.0.0.1:8080'
crumb = '1'

def DoPost(url, formData):
    myHeaders['Jenkins-Crumb'] = crumb
    r = seesion.post(url, data=urlencode(formData), headers=myHeaders)
    if r.status_code >= 300:
        print('post[%s] error status_code[%d]' % (url, r.status_code))
        print(r.text.encode('utf-8'))
        return False
    return True

def Login(usr, pwd):
    url = "http://%s/j_acegi_security_check" % (server, usr, pwd)
    formData = {
        'j_username': usr,
        'j_password': pwd,
        'remember_me': 'on',
    }
    if not DoPost(url, formData):
        print('jenkins login error!')
        return False
    str_re = r'data-crumb-value="(.+?)"'

def CreateItem(name):
    mode = 'hudsom.model.FreeStyleProject'
    formData = {
        'name': name,
        'mode': mode,
        'Jenkins-Crumb': crumb,
    }
    url = 'http://%s/view/all/createItem' % server
    return DoPost()
