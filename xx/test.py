#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys 
sys.path.append('/www/web/python')
import fun

fun.hi()

a = 'b'
print fun.a

from fun import hi
hi()

from libs import book

book1 = book('py')
print book1.getName(), book('java').getName(), book.name
book.name = 'xy'
print book1.name

#print book.getName()
print book1.staticMethod(),'_____', book.staticMethod()
print book.staticMethod2()
book.foo()
book.too()
setattr(book, 'age', '2002')
print book.age, book1.age, book._content, book1.abc
