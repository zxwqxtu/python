#! /usr/bin/env python
# -*- coding:utf-8 -*-

import os

path = '/www/web/fms/application/wms/views/'

def replaceAll(path):
    for item in os.listdir(path):
        subPath = os.path.join(path, item)
        if os.path.isdir(subPath):  
            replaceAll(subPath)
        elif os.path.basename(subPath)[-6:] == '.phtml':
            f = open(subPath, 'r+')
            str = f.read()
            f.seek(0)
            f.truncate()
            str = str.replace('北京兴长信达 WMS 后台管理系统','<?php echo APP_TITLE;?>')
            f.write(str)
            f.close()

replaceAll(path)

