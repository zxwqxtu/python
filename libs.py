#libs.py
# -*- coding:utf-8 -*-

class abstractClass:
    pass

class parentClass(abstractClass):
    flag = '0'
    
    def __init__(self):
        self.flag = 'parent'

class ChildClass(parentClass):
    "__init__"
    def __init__(self, flag = 'child'):
        parentClass.__init__(self)
        self.flag = flag 
        self.data = {'flag': 'xxxxx'} 

    "get Flag"
    def getFlag(self):
        return self.flag

    "set Flag"
    def setFlag(self, flag):
        self.flag = flag

    def __getitem__(self, flag):
        return self.data[flag]


class book(object):
    name = None
    _content = '中国'
    __title = '北京'
    def __init__(self, name):
        self.setName(name)
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def staticMethod():
        return 'static method'

    staticMethod = staticmethod(staticMethod)

    def staticMethod2(cls):
        return 'static method2___'+ cls.__name__

    staticMethod2 = classmethod(staticMethod2)

    @staticmethod
    def foo():
        print 'foo', book.name
    @classmethod
    def too(cl):
        print 'too', dir(cl)

    #魔术方法
    def __getattr__(self, attr):
        return attr

