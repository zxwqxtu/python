#ClassOne.py

class ClassOne(object):
    #define class to simulate a simple calculator
    def __init__(self):
        self.current = 0
    def add(self, amount):
        self.current += amount
    def getCurrent(self):
        return self.current

class Animal:
    name = ''
    age = 0
    def __init__(self, name, age=0):
        self.name = name
        self.age = age 
    def add_trick(self):
        tricks = []

class Dog(Animal):
    name = ''
    tricks = []
    '''
    def __init__(self, name):
        self.name = name
        self.tricks = []
    '''
    def add_trick(self, trick):
        #Animal.add_trick()
        self.tricks.append(trick)

class MixData():
    pass

class B:
    pass
class C(B):
    pass
class D(C):
    pass

d1 = Dog('d1')
d2 = Dog('d2')
d1.add_trick('trick1')
d2.add_trick('trick2')
print d1.name
print d1.tricks
print d2.name
print d2.tricks

mixData = MixData()
mixData.x = 'x'
print mixData.x

for c in [B, C, D]:
    try:
        raise c()
    except D:
        print 'D'
    except C:
        print 'C'
    except B:
        print 'B'
