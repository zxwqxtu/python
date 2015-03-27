#!/usr/bin/python

import os
import sys 
import random


def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1

def max2(one, two):
    if one > two:
        return one
    else:
        return two
def my_max(aList):
    max = aList[0]
    for item in aList:
        if max < item:
            max = item
    return max
print "%s, %f" % ('a', 20)

def mult(n):
    return reduce(lambda x, y: x*y, range(1, n+1))
print 'reduce %d' % mult(5)
def printf(format="%s", *val):
    print val
    print format % val

printf("%s,%s,%s", 12, 13, 'a')

print my_max([1,2,3,4,5])
print max2(4, 8)
count = counter(5)
print count.next(),count.next(),count.send(9), count.next()

def simpleGen():
    yield 1
    yield '2->puchk'

a = simpleGen()
print a.next(), a.next()

for item in simpleGen():
    print item
print filter(lambda x: x%2, range(0, 10))
print map(lambda x: x**2, range(0, 10))
print reduce(lambda x,y:x+y, range(0, 5))
add = lambda x, y=3: x+y
print add(3,4), add(4)
print (lambda x, y=2: x*y)(3, 4)

def createTmpFile(c, l):
    f = os.tmpfile()
    while True:
        l -= 1
        if l < 0:
            break
        f.write(chr(random.randint(0, 255)))
    f.seek(0)
    num = 0
    for line in f:
        num += line.count(c)
    f.close()
    return num

print createTmpFile('c', 20450)

print 'babaaaa'.count('a')
exit()

dir = os.getcwd()
file1 = dir + '/' + sys.argv[1]
file2 = dir + '/' + sys.argv[2]
f1 = open(file1, 'rb')
f2 = open(file2, 'wb')
for line in f1:
    f2.write(line)
f1.close()
f2.close()
exit('ok')

file = dir + '/'+ raw_input('input file path:')
if not os.path.exists(file):
    exit('not file')
total = int(raw_input('input line total number:'))
num = 0
for line in open(file, 'r'):
    num += 1
    if num > total:
        break
    print line

exit('ok')


import os
file = os.getcwd() +'/out.log'
if (not os.path.exists(file)):
    exit('file not exists!')
f = open(file, 'r')
print f.readlines()
for line in f:
    print line ,
f.close()

'''
with open(file) as f:
    for line in f:
        print line
'''
exit()

for item in [1,2,3]:
    print item,

print 'basd', 'cccc'

who = 'knights'
what = 'Ni!'
print 'We are the %s who say %s' %\
        (who, ((what+' ')*4))

for c in who:
    print c,

print ''

list = [i ** 2 for i in range(4)]
print list

for v in [i ** 2 for i in range(4) if not i %2 ]:
    print v,

'''
fileName = raw_input('Enter file name:')
fp = open(fileName)
for eachLine in fp:
    print eachLine
fp.close()
'''

def foo(debug=False):
    'determine if in debug mode with default argument'
    if debug:
        print 'debug mode'
    else:
        print 'no debug mode'
    print 'done'

foo()
foo(True)


class cooCls(object):
    """my very first class: coo"""
    version = 0.1 #version
    def __init__(self, name='john'):
        self.name = name
        print 'Created a class instance for', name
    def showname(self):
        """display instance attribute and class name"""
        print 'Your name is ', self.name
        print 'My name is ', self.__class__.__name__
    def showver(self):
            print self.version
    def addMe2Me(self, x):
        return x*x
coo = cooCls()
coo.showname()

import sys
sys.stdout.write('Hello\n')

print sys.platform
print sys.version

num = 0
while(num <= 10):
    print num,
    num += 1 

print ''
for i in range(11):
    print i,
       
print dir()
print type(dir)


print min([1,2,4])
print min(1,2,4)
print min('123')

print 'aba'.count('a'),
print 'aba'.capitalize()
print 'aba'.encode()
print 'Aba'.lower()
print ' '.join(['a', 'b'])
print 'a b'.split(' ')
print ' ba '.strip(' ba')
print 'aaaaaa'.replace('a', 'b')
