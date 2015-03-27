a = dict(name='wq', age=26)
b = dict(zip(['name','age'], ['wq', 26]))
c = dict({'name':'wq', 'age':26})
d = dict([('name', 'wq'), ('age', 26)]);
print a, id(a)
print b, id(b)
print c, id(c)
print d, id(d)
print a == b == c == d
print len(a)
print 'name' in a, 'wq' in a, 'wq' not in a
a.clear()
print a
print b.keys(), b.items(), b.values()
print {}.fromkeys(['name', 'age'], ['wq', 26])
print set([1,2,3]), frozenset([1,2,3])
print c.update({'xx':'xx'}), c

c.update({23:34})
print c

print {('ok', 'bb'):1}
print sorted({'b':'b', 'a':'a', 'c':'c'}.keys())

keys = ['a', 'b', 'c', 'd']
values = ['aa', 'bb', 'cc', 'dd']
z = dict(zip(keys, values))
#z.sort()
print z
print dict(zip(z.values(), z.keys()))

print 'a' in set([1,2,3, 'a'])
print 'ok'

