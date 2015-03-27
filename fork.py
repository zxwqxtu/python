import os
import time

ret = os.fork()
if ret:

    time.sleep(1)
    f = os.popen('ps -ef|grep py')
    data = f.read()
    f.close()
    #time.sleep(1)
    #os.wait()
    print data
else:
    time.sleep(2)
    print 'child fork'
