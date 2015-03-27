#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys

def login(ip = '127.0.0.1', name='zxwqxtu', port = 22):
    sh = "ssh "+name+"@"+ip+" -p "+str(port)
    print sh
    os.popen(sh)

login('192.243.116.121', 'root', 28026)

