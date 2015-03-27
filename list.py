def f(x):
    return x%2
l = range(0,10)
print filter(f, l)
l = []
l = ['abc', 'ABD', 'aBe']
l.append('abf')
l.extend(['acd'])
l = [1,2,3,1]
l.remove(1)
print l
'''

print('old:'+str(l))
l.sort()
print(l)

l.sort(key=str.lower, reverse=True)
print(l)
l.sort(key=None, reverse=True)
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
del l[0]
print(l)
'''

a = 1;
b = a;
a = 2;
print id(a), id(b)

import copy
b = a = [1,2,{'k':'k', 'v':'v'}]
c = copy.copy(a)
a[0] = 2
a[2]['k'] = 'kk'
print a, b, c
print id(a), id(b), id(c)

print 'abc'.find('b'), 'a' in 'abc'

'''
str = raw_input("please enter some numbers:");
a = [i for i in str.split(' ') if i is not '']
print sorted(a)
print sorted(a, reverse=True)
#a.sort()
print a
'''

def transe(str):
    new = ''
    for c in str:
        if c.islower():
            new += c.upper()
        else:
            new += c.lower()
    return new

str = 'aBcD'
print str, transe(str)

print {'0':'x',1:'xx', 0:'xx'}
