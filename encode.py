#! /usr/bin/env python
# -*- coding:utf-8 -*-
#this
str = "#this\
        abaad"
str = """
aba
    csdfs

"""
str = r"aba\nxxx" + "xxxba"*3 
str = u'a\u0020' + 'b' 'c'
print str.encode('utf-8')
print str[1]
print str[1:3]
print "中国"
print ord('a')

l = ['span', 'eggs', 100, 1024]
print l
print l[:]
print len(l[1:-1])

a = 2
a, b = 0, 1+a
print a,b
