#coding:utf-8

import os
import time

class File:
    filePath = '/www/web/logs';

    "处理文件"
    def __init__(self, path=''):
        self.filePath = path or self.filePath 
        os.path.isdir(self.filePath) or os.mkdir(self.filePath)

    def writeLog(self, str, fileName):
        file = self.filePath+'/'+fileName
        global f
        try:
            f = open(file, "ab")
            f.write(str)
        except IOError:
            print 'error' 
            pass
        finally:
            f.close()
        return f.closed

    def logTmp(self):
        for i in range(1000):
            self.writeLog("\n"+str(i)+time.ctime(), '2.log');

    def delAll(self):
        for path in os.listdir(self.filePath):
            os.unlink(self.filePath+'/'+path)
        os.rmdir(self.filePath)
        

