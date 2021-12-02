#!/bin/env python
# _*_ coding: UTF-8 _*_

import sys
import jenkins

usr = 'zogodo'
pwd = '123456'

ok = jenkins.Login(usr, pwd)
if not ok:
    sys.exit(1)

name = 'zgd_test'
