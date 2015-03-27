#!/usr/bin/env python

import thread
import time

def loop0():
    print 'start loop 0 at:', time.ctime()
    time.sleep(4)
    print 'loop 0 done at', time.ctime()


def loop1():
    print 'start loop 1 at:', time.ctime()
    time.sleep(2)
    print 'loop 1 done at', time.ctime()


def loop(nloop, nsec,lock):
    print 'start loop', nloop, 'at:', time.ctime()
    time.sleep(nsec)
    print 'loop', nloop, 'done at:', time.ctime()
    lock.release()

loops = [4, 2]
def main():
    print 'starting at:', time.ctime()
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked(): pass

    print 'all done at:', time.ctime()


if __name__ == '__main__':
    main()
